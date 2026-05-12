from utils.transform import transform_data


def test_transform():
    data = [
        {
            "title": "Test",
            "price": "$100.00",
            "rating": "Rating: 4.5 / 5",
            "colors": "3 Colors",
            "size": "Size: M",
            "gender": "Gender: Men",
            "timestamp": "2025-01-01"
        }
    ]

    df = transform_data(data)

    assert df.iloc[0]["price"] == 1600000
    assert df.iloc[0]["rating"] == 4.5
