from lxml import html
from selenium import webdriver
import multiprocessing
import time
import datetime
import mysql.connector


def collectItemData(kode):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument('headless')
    browser = webdriver.Chrome(options=chromeOptions,
                               executable_path=r'C:/Users/dormamu/AppData/Local/Programs/Python/Python37-32/chromedriver.exe')
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bltp"
    )
    dbcursor = dbconnection.cursor()
    dbcursor.execute('SELECT link FROM tpindextest WHERE kategori = %s', (kode,))
    linkCollection = dbcursor.fetchall()
    for item in linkCollection:
        print(item[0])

    browser.get(url)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    browser.close()
    htmlElem = html.document_fromstring(innerHTML)






if __name__ == '__main__':
    collectItemData('tp01')
