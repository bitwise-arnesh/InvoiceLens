def create_freight_per_unit(df):
    df["freight_per_unit"] = (
        df["Freight"] / df["Quantity"]
    )

    return df


def analyze_quantity_segments(df):
    low_quantity = df["Quantity"].quantile(0.25)
    high_quantity = df["Quantity"].quantile(0.75)

    low_mean = df.loc[
        df["Quantity"] < low_quantity,
        "freight_per_unit"
    ].mean()

    high_mean = df.loc[
        df["Quantity"] > high_quantity,
        "freight_per_unit"
    ].mean()

    print(f"Low Quantity Mean Freight/Unit : {low_mean:.4f}")
    print(f"High Quantity Mean Freight/Unit : {high_mean:.4f}")