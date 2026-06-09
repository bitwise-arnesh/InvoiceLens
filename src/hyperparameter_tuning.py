from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV


def tune_xgboost(X_train, y_train):

    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [2, 4, 6],
        "learning_rate": [0.01, 0.05, 0.1]
    }

    grid_search = GridSearchCV(
        estimator=XGBRegressor(
            random_state=42
        ),
        param_grid=param_grid,
        scoring="r2",
        cv=5,
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    print("\nBest Parameters")
    print(grid_search.best_params_)

    print("\nBest CV Score")
    print(grid_search.best_score_)

    return grid_search.best_estimator_