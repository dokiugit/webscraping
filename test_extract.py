from utils.extract import parse_product
from bs4 import BeautifulSoup


def test_parse_product():
    html = """
    <div class="collection-card">
        <div class="product-details">
            <h3 class="product-title">Test Product</h3>
            <span class="price">$100.00</span>
            <p>Rating: 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Men</p>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    card = soup.find("div", class_="collection-card")

    result = parse_product(card)

    assert result["title"] == "Test Product"
    assert "$" in result["price"]
