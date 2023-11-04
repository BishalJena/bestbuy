from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}


def amazonScrapper(url):
    """
    This function takes in a url of an Amazon product page and returns the price and website name.

    Parameters:
    url (str): The url of the Amazon product page.

    Returns:
    tuple: A tuple containing the product name (str), website name (str), and price (str).
    """

    # Send a request to the url and get the html content
    try:
        html_text = requests.get(url, headers=header).text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the URL: {e}")
        return None, None, None

    # Parse the html content using BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')

    # Check if the product is available or not
    if not soup.find('div', class_='a-alert-content'):
        print("Product not found on Amazon.")
        return None, None, None
    # Getting the name of the product
    try:
        title_div = soup.find('div', id='titleSection')
        title_h1 = title_div.find('h1', id='title').text.strip()
        product_name = title_h1
    except Exception as e:
        print(
            f"An error occurred while trying to get the name of the product: {e}")
        return None, None, None

    # Check if the product name is available or not
    if product_name is None:
        print("Unable to get name of the product please try again later or try another product")
        return None, None, None

    # Getting the price of the product
    try:
        price_span = soup.find('span', class_='a-price-whole')
        price = price_span.text.strip()
    except Exception as e:
        print(
            f"An error occurred while trying to get the price of the product: {e}")
        return None, None, None

    # Check if the price is available or not
    if price is None:
        print("Unable to get price of the product please try again later or try another product")
        return None, None, None

    # Getting the name of website
    try:
        website_source = soup.find('title')
        website_source = website_source.text.strip().split(' ')[-1]
    except Exception as e:
        print(
            f"An error occurred while trying to get the name of the website: {e}")
        return None, None, None

    # Check if the website name is available or not
    if website_source is None:
        print("Unable to get name of the website please try again later or try another product")
        return None, None, None

    # Print the product name, website name and price
    print(
        f'The Product: {product_name} is available at {website_source} for Rs.{price}')

    return product_name, website_source, price