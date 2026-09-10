"""
Evaluation and validation.

Stubbed per the project plan (docs/ML_Model_Development_Plan.docx, Section 5):
- Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC, confusion matrix
- Stratified 5-fold cross-validation
- Learning curves, calibration check, threshold tuning
"""


def evaluate_model(model, X_test, y_test):
    """Compute the metric suite described in Section 5. To be implemented."""
    raise NotImplementedError("Implement per Section 5 of the development plan.")


def cross_validate_model(model, X, y, cv=5):
    """Stratified k-fold cross-validation per Section 5.1. To be implemented."""
    raise NotImplementedError("Implement per Section 5.1 of the development plan.")
