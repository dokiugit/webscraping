import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://fashion-studio.dicoding.dev"


def get_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_product(card):
    try:
        title = card.find("h3", class_="product-title").text.strip()

        price_tag = card.find("span", class_="price")
        price = price_tag.text.strip() if price_tag else "Price Unavailable"

        details = card.find_all("p")

        rating_text = details[0].text.strip()
        colors_text = details[1].text.strip()
        size_text = details[2].text.strip()
        gender_text = details[3].text.strip()

        timestamp = datetime.now().isoformat()

        return {
            "title": title,
            "price": price,
            "rating": rating_text,
            "colors": colors_text,
            "size": size_text,
            "gender": gender_text,
            "timestamp": timestamp
        }
    except Exception as e:
        print(f"Error parsing product: {e}")
        return None


def scrape_all():
    results = []

    for page in range(1, 51):
        try:
            url = BASE_URL if page == 1 else f"{BASE_URL}/page{page}"
            html = get_page(url)

            if not html:
                continue

            soup = BeautifulSoup(html, "html.parser")
            cards = soup.find_all("div", class_="collection-card")

            for card in cards:
                product = parse_product(card)
                if product:
                    results.append(product)

        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    return results
