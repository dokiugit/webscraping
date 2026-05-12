import pandas as pd


def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {e}")
