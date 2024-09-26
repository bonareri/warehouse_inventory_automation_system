import requests
from bs4 import BeautifulSoup
from database import add_product
import random  # Import the random module for generating random quantities

def scrape_products():
    url = 'https://www.jumia.co.ke/' 
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the products on the page
        products = soup.find_all('article', class_='prd _box _hvr')

        for product in products:
            # Extract product details
            link = product.select_one('a.core')
            name = product.select_one('.name').get_text(strip=True) if product.select_one('.name') else "N/A"
            price = product.select_one('.prc').get_text(strip=True) if product.select_one('.prc') else "N/A"
            
            # Get quantity information from the stock element
            stock_element = product.select_one('.stk')
            if stock_element:
                stock_text = stock_element.get_text(strip=True)
                quantity = int(stock_text.split()[0]) if "items left" in stock_text else 0
            else:
                quantity = 0

            # If quantity is not available or is zero, assign a random quantity between 1 and 500
            if quantity == 0:
                quantity = random.randint(1, 500)

            # Get the product category from the link attribute if available
            category = link['data-ga4-item_category'] if link and 'data-ga4-item_category' in link.attrs else "N/A"

            # Save the scraped product to the database
            add_product(name, price, quantity, category)

        print("Scraped product data has been added to the database.")
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

if __name__ == '__main__':
    scrape_products()
