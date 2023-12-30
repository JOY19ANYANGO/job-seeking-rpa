from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com/")
print("Page Title:", driver.title)
object_name = driver.find_element(By.CLASS_NAME,"RNNXgb")
# object_name.send_keys("test")
# object_name.send_keys(Keys.RETURN)
print("Page Title:", driver.page_source)

driver.quit()