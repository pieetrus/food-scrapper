from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 10)
driver.get('https://www.ubereats.com/pl')
city_name = 'Wrocław'

city_input = driver.find_element_by_xpath('//*[@id="location-typeahead-home-input"]')
find_btn = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[2]/div/div[1]/button')
city_input.send_keys(city_name)
time.sleep(1) #todo: use some event instead
find_btn.click()

# show more loading
while True:
    try:
        driver.execute_script("document.querySelectorAll('button')[document.querySelectorAll('button').length - 1].click();", WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div/button'))))
        print("Show more button clicked.")
    except:
        print("No more content to load.")
        break
