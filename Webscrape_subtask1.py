from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the desired website
url = 'https://www.bbc.com/news' 
driver.get(url)

#  Wait for the page to load
time.sleep(5)  

#  Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

#  Locate and extract all <a> and <p> tags
a_tags = soup.find_all('a')
p_tags = soup.find_all('p')

# Initialize a list to store the scraped data
article_data = []

# Loop through <a> tags to extract links and titles
for a in a_tags:
    title = a.get_text(strip=True)
    link = a['href']
    
    # Ensure full URL (in case of relative URLs)
    if link.startswith('/'):
        link = f'https://www.bbc.com{link}'
    
    # Append <a> tag data to the list
    article_data.append({
        'Type': 'Link',
        'Title': title,
        'URL': link,
        'Content': ''
    })

#  Loop through <p> tags to extract content
for p in p_tags:
    content = p.get_text(strip=True)
    
    # Append <p> tag data to the list
    article_data.append({
        'Type': 'Paragraph',
        'Title': '',
        'URL': '',
        'Content': content
    })

#  Convert the data into a pandas DataFrame
df = pd.DataFrame(article_data)

#  Save the data to a CSV file with labels
df.to_csv('D:/technical task/all_data_scraped.csv', index=False)
print("Scraping complete. Data saved to all_data_scraped.csv")

# Close the browser
driver.quit()
