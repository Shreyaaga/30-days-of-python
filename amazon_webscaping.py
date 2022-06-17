from email import header
import requests
from bs4 import BeautifulSoup

#getting content from url 
url='https://www.flipkart.com/libra-bluetech-dancing-cactus-toy-talking-repeat-singing-sunny-kactus-120-songs/p/itmb82c44bc1402a?pid=MTYG7XG9AF2EWKSJ&lid=LSTMTYG7XG9AF2EWKSJM7IY4V&marketplace=FLIPKART&store=tng%2Fdcr&srno=b_1_3&otracker=hp_omu_Top%2BOffers_1_4.dealCard.OMU_JDQF5NV3L0C6_4&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_1_NA_view-all_4&fm=neo%2Fmerchandising&iid=882d86af-ade7-4062-8e15-b94151948c9b.MTYG7XG9AF2EWKSJ.SEARCH&ppt=hp&ppn=homepage&ssid=pbs55adhhc0000001655394734039'
headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
pagex=requests.get(url,headers=headers)
page=pagex.content

 #parsing
soup=BeautifulSoup(page,'html.parser')
print(soup.prettify)
#extracting useful information from the soup
title=soup.find(class_="B_NuCI").get_text()
print(title)
price=soup.find(class_='_30jeq3 _16Jk6d').get_text()
convertedprice=float(price[0:4])
print(convertedprice)
if price<500:
    send_mail()

def semd_mail():
    print("hry")
    