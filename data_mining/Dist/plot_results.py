import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

def plot_confusion_matrix(cm, labels, title):
    ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels).plot(cmap='Blues')
    plt.title(title)
    plt.show()

def compare_model_accuracies(results):
    plt.bar(results.keys(), results.values(), color=['blue', 'green', 'orange'])
    plt.title('Model Accuracy Comparison')
    plt.xlabel('Models')
    plt.ylabel('Accuracy')
    plt.show()
