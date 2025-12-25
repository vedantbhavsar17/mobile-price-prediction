from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\bhavs\OneDrive\Desktop\geckodriver.exe") # Driver Path
driver = webdriver.Firefox(service=service)

driver.get('https://www.smartprix.com/mobiles') #Data Scrapped Smartprix website
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/div/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/div/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.find_element(by=By.XPATH, value='/html/body/div/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source # Full Page HTML


#Created a local file for HTML
with open('smartprix.html','w',encoding='utf-8') as f: 
    f.write(html)