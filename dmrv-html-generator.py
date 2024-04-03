import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://www.climatebonds.net/cbi/pub/data/bonds'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the specified classes
bond_ids = soup.find_all(class_='views-field-title')
entities = soup.find_all(class_='views-field-field-bond-entity')
amounts_issued = soup.find_all(class_='views-field-field-bond-amt-issued')
currencies = soup.find_all(class_='views-field-field-bond-currency')
issue_dates = soup.find_all(class_='views-field-field-bond-issue-date')
maturity_dates = soup.find_all(class_='views-field-field-bond-maturity-date')
cbi_certified = soup.find_all(class_='views-field-field-bond-verifier')

# Extract text from the found elements
bond_ids_text = [element.get_text().strip() for element in bond_ids]
entities_text = [element.get_text().strip() for element in entities]
amounts_issued_text = [element.get_text().strip() for element in amounts_issued]
currencies_text = [element.get_text().strip() for element in currencies]
issue_dates_text = [element.get_text().strip() for element in issue_dates]
maturity_dates_text = [element.get_text().strip() for element in maturity_dates]
cbi_certified_text = [element.get_text().strip() for element in cbi_certified]

# Print the collected data (for demonstration)
data = zip(bond_ids_text, entities_text, amounts_issued_text, currencies_text, issue_dates_text, maturity_dates_text, cbi_certified_text)


df = pd.DataFrame(data)

def getHTMLTable():
    return df.to_html()  # print the dataframe