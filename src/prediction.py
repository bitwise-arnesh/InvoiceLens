import pandas as pd


def predict_new_invoice(model):

    input_data = {
        "Quantity": [500, 200],
        "Dollars": [18500, 9000]
    }

    df = pd.DataFrame(input_data)

    preds = model.predict(df)

    print("\nPredictions")
    print(preds)

    return preds