#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install selenium')


# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:





# # solution1

# In[ ]:


driver=webdriver.Chrome()


# In[ ]:


driver.get("https://www.naukri.com/")


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Scientist')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_location=[]
salary=[]


# In[ ]:


#scratching job location
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    
    
#scratching salary

salary_tags=driver.find_elements(By.XPATH,'//span[@class=""]')
for tag in salary_tags:  
    sal = tag.text  
    salary.append(sal)


# In[ ]:


print(len(job_location),len(salary))


# In[ ]:


import pandas as ps
df=pd.DataFrame({'Location':job_location,'income':salary})
print(df.head(10))


# # solution3
# 

# In[ ]:


driver=webdriver.Chrome()


# In[ ]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=F")


# In[ ]:


article_rating=[]
article_Review_Summary=[]
article_Full_Review=[]


# In[ ]:


rating_tags=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in rating_tags:
    rate=i.text
    article_rating.append(rate)    


# In[ ]:


#scraping review summary


review_tags=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')  
for tag in review_tags:  
    review = tag.text  
    article_Review_Summary.append(review)
    
#scraping article full samary
full_review_tags = driver.find_elements(By.XPATH, '//p[@class="z9E0IG"]')
for review in full_reviews:  
    full_review_text = review.text  
    article_Full_Review.append(full_review_text)


# In[ ]:





# In[ ]:





# # solution 2

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Step 1: Open the Shine.com webpage
driver.get('https://www.shine.com/')
time.sleep(3)  # Allow the page to load

# Step 2: Enter "Data Scientist" in the Job title field and "Bangalore" in the location field
job_title_field = driver.find_element(By.ID, 'id_q')
job_title_field.send_keys('Data Scientist')

location_field = driver.find_element(By.ID, 'id_loc')
location_field.send_keys('Bangalore')

# Step 3: Click the search button
search_button = driver.find_element(By.CLASS_NAME, 'cls_searchJob')
search_button.click()

# Allow the search results to load
time.sleep(5)

# Step 4: Scrape the data for the first 10 job results
job_titles = []
job_locations = []
company_names = []
experience_required = []

# Fetch the first 10 jobs
jobs = driver.find_elements(By.CLASS_NAME, 'result-display__profile')[:10]

for job in jobs:
    try:
        # Scrape the job title
        job_title = job.find_element(By.CSS_SELECTOR, 'a.job-title').text
        job_titles.append(job_title)
        
        # Scrape the company name
        company_name = job.find_element(By.CSS_SELECTOR, 'span.result-display__profile__company-name').text
        company_names.append(company_name)
        
        # Scrape the location
        location = job.find_element(By.CSS_SELECTOR, 'li.job-location').text
        job_locations.append(location)
        
        # Scrape the experience required
        experience = job.find_element(By.CSS_SELECTOR, 'li.job-experience').text
        experience_required.append(experience)
    
    except Exception as e:
        print(f"Error scraping job: {e}")
        continue

# Step 5: Create a DataFrame from the scraped data
jobs_data = {
    'Job Title': job_titles,
    'Company Name': company_names,
    'Location': job_locations,
    'Experience Required': experience_required
}

df = pd.DataFrame(jobs_data)

# Display the DataFrame
print(df)


# In[ ]:





