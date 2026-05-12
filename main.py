from utils.extract import scrape_all
from utils.transform import transform_data
from utils.load import load_to_csv


def main():
    print("Extracting...")
    raw_data = scrape_all()

    print("Transforming...")
    clean_data = transform_data(raw_data)

    print("Loading...")
    load_to_csv(clean_data)


if __name__ == "__main__":
    main()

