from lxml import html
from selenium import webdriver

baseUrl = "https://www.tokopedia.com/p/"
page = 1
categoriesWanita = ['fashion-wanita/atasan','fashion-wanita/celana','fashion-wanita/rok','fashion-wanita/dress','fashion-wanita/outwear','fashion-wanita/setelan','fashion-wanita/batik-warna','fashion-wanita/pakaian-dalam-wanita','fashion-wanita/tas','fashion-wanita/sepatu','fashion-wanita/jam-tangan','fashion-wanita/perhiasan','fashion-wanita/aksesoris','fashion-wanita/aksesoris-rambut','fashion-wanita/perlengkapan-couple','fashion-wanita/baju-tidur','fashion-wanita/perlengkapan-jahit']
sorting = '?ob=8'

def collectData(url, page):
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
    jumlah = 0
    for i in range(0, len(nama)):
        try:
            print(nama[i].text_content(), review[i].text_content())
        except:
            print(nama[i].text_content()+' (0)')
    if (page <=20):
        collectData(url, page+1)

for item in categoriesWanita:
    collectData(baseUrl+item+sorting, page)