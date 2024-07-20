from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard
username = r''
password = r''
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=r'./chromedriver-win64/chromedriver.exe'))

human_benchmark_url = 'https://humanbenchmark.com/login'
driver.get(human_benchmark_url)

time.sleep(2)

username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_submit = driver.find_element(By.XPATH, '//*[@class="css-z5gx6u e19owgy712"]')

# Enter your login credentials
username_field.send_keys(username)
password_field.send_keys(password)
login_submit.click()

time.sleep(5)

typing_test_url = 'https://humanbenchmark.com/tests/typing'
driver.get(typing_test_url)

text_elements = driver.find_elements(By.CLASS_NAME, 'incomplete')
text_list = []

for text_element in text_elements:
    text = text_element.text
    if text == "":
        text = " "
    text_list.append(text)

text_to_type = "".join(text_list)

time.sleep(5)

keyboard.write(text_to_type)

time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[1]/div/div[3]/button[1]').click()

input("Press Enter to close the browser window...")
driver.quit()
