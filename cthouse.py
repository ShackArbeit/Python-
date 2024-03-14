import requests
from bs4 import BeautifulSoup
import pandas as pd 

url='https://www.cthouse.com.tw/about/franchise/%e8%87%ba%e5%8c%97%e5%b8%82-city/'

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')


title_list=[]
address_list=[]
tel_list=[]

div_list=soup.find_all('div','n franchise_object_mode')
try:
    for i in div_list:
        store_title=i.find('h5',class_='h5').text
        store_address=i.find('div','addr').text
        store_tel=i.find('span',class_='tel').text
        # 將店名、地址、電話分別放入空的 list 中
        title_list.append(store_title)
        address_list.append(store_address)
        tel_list.append(store_tel)
    print(address_list)
    df=pd.DataFrame()
    df['店鋪名稱']=title_list
    df['店鋪地址']=address_list
    df['店鋪電話']=tel_list
    df.to_csv(r'C:\Python\ 中信房屋店鋪資料.csv', index=False,encoding='utf_8_sig')
    print('轉檔成功 !')
except Exception as e:
    print('轉檔失敗:', e)