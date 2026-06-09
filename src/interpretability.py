import pandas as pd
import shap


def feature_importance_analysis(model, X):

    importance = model.feature_importances_

    result = pd.DataFrame({
        "Feature": X.columns,
        "Importance": importance
    })

    result = result.sort_values(
        "Importance",
        ascending=False
    )

    print(result)

    return result


def shap_analysis(model, X_test):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_test)

    shap.summary_plot(
        shap_values,
        X_test
    )