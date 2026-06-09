import joblib
from pathlib import Path

from data_preprocessing import (
    load_vendor_data,
    prepare_features,
    split_data
)

from feature_engineering import (
    create_freight_per_unit,
    analyze_quantity_segments
)

from model_training import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    train_xgboost
)

from model_evaluation import (
    evaluate_model
)

from hyperparameter_tuning import (
    tune_xgboost
)

from interpretability import (
    feature_importance_analysis,
    shap_analysis
)

from prediction import (
    predict_new_invoice
)


def main():

    print("\nLoading Data...")

    df = load_vendor_data(
        "data/inventory.db"
    )

    print("Data Loaded Successfully")

    print("\nRunning Feature Engineering...")

    df = create_freight_per_unit(df)

    analyze_quantity_segments(df)

    print("\nPreparing Features...")

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = split_data(
        X,
        y
    )

    print("\nTraining Models...")

    lr_model = train_linear_regression(
        X_train,
        y_train
    )

    dt_model = train_decision_tree(
        X_train,
        y_train
    )

    rf_model = train_random_forest(
        X_train,
        y_train
    )

    xgb_model = train_xgboost(
        X_train,
        y_train
    )

    print("\nEvaluating Models...")

    evaluate_model(
        lr_model,
        X_test,
        y_test,
        "Linear Regression"
    )

    evaluate_model(
        dt_model,
        X_test,
        y_test,
        "Decision Tree Regression"
    )

    evaluate_model(
        rf_model,
        X_test,
        y_test,
        "Random Forest Regression"
    )

    evaluate_model(
        xgb_model,
        X_test,
        y_test,
        "XGBoost Regression"
    )

    print("\nRunning GridSearchCV Hyperparameter Tuning...")

    best_xgb = tune_xgboost(
        X_train,
        y_train
    )

    evaluate_model(
        best_xgb,
        X_test,
        y_test,
        "Tuned XGBoost"
    )

    print("\nRunning Feature Importance Analysis...")

    feature_importance_analysis(
        best_xgb,
        X
    )

    print("\nRunning SHAP Explainability...")

    shap_analysis(
        best_xgb,
        X_test
    )

    print("\nPredicting Freight Cost for New Invoices...")

    predict_new_invoice(
        lr_model
    )

    print("\nSaving Models...")

    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)

    joblib.dump(
        lr_model,
        model_dir / "linear_regression.pkl"
    )

    joblib.dump(
        best_xgb,
        model_dir / "tuned_xgboost.pkl"
    )

    print("\nModels Saved Successfully")
    print("\nInvoiceLens Pipeline Completed Successfully")


if __name__ == "__main__":
    main()