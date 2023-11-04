def comparePrices():
  
    # Initialize empty lists to store the product prices, names and domains
    price = []
    name = []
    domain = []

    product_fetched = True

    # Loop through the range of 1 to 3 to get the URLs of the products
    for i in range(1, 3):
        website_url = input("Enter the URL of the product: ")

        # Check if the URL belongs to Flipkart
        if 'flipkart' in website_url:
            from flipkartScrapper import flipkartScrapper
            [product_name, domain_name, product_price] = flipkartScrapper(
                website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to Amazon
        elif 'amazon' in website_url:
            from amazonScrapper import amazonScrapper
            [product_name, domain_name,
                product_price] = amazonScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        else:
            print("enter a valid URL")
            break

    if (product_fetched == False):
        return

    # Remove the currency symbol and commas from the prices
    for i in range(len(price)):
        price[i] = price[i].replace('₹', '')
        price[i] = price[i].replace(',', '')
        price[i] = price[i].replace('.', '')

    # Find the minimum price and its index in the list
    min_price = min(price)
    min_price_index = price.index(min_price)

    # Print the website where the product is cheaper
    print(
        f'Best Buy option here \n {name[min_price_index]} is available at {domain[min_price_index]} for ₹{min_price}')


comparePrices()

