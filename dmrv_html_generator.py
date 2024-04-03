import requests
from bs4 import BeautifulSoup
import pandas as pd
from ydata_profiling import ProfileReport

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
spo_providers = soup.find_all(class_='views-field views-field-field-bond-spo-provider')

# Extract text from the found elements
bond_ids_text = [element.get_text().strip() for element in bond_ids]
entities_text = [element.get_text().strip() for element in entities]
amounts_issued_text = [element.get_text().strip() for element in amounts_issued]
currencies_text = [element.get_text().strip() for element in currencies]
issue_dates_text = [element.get_text().strip() for element in issue_dates]
maturity_dates_text = [element.get_text().strip() for element in maturity_dates]
cbi_certified_text = [element.get_text().strip() for element in cbi_certified]
spo_providers_text = [element.get_text().strip() for element in spo_providers]

# Since the first row of data should be the column labels, prepare data accordingly
data = zip(bond_ids_text[1:], entities_text[1:], amounts_issued_text[1:], currencies_text[1:], issue_dates_text[1:], maturity_dates_text[1:], cbi_certified_text[1:], spo_providers_text[1:])

# Define column labels based on the first row (now removed from data)
columns = ['BondID', 'Entity', 'Amount Issued', 'Currency', 'Issue Date', 'Maturity Date', 'CBI Certified', 'SPO Provider']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)


def getHTMLTable():
    df.style.set_table_styles([
            {'selector': 'table', 
                'props': 'font-family: arial, sans-serif; border-collapse: collapse; width: 100%;'},
            {'selector': 'td, th', 
                'props': 'text-align: left; padding: 8px;'},
            {'selector': 'tr:nth-child(even)', 
                'props': 'background-color: #dddddd;'}
        ], overwrite=False)
    return df.to_html()# Converts the dataframe to HTML table format

def getProfileReport():
    return ProfileReport(df).to_html()# Generates profile