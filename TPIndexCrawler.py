from lxml import html
from selenium import webdriver
import multiprocessing
import time
import datetime
import mysql.connector

categories = {
    'tp01': 'https://www.tokopedia.com/p/kategori-fashion-wanita?ob=8',
    'tp02': 'https://www.tokopedia.com/p/kategori-fashion-pria?ob=8',
    'tp03': 'https://www.tokopedia.com/p/kategori-fashion-muslim?ob=8',
    'tp04': 'https://www.tokopedia.com/p/kategori-fashion-anak?ob=8',
    'tp05': 'https://www.tokopedia.com/p/kategori-kecantikan?ob=8',
    'tp06': 'https://www.tokopedia.com/p/kateogri-kesehatan?ob=8',
    'tp07': 'https://www.tokopedia.com/p/kategori-perawatan-tubuh?ob=8',
    'tp08': 'https://www.tokopedia.com/p/kategori-handphone-tablet?ob=8',
    'tp09': 'https://www.tokopedia.com/p/kategori-laptop-aksesoris?ob=8',
    'tp10': 'https://www.tokopedia.com/p/kategori-komputer-aksesoris?ob=8',
    'tp11': 'https://www.tokopedia.com/p/kategori-elektronik?ob=8',
    'tp12': 'https://www.tokopedia.com/p/kategori-kamera?ob=8',
    'tp13': 'https://www.tokopedia.com/p/kategori-gaming?ob=8',
    'tp14': 'https://www.tokopedia.com/p/kategori-ibu-bayi?ob=8',
    'tp15': 'https://www.tokopedia.com/p/kategori-rumah-tangga?ob=8',
    'tp16': 'https://www.tokopedia.com/p/kategori-dapur?ob=8',
    'tp17': 'https://www.tokopedia.com/p/kategori-makanan-minuman?ob=8',
    'tp18': 'https://www.tokopedia.com/p/kategori-souvenir-kado?ob=8',
    'tp19': 'https://www.tokopedia.com/p/kategori-buku?ob=8',
    'tp20': 'https://www.tokopedia.com/p/kategori-otomotif?ob=8',
    'tp21': 'https://www.tokopedia.com/p/kategori-olahraga?ob=8',
    'tp22': 'https://www.tokopedia.com/p/kategori-film-musik?ob=8',
    'tp23': 'https://www.tokopedia.com/p/kategori-office-stationery?ob=8',
    'tp24': 'https://www.tokopedia.com/p/kategori-mainan-hobi?ob=8',
    'tp25': 'https://www.tokopedia.com/p/kategori-software?ob=8',
}


def collectData(kode, url, page, numberOfPage):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument('headless')
    browser = webdriver.Chrome(options=chromeOptions,executable_path=r'C:/Users/dormamu/AppData/Local/Programs/Python/Python37-32/chromedriver.exe')
    if (page == 0):
        browser.get(url)
        innerHTML = browser.execute_script("return document.body.innerHTML")
        browser.close()
    elif (page != 0):
        modUrl = url + str('&page=') + str(page)
        browser.get(modUrl)
        innerHTML = browser.execute_script("return document.body.innerHTML")
        browser.close()
    htmlElem = html.document_fromstring(innerHTML)
    nama = htmlElem.cssselect('div.product-name.ng-binding')
    link = htmlElem.cssselect('a.category-tracker')
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bltp"
    )
    dbcursor = dbconnection.cursor()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    dbcursor.execute("SELECT link FROM tpindextest")
    listlink = dbcursor.fetchall()
    for i in range(0, len(nama)):
        try:
            if (((link[i * 2].get('ng-href').split('?trkid=')[0],)) in listlink) :
                dbcursor.execute('UPDATE tpindextest SET lastcheck = %s WHERE link = %s', (timestamp, link[i * 2].get('ng-href').split('?trkid=')[0]))
            else:
                dbcursor.execute('INSERT INTO tpindextest (link, kategori, lastcheck) VALUES (%s,%s,%s)',(link[i * 2].get('ng-href').split('?trkid=')[0], kode, timestamp))
        except:
            print('error. check connection?')
    if page < numberOfPage:
        collectData(kode, url, page+1)
    dbconnection.close


if __name__ == '__main__':
    mulai = time.time()
    numberOfPage = 1
    #multiprocessing.freeze_support()
    processes = [ ]
    for kode,nama in categories.items():
        print('process '+kode)
        t = multiprocessing.Process(target=collectData, args=(kode, nama, 1, numberOfPage))
        processes.append(t)
        t.start()

    for one_process in processes:
        one_process.join()

    print('')
    print('elapsed time'+str(time.time()-mulai))