import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)


def main():
    # Load the saved model path (hard-coded or param)
    model_path = "models/xgboost_test_gini0.2840.pkl"  # Example
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Load test data
    test_df = pd.read_csv('data/test.csv')
    X_test = test_df.drop('target', axis=1)
    y_test = test_df['target']

    # Predict probabilities
    y_prob = model.predict_proba(X_test)[:, 1]
    # Convert to binary predictions (threshold=0.5)
    y_pred = (y_prob >= 0.5).astype(int)

    # Compute metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    print("=== Model Evaluation ===")
    print(f"Accuracy:      {acc:.4f}")
    print(f"Precision:     {prec:.4f}")
    print(f"Recall:        {rec:.4f}")
    print(f"F1-Score:      {f1:.4f}")
    print(f"ROC-AUC Score: {auc:.4f}\n")

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    print("=== Confusion Matrix ===")
    print(cm)

    print("\nEvaluation done!")


if __name__ == "__main__":
    main()
