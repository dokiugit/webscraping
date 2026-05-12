import pandas as pd
import re


def transform_data(data):
    try:
        df = pd.DataFrame(data)

        # Remove invalid
        df = df[df["title"] != "Unknown Product"]

        # Clean price → convert to IDR
        def convert_price(p):
            if "Unavailable" in p:
                return None
            value = float(p.replace("$", ""))
            return value * 16000

        df["price"] = df["price"].apply(convert_price)

        # Clean rating
        df["rating"] = df["rating"].str.replace("Rating:", "").str.replace("/ 5", "").str.strip()
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

        # Clean colors
        df["colors"] = df["colors"].str.extract(r"(\d+)").astype(float)

        # Clean size
        df["size"] = df["size"].str.replace("Size:", "").str.strip()

        # Clean gender
        df["gender"] = df["gender"].str.replace("Gender:", "").str.strip()

        # Drop null
        df = df.dropna()

        # Remove duplicates
        df = df.drop_duplicates()

        return df

    except Exception as e:
        print(f"Error transforming data: {e}")
        return pd.DataFrame()
