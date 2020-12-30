from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys

import time
import random

chrome_profile = Options()
chrome_profile.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3641.0 Safari/537.36') #new
chrome_profile.add_argument(
    "--user-data-dir=C:\\Users\\abhin\\AppData\\Local\\Google\\Chrome\\selenium")
browser = webdriver.Chrome(options=chrome_profile)
browser.get("https://web.whatsapp.com/")

time.sleep(15)


search_box = browser.find_element_by_xpath ('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
search_box.click()
search_box.send_keys("John Doe")
search_box.send_keys(Keys.ENTER)

text_box = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

no_of_texts = 100 # replace with the number of spam texts you want to sent

for i in range(no_of_texts):
    time.sleep(random.uniform(0.20,1.5))
    text_box.click()
    text_message = "Hi, this is a spam text" # replace with a witty insult or any other text of your liking
    text_box.send_keys(text_message)
    text_box.send_keys(Keys.ENTER)