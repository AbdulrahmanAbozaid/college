from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from plot_results import plot_confusion_matrix

def run_decision_tree(x_train, y_train, x_test, y_test):
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Decision Tree Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, predictions))

    cm = confusion_matrix(y_test, predictions)
    return accuracy, cm

if __name__ == '__main__':
    # Test this module standalone
    from preprocessing import load_and_preprocess_data
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from imblearn.over_sampling import SMOTE

    data = load_and_preprocess_data("spam_dataset.csv")
    x = data['cleaned_message']
    y = data['is_spam']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    tfid = TfidfVectorizer(stop_words="english")
    x_train_tfid = tfid.fit_transform(x_train)
    x_test_tfid = tfid.transform(x_test)

    smote = SMOTE()
    x_train_tfid, y_train = smote.fit_resample(x_train_tfid.toarray(), y_train)

    accuracy, cm = run_decision_tree(x_train_tfid, y_train, x_test_tfid, y_test)
    plot_confusion_matrix(cm, ['Not Spam', 'Spam'], "Decision Tree Confusion Matrix")
