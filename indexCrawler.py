from lxml import html
from selenium import webdriver
import multiprocessing
import time
import csv

baseUrl = "https://www.tokopedia.com/p/"
page = 1
categoriesWanita = {
    't0001':'fashion-wanita/atasan',
    't0002':'fashion-wanita/celana',
    't0003':'fashion-wanita/rok',
    't0004':'fashion-wanita/dress',
    't0005':'fashion-wanita/outwear',
    't0006':'fashion-wanita/setelan',
    't0007':'fashion-wanita/batik-warna',
    't0008':'fashion-wanita/pakaian-dalam-wanita',
    't0009':'fashion-wanita/tas',
    't0010':'fashion-wanita/sepatu',
    't0011':'fashion-wanita/jam-tangan',
    't0013':'fashion-wanita/perhiasan',
    't0014':'fashion-wanita/aksesoris',
    't0015':'fashion-wanita/aksesoris-rambut',
    't0016':'fashion-wanita/perlengkapan-couple',
    't0017':'fashion-wanita/baju-tidur',
    't0018':'fashion-wanita/perlengkapan-jahit'
    }
sorting = '?ob=8'

def collectData(tipe, url, page):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument('headless')
    browser = webdriver.Chrome(options=chromeOptions,
                               executable_path=r'C:/Users/dormamu/AppData/Local/Programs/Python/Python37-32/chromedriver.exe')
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
    review = htmlElem.cssselect('span.reviewer-count.ng-binding')
    harga = htmlElem.cssselect('div.product-price.ng-binding')
    link = htmlElem.cssselect('a.category-tracker')
    #jumlah = 0
    for i in range(0, len(nama)):
        try:
            print(tipe, nama[i].text_content(), harga[i].text_content(), review[i].text_content(), link[i*2].get('ng-href').split('?trkid=')[0])
        except:
            print(tipe, nama[i].text_content(), harga[i].text_content()+' (0)', link[i*2].get('ng-href').split('?trkid=')[0])
    if (page <1):
        collectData(tipe, url, page+1)

# collectData(0,baseUrl+categoriesWanita[0]+sorting,page)

if __name__ == '__main__':
    mulai = time.time()
    #multiprocessing.freeze_support()
    processes = [ ]
    for kode,nama in categoriesWanita.items():
        print('process '+kode)
        t = multiprocessing.Process(target=collectData, args=(kode,baseUrl+nama+sorting,page))
        processes.append(t)
        t.start()

    for one_process in processes:
        one_process.join()

    print('')
    print('elapsed time'+str(time.time()-mulai))