from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Navigate to the desired website (e.g., BBC News)
url = 'https://www.bbc.com/news'  # Change this to your target website
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(5)  # You can adjust this based on your internet speed

# Step 4: Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Step 5: Locate and extract all <a> and <p> tags
a_tags = soup.find_all('a')
p_tags = soup.find_all('p')

# Initialize a list to store the scraped data
article_data = []

# Step 6: Loop through <a> tags to extract links and titles
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

# Step 7: Loop through <p> tags to extract content
for p in p_tags:
    content = p.get_text(strip=True)
    
    # Append <p> tag data to the list
    article_data.append({
        'Type': 'Paragraph',
        'Title': '',
        'URL': '',
        'Content': content
    })

# Step 8: Convert the data into a pandas DataFrame
df = pd.DataFrame(article_data)

# Step 9: Save the data to a CSV file with labels
df.to_csv('D:/technical task/all_data_scraped.csv', index=False)
print("Scraping complete. Data saved to all_data_scraped.csv")

# Step 10: Close the browser
driver.quit()