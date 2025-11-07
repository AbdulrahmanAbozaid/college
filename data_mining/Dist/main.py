from preprocessing import load_and_preprocess_data
from decision_tree import run_decision_tree
from knn import run_knn
from naive_bayes import run_naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
from compare_models import compare_models
import matplotlib.pyplot as plt

# Load and preprocess data
data = load_and_preprocess_data("spam_dataset.csv")

# Display dataset information
print("Dataset Analysis:")
print(f"Total Emails: {len(data)}")
print(f"Spam Emails: {data['is_spam'].sum()} ({data['is_spam'].sum() / len(data) * 100:.2f}%)")
print(f"Non-Spam Emails: {len(data) - data['is_spam'].sum()} ({(len(data) - data['is_spam'].sum()) / len(data) * 100:.2f}%)\n")

# Visualize class distribution
plt.figure(figsize=(6, 4))
data['is_spam'].value_counts().plot(kind='bar', color=['blue', 'orange'], alpha=0.7)
plt.title('Class Distribution')
plt.xticks([0, 1], ['Not Spam', 'Spam'], rotation=0)
plt.ylabel('Count')
plt.show()

# Analyze email lengths
data['email_length'] = data['message_content'].apply(len)
data['cleaned_length'] = data['cleaned_message'].apply(len)

# Plot original vs cleaned email lengths
plt.figure(figsize=(10, 5))
plt.hist(data['email_length'], bins=50, alpha=0.7, label='Original', color='purple')
plt.hist(data['cleaned_length'], bins=50, alpha=0.7, label='Cleaned', color='green')
plt.title('Email Length Distribution')
plt.xlabel('Email Length')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Split data
x = data['cleaned_message']
y = data['is_spam']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Vectorize text data
tfid = TfidfVectorizer(stop_words="english")
x_train_tfid = tfid.fit_transform(x_train)
x_test_tfid = tfid.transform(x_test)

# Handle class imbalance
smote = SMOTE()
x_train_tfid, y_train = smote.fit_resample(x_train_tfid.toarray(), y_train)

# Run models and collect results
results = {}
results['Decision Tree'], _ = run_decision_tree(x_train_tfid, y_train, x_test_tfid, y_test)
results['KNN'], _ = run_knn(x_train_tfid, y_train, x_test_tfid, y_test)
results['Naive Bayes'], _ = run_naive_bayes(x_train_tfid, y_train, x_test_tfid, y_test)

# Compare results
compare_models(results)
