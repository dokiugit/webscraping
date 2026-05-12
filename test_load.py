
import pandas as pd
from utils.load import load_to_csv


def test_load():
    df = pd.DataFrame({
        "title": ["Test"],
        "price": [100],
    })

    load_to_csv(df, "test.csv")

    loaded = pd.read_csv("test.csv")

    assert len(loaded) == 1
``
