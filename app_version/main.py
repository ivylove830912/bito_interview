import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# set webdriver
driver = webdriver.Chrome('chromedriver')

# set url
app_store_url = 'https://apps.apple.com/tw/app/bitopro/id1393007496'
google_play_url = 'https://play.google.com/store/apps/details?id=com.bitoex.bitoproapp'

# direct to google play url
driver.get(google_play_url)
time.sleep(3)

# click button to show version message
driver.find_element(By.XPATH, "//*[text()='關於這個應用程式']/../..//button").click()

# get version text
time.sleep(5)
google_play_version = driver.find_element(By.XPATH, "//*[text()='版本']/..//div[last()]").text

# direct to app store url
driver.get(app_store_url)
time.sleep(5)

# get version text
app_play_version = driver.find_element(By.XPATH, "//*[@class='l-column small-6 medium-12 whats-new__latest__version']").text

# compare version
if app_play_version.split()[-1] == google_play_version:
    print("The version number is the same!!!")
else:
    print("The version number is not the same!!!")
