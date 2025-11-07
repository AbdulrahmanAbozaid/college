"""
Classifier For Spam Messages
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import nltk


nltk.download('stopwords')

# Phase 1: Know Your Data
data = pd.read_csv("spam_dataset.csv")
print(data.head())
print(data.info())
print(data['is_spam'].value_counts())

# Visualize class distribution
sns.countplot(x='is_spam', data=data, palette='husl')
plt.title('Class Distribution')
plt.show()

# Phase 2: PreProcessing
# Drop duplicates
data = data.drop_duplicates()

# Text preprocessing function
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = ' '.join(word for word in text.split() if word not in stop_words)
    text = ' '.join(stemmer.stem(word) for word in text.split())
    return text

# Apply preprocessing
data['cleaned_message'] = data['message_content'].apply(preprocess_text)

# Check data after cleaning
print(data[['message_content', 'cleaned_message']].head())

# Phase 3: Data Analysis and Visualization
# Message length analysis
data['message_length'] = data['cleaned_message'].apply(len)
sns.histplot(data[data['is_spam'] == 0]['message_length'], bins=30, color='blue', label='Not Spam', kde=True)
sns.histplot(data[data['is_spam'] == 1]['message_length'], bins=30, color='red', label='Spam', kde=True)
plt.legend()
plt.title('Message Length Distribution')
plt.show()

# Phase 4: Data Mining (Classification)
# Splitting the dataset
x = data['cleaned_message']
y = data['is_spam']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Vectorization using TF-IDF
tfid = TfidfVectorizer(stop_words="english")
x_train_tfid = tfid.fit_transform(x_train)
x_test_tfid = tfid.transform(x_test)

# Handle class imbalance
smote = SMOTE()
x_train_tfid, y_train = smote.fit_resample(x_train_tfid.toarray(), y_train)

# Models: Decision Tree, KNN, Naive Bayes
models = {
    'Decision Tree': DecisionTreeClassifier(),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': MultinomialNB()
}

results = {}

for model_name, model in models.items():
    print(f"Training {model_name}...")
    model.fit(x_train_tfid, y_train)
    predictions = model.predict(x_test_tfid)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy for {model_name}: {accuracy:.2f}")
    print(classification_report(y_test, predictions))

    cm = confusion_matrix(y_test, predictions)
    ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Spam', 'Spam']).plot(cmap='Blues')
    plt.title(f"Confusion Matrix: {model_name}")
    plt.show()

    results[model_name] = accuracy

# Compare Model Accuracies
plt.bar(results.keys(), results.values(), color=['blue', 'green', 'orange'])
plt.title('Model Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.show()

print("Final Accuracy Scores:")
for model_name, accuracy in results.items():
    print(f"{model_name}: {accuracy:.2f}")
