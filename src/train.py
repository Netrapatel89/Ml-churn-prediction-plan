"""
Model training and hyperparameter tuning.

Stubbed per the project plan (docs/ML_Model_Development_Plan.docx, Section 4):
- Stratified train/validation/test split
- Baseline (majority class), Logistic Regression, Random Forest, XGBoost
- Grid/Randomized search with stratified k-fold cross-validation
"""


def train_baseline_models(X_train, y_train):
    """Train the candidate models listed in Section 4.1. To be implemented."""
    raise NotImplementedError("Implement per Section 4 of the development plan.")


def tune_hyperparameters(model, param_distributions, X_train, y_train, cv=5):
    """Run randomized/grid search per Section 4.4. To be implemented."""
    raise NotImplementedError("Implement per Section 4.4 of the development plan.")
