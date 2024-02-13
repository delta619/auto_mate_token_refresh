import logging
import sys
from selenium import webdriver
import time
import schedule

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Function to open website, wait for 10 seconds, and then close the browser
def open_website():
    try:
        # Path to Chrome executable
        chrome_binary = r'C:/Users/ashu/Downloads/chrome/chrome.exe'

        # Path to ChromeDriver executable
        chrome_driver_path = r'C:/Users/ashu/Downloads/chromedriver/chromedriver.exe'

        # URL of the website you want to open
        website_url = 'https://play.fresco.me'

        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_binary
        chrome_options.add_argument('--disable-background-networking')
        chrome_options.add_argument('--disable-background-timer-throttling')
        chrome_options.add_argument('--enable-chrome-browser-cloud-management')

        profile_directory = r'C:/Users/ashu/AppData/Local/Google/Chrome For Testing/User Data/'
        chrome_options.add_argument(f'--user-data-dir={profile_directory}')

        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website
        driver.get(website_url)
        logging.info('Opened website')

        time.sleep(5)  # Wait for 10 seconds

        # Close the browser
        current_url = driver.current_url
        if current_url.startswith("https://play.fresco.me"):
            logging.info("Successfully refreshed")
        else:
            logging.error("Unsuccessful refresh, Token epired")
        driver.quit()
        logging.info('Closed browser')
    except Exception as e:
        # Log error
        logging.error(f'Error occurred: {e}')

# Schedule the function to run every 1 hour
schedule.every(2).hours.do(open_website)
logging.info('Schedule started')

# Keep the script running indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
