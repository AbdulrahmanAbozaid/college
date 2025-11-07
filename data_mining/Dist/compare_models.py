from plot_results import compare_model_accuracies

def compare_models(results):
    print("Final Accuracy Scores:")
    for model_name, accuracy in results.items():
        print(f"{model_name}: {accuracy:.2f}")
    compare_model_accuracies(results)
