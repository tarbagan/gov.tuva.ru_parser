import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def url_base():
    """url generation"""
    page = 386 #pagination page
    url_all = []
    for i in range(1,page):
        url = "http://gov.tuva.ru/press_center/news/?PAGEN_1=%s" % i
        url_all.append(url)
    return url_all
    
def parser():
    """multiprocessing perser function """
    pool = ThreadPool(5) #multiprocessing stream
    try:
        r = pool.map(requests.get, url_base())
    except:
        print ("Ошибка")
    for i in r:
        tag = bs(i.text, 'lxml').findAll("div", {"class": "news-name"})
        for lnk in tag:
            news = str(lnk)
            title = (re.findall(r'<b>(.*?)</b>', news)[0])
            link = "http://gov.tuva.ru"+(re.findall(r'<a href="(.*?)"><b>', news)[0])
            print (title)
            print (link)
parser()