# # solution 4

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_flipkart_sneakers_selenium(num_sneakers=100):
  """Scrapes data for sneakers on Flipkart.com using Selenium.

  Args:
      num_sneakers (int, optional): The number of sneakers to scrape. Defaults to 100.

  Returns:
      list: A list of dictionaries containing scraped sneaker data.
  """

  # Replace with the actual path to your WebDriver (e.g., chromedriver.exe)
  driver_path = "path/to/your/webdriver"
  driver = webdriver.Chrome(executable_path=driver_path)

  sneakers_data = []
  page_num = 1

  while len(sneakers_data) < num_sneakers and page_num <= 10:  # Limit to 10 pages
    url = f"https://www.flipkart.com/search?q=sneakers&sort=popularity&otracker=nmenu_search&otracker1=navigation_menu&marketplace=FLIPKART&as=off&as-show=off&otracker2=nav_search&page={page_num}"
    driver.get(url)

    try:
      # Wait for page to load (adjust wait times as needed)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_2kFwH')))

      soup = BeautifulSoup(driver.page_source, 'html.parser')

      # Extract sneaker data based on Flipkart's HTML structure (might need adjustments)
      sneaker_cards = soup.find_all('div', class_='_2kFwH')

      for sneaker_card in sneaker_cards:
        brand = sneaker_card.find('div', class_='UGa5b8').text.strip()
        description = sneaker_card.find('a', class_='_3Sq6M-').text.strip()
        price = sneaker_card.find('div', class='_30jeQ7').text.strip()

        sneakers_data.append({
            'Brand': brand,
            'Product Description': description,
            'Price': price
        })

        if len(sneakers_data) == num_sneakers:
          break

    except Exception as e:
      print(f"Error occurred while scraping page {page_num}: {e}")

    page_num += 1

  driver.quit()
  return sneakers_data

if __name__ == '__main__':
  # Example usage
  sneakers = scrape_flipkart_sneakers_selenium()
  print(sneakers)


# # solution 6

# In[ ]:


import selenium  
from selenium import webdriver  
from bs4 import BeautifulSoup  
import time  
  
# Set up the webdriver  
driver = webdriver.Chrome()  # Replace with your preferred browser  
  
# Navigate to the webpage  
driver.get("https://www.azquotes.com/")  
  
# Click on the "Top Quotes" button  
top_quotes_button = driver.find_element_by_xpath("//a[@href='/top_quotes']")  
top_quotes_button.click()  
  
# Wait for the page to load  
time.sleep(2)  
  
# Parse the HTML content of the page with BeautifulSoup  
soup = BeautifulSoup(driver.page_source, 'html.parser')  
  
# Find all quote elements on the page  
quotes = soup.find_all('div', class_='quote')  
  
# Create lists to store the scraped data  
quotes_list = []  
authors_list = []  
types_list = []  
  
# Loop through each quote element and extract the data  
for quote in quotes:  
    quote_text = quote.find('p', class_='quoteText').text.strip()  
    author = quote.find('span', class_='author').text.strip()  
    quote_type = quote.find('span', class_='quoteType').text.strip()  
    
    quotes_list.append(quote_text)  
    authors_list.append(author)  
    types_list.append(quote_type)  
  # Print the scraped data  
for i in range(len(quotes_list)):
    
    print(f"Quote {i+1}: {quotes_list[i]}")  
    print(f"Author: {authors_list[i]}")  
    print(f"Type: {types_list[i]}")  
    print("------------------------") 


# # solution 5

# In[130]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Step 1: Open Amazon India website
driver.get('https://www.amazon.in/')
time.sleep(3)  # Allow the page to load

# Step 2: Enter "Laptop" in the search field and click the search icon
search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('Laptop')
search_field.send_keys(Keys.RETURN)  # Press enter to search
time.sleep(3)

# Step 3: Set the CPU Type filter to "Intel Core i7"
# Scroll down to find the filter option (Amazon uses dynamic IDs so we might need to adjust by label text)
cpu_filter = driver.find_element(By.XPATH, "//span[text()='Intel Core i7']")
cpu_filter.click()
time.sleep(3)  # Allow the page to refresh after applying the filter

# Step 4: Scrape the first 10 laptop results
laptops_data = []
laptops = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")[:10]

for laptop in laptops:
    try:
        # Scrape the title
        title = laptop.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
        
        # Scrape the rating (some products may not have ratings, handle exceptions)
        try:
            rating = laptop.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        except:
            rating = "No rating"
        
        # Scrape the price (handle cases where the price is not listed)
        try:
            price = laptop.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "Price not available"
        
        # Append the scraped data to the list
        laptops_data.append({
            'Title': title,
            'Rating': rating,
            'Price': price
        })
    
    except Exception as e:
        print(f"Error scraping laptop data: {e}")
        continue

# Step 5: Create a DataFrame from the scraped data
df = pd.DataFrame(laptops_data)

# Display the DataFrame
print(df)

# Close the driver
driver.quit()


# In[ ]:




