import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Creating a new workbook and worksheet for storing cellphone data
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Cellphones"

# Headers to simulate a human user when making HTTP requests
im_human = {'user-agent': 'Chrome/91.0.4472.124'}

def scrape_items(url):
    # Used to try to execute the code as expected; if not, a message is transmitted indicating a problem.
    try:
        # Receives the code from the HTTPS GET request
        response = requests.get(url, headers=im_human)

        # The library constructor is called, receiving as parameters the response of the request.
        # Note that the code is only checked under the condition that the request is successful.
        # The .text attribute contains the content of the response, i.e., the HTML content of the downloaded web page.
        # The second attribute represents the chosen parser, in this case, Python's native parser.
        soup = BeautifulSoup(response.text, 'html.parser')

        # The object to be checked is found by its class. Often, the class is a good choice because
        # All common items often have the same class. Facilitating the selection of specific items.
        smarthPhone_class = 'sc-fBWQRz cULVBz sc-fulCBj fxxByy sc-heIBml bMUpMo'

        # Locating the product with the find function ('tag_name', attribute_1='value_1', attribute_2='value_2', ...)
        smartphones_product = soup.find('ul', class_=smarthPhone_class)

        # It is checked if the variable has any value. If not, the search failed and the variable will receive the value None,
        # Which is natively recognized as False.
        if smartphones_product:
            # Initializing a list to store the extracted information
            info = [['Smartphone', 'Price']]
            for item in smartphones_product.find_all('li', class_='sc-kTbCBX ciMFyT'):
                # Extracting the product name and price from the HTML structure
                product_name_tag = item.find('a').find('div', class_='sc-dcjTxL xDJfk').find('h2')
                product_price_tag = item.find('a').find('div', class_='sc-fqkvVR hlqElk sc-bOQTJJ jWlrTP').find('div').find('div').find('p')

                # Checks if product_name_tag and product_price_tag exist before adding them to the list, i.e., if they are not None in type.
                if product_name_tag and product_price_tag:
                    info.append([
                        product_name_tag.text.strip(),
                        product_price_tag.text.strip()]
                    )
                else:
                    # If either the name or price is not found, print an error message
                    print("Phone name or price not found.")
            return info
        else:
            print(f"No smartphones with class '{smarthPhone_class}' were found on the page.")
            return None
    except requests.exceptions.RequestException as e:
        # Handles exceptions related to making HTTP requests
        print(f"Failed to access the page. Please check if the URL is correct.\n\n\n Error: {e}")

    except Exception as e:
        # Handles unexpected exceptions
        print(f"An unexpected error occurred. Contact support. Error: {e}")

# URL of the page with the list of items
website_url = 'https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/'

# Get the list of items with names and prices
items_list = scrape_items(website_url)

if items_list:
    # Appending the extracted information to the worksheet
    for rows in items_list:
        worksheet.append(rows)
else:
    print("Failed to access the list of items.")

# Saving the workbook with the extracted data
print('Smartphone data collection completed successfully!')
workbook.save("Price Spreadsheet.xlsx")
