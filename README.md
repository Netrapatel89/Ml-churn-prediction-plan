# ML Churn Prediction — Development & Evaluation Plan

Week 3 assignment: a conceptual, step-by-step plan for developing and evaluating a
machine learning model in Python. No model is trained in this repo — the deliverable
is the design document, diagrams, and a scaffolded project structure that a real
implementation would follow.

**Use case:** predict which customers of a subscription-based telecom service are
likely to churn within the next 30 days.

## Contents

- [`docs/ML_Model_Development_Plan.docx`](docs/ML_Model_Development_Plan.docx) — full written plan (problem definition, preprocessing, model selection, evaluation, deployment)
- [`assets/workflow_diagram.png`](assets/workflow_diagram.png) — end-to-end ML workflow diagram
- [`assets/cv_diagram.png`](assets/cv_diagram.png) — k-fold cross-validation diagram
- `src/` — stubbed pipeline modules mirroring the plan's phases (not yet implemented)
- `notebooks/` — placeholder for exploratory data analysis
- `data/` — placeholder for raw/processed data (git-ignored)

## Project structure

```
ml-churn-prediction-plan/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── ML_Model_Development_Plan.docx
├── assets/
│   ├── workflow_diagram.png
│   └── cv_diagram.png
├── notebooks/
│   └── 01_eda.ipynb            # placeholder
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py   # cleaning, encoding, scaling, feature engineering
│   ├── train.py                # model training + hyperparameter tuning
│   └── evaluate.py             # metrics, cross-validation, reporting
└── data/                       # raw/ and processed/ (git-ignored)
```

## Plan summary

1. **Problem definition** — churn prediction, framed as a binary classification task.
2. **Data preprocessing** — cleaning, normalization, feature engineering, feature selection.
3. **Model selection & training** — Logistic Regression baseline vs. Random Forest / XGBoost, with grid/random search hyperparameter tuning.
4. **Evaluation** — Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC, validated with stratified 5-fold cross-validation.
5. **Deployment (optional)** — packaging, REST API serving, drift monitoring, retraining cadence.

See the full plan in `docs/ML_Model_Development_Plan.docx` for the complete
write-up, justifications, and diagrams.

## Getting started (for a future real implementation)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## License

For coursework / educational use.
