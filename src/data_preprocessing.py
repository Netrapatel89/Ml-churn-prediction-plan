"""
Data preprocessing pipeline for churn prediction.

Stubbed per the project plan (docs/ML_Model_Development_Plan.docx, Section 3):
- Cleaning (missing values, duplicates, outliers)
- Normalization / scaling
- Feature engineering (tenure buckets, spend trend, support ratio)
- Feature selection (variance/correlation filtering, RFE)

This module intentionally contains no executed logic yet -- it mirrors the
structure a full implementation would use.
"""

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


def build_preprocessing_pipeline(numeric_features, categorical_features):
    """Return a scikit-learn ColumnTransformer implementing the cleaning/
    scaling/encoding steps described in the plan. To be implemented."""
    raise NotImplementedError("Implement per Section 3 of the development plan.")


def engineer_features(df):
    """Derive tenure buckets, spend trend, and support-interaction ratio
    features as described in Section 3.3 of the plan."""
    raise NotImplementedError("Implement per Section 3.3 of the development plan.")
