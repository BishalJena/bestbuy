# Price Comparison Tool

This tool allows users to compare prices of products between Amazon and Flipkart. It scrapes product information from both websites and provides a comparison to help users find the best deal.

## Features

- Scrapes product information from Amazon and Flipkart
- Compares prices between the two platforms
- Identifies the best buying option

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- pip package manager

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/bishaljena/bestbuy.git
   cd bestbuy
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. When prompted, enter the URLs of the product from Amazon and Flipkart.

3. The script will display the product information and compare the prices, showing you the best buying option.

## Project Structure

- `main.py`: The main script that orchestrates the price comparison
- `amazonScrapper.py`: Contains the function to scrape product information from Amazon
- `flipkartScrapper.py`: Contains the function to scrape product information from Flipkart
- `requirements.txt`: Lists the required Python packages

## How It Works

1. The `comparePrices()` function in `main.py` prompts the user for product URLs.
2. Depending on the URL (Amazon or Flipkart), it calls the respective scraping function.
3. The scraping functions (`amazonScrapper()` and `flipkartScrapper()`) extract the product name, price, and website name.
4. The main function compares the prices and displays the best buying option.

## Limitations

- The tool relies on the current structure of Amazon and Flipkart web pages. Changes to their HTML structure may break the scraping functionality.
- Some products may not be available or may have different structures, which could lead to errors.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for educational purposes only. Please respect the terms of service of the websites you are scraping. Excessive use of this tool may result in your IP being blocked by Amazon or Flipkart.
