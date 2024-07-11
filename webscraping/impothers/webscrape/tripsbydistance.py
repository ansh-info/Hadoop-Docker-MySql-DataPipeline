from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the WebDriver
driver_service = Service(ChromeDriverManager().install())

# Uncomment the line below to specify the path to ChromeDriver locally
# driver_service = Service('/path/to/your/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=driver_service, options=options)

# URL of the NYC Open Data Air Quality page
url = "https://data.bts.gov/Research-and-Statistics/Trips-by-Distance/w96p-f2qv/data_preview"
driver.get(url)

# Allow the page to load
time.sleep(5)

def scrape_table():
    global columns
    # Locate the table
    table = driver.find_element(By.CLASS_NAME, 'ag-root-wrapper-body')
    
    # Retrieve the table headers only on the first page
    if not columns:
        header_elements = driver.find_elements(By.CSS_SELECTOR, '.ag-header-cell-label .ag-header-cell-text')
        columns = [header.text for header in header_elements if header.text.strip() != '']
        print("Headers found:", columns)  # Debug print
    
    # Retrieve the table rows
    rows = table.find_elements(By.CSS_SELECTOR, '.ag-row')

    # Collect data
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, '.ag-cell')
        row_data = [cell.text for cell in cells]
        
        # Debugging: Print row length
        print(f"Row length: {len(row_data)}, Expected: {len(columns)}")
        
        # Ensure row length matches column length, adjust headers if necessary
        if len(row_data) > len(columns):
            additional_columns = len(row_data) - len(columns)
            columns.extend([f"Extra_Column_{i+1}" for i in range(additional_columns)])
        
        data.append(row_data)

data = []
columns = []  # Ensure columns is defined

# Scrape the first page
scrape_table()

# Pagination logic
page_number = 1
max_pages = 10

while page_number < max_pages:
    try:
        # Try to find the "Next" button using the correct class
        next_button = driver.find_element(By.CSS_SELECTOR, '.ag-button.ag-paging-button[ref="btNext"]')
        if next_button.is_enabled():
            next_button.click()
            time.sleep(5)  # Allow time for the next page to load
            scrape_table()
            page_number += 1
        else:
            break
    except Exception as e:
        print("No more pages or error:", e)
        break

# Close the driver
driver.quit()

# Save the scraped data to a local file
if data:
    df = pd.DataFrame(data, columns=columns)
    local_file_path = 'tripsbydistance_data.csv'
    df.to_csv(local_file_path, index=False)
    print(f"Data successfully saved to {local_file_path}")
else:
    print("No data found")
