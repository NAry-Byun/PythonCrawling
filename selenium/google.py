from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Add this import
from selenium.webdriver.support import expected_conditions as EC

import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=ko&tab=wi&authuser=0&ogbl")

# Locate the search box using an explicit wait
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
elem.send_keys("Melbourne")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except NoSuchElementException:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        # Adjusted XPath for the image URL
        imgUrl = driver.find_element_by_xpath('//img[@class="n3VNCb"]').get_attribute("src")
        
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass

driver.quit()