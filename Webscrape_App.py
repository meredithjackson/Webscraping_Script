import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
table = soup.find('table', {'class': 'wikitable'})

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr'):
    rows.append([cell.text.strip() for cell in row.find_all(['td', 'th'])])

# Remove empty rows
rows = [row for row in rows if row]

# Convert data into a DataFrame
df = pd.DataFrame(rows)

# Print the DataFrame
print(df)