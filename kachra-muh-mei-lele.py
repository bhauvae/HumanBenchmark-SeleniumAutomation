from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=r'./chromedriver-win64/chromedriver.exe'))
# Website URL
human_benchmark_url = 'https://www.startupindia.gov.in/content/sih/en/search.html/Uttar-Pradesh?states=5f48ce592a9bb065cdf9fb3f&roles=Startup&page=3330'
driver.get(human_benchmark_url)

# Wait for the page to load
time.sleep(1000)


# Pause to interact with the page (you can remove this if not needed)
input("Press Enter to exit")

# Close the WebDriver
driver.quit()
