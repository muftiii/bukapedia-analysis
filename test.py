from lxml import html
from selenium import webdriver
import multiprocessing
import time
import datetime
import mysql.connector

start = time.time()
url = 'https://www.tokopedia.com/ninscollections/munafie-tebal-munafie-slimming-pants-tebal'
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_argument('headless')
browser = webdriver.Chrome(options=chromeOptions,executable_path=r'C:/Users/dormamu/AppData/Local/Programs/Python/Python37-32/chromedriver.exe')
browser.get(url)
innerHTML = browser.execute_script("return document.body.innerHTML")
browser.close()
htmlElem = html.document_fromstring(innerHTML)
view = htmlElem.cssselect('div.view-count')[0].text_content()
sold = htmlElem.cssselect('div.item-sold-count')[0].text_content()
merchLink = htmlElem.cssselect('div.rvm-merchat-name a')[0].get('href')
merchName = htmlElem.cssselect('span.shop-name')[0].text_content()
harga = htmlElem.cssselect('div.rvm-price span')[1].get('content')
lokasi = htmlElem.cssselect('div.rvm-merchat-city span')[0].text_content()
print(view)
print(sold)
print(merchLink)
print(merchName)
print(harga)
print(lokasi)
print('konversi : ')

print('elapsed time '+str(time.time()-start))
