import sys
import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract product name
    name_tag = soup.find('h1', class_="product_title")
    name = name_tag.text.strip() if name_tag else "N/A"

    # Extract price
    price_tag = soup.find('span', class_="price")
    price = price_tag.text.strip() if price_tag else "N/A"

    # Extract image URL
    img_tag = soup.find('img', class_="wp-post-image")
    img_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else "N/A"

    print("Product Name:", name)
    print("Price:", price)
    print("Image URL:", img_url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrape_numerouno.py <product_url>")
        sys.exit(1)
    product_url = sys.argv[1]
    scrape_product(product_url)