import requests
from bs4 import BeautifulSoup
import pandas as pd

# 建立英文縣市名稱和中文縣市名稱的映射字典
county_mapping = {
    'taipei-city': '台北市',
    'keelung-city':'基隆市',
    'new-taipei-city': '新北市',
    'taoyuan-city': '桃園市',
    'hsinchu-county':'新竹縣',
    'xinzhu-city':'新竹市',
    'miaoli-county':'苗栗縣',
    'taichung-city':'台中市',
    'changhua-county':'彰化縣',
    'nantou-county':'南投縣',
    'yunlin-county':'雲林縣',
    'chiayi-county':'嘉義縣',
    'chiayi-city':'嘉義市',
    'tainan-city':'台南市',
    'kaohsiung-city':'高雄市',
    'pingtung-county':'屏東縣',
    'yilan-county':'宜蘭縣',
    'hualien-county':'花蓮縣',
    'taitung-county':'台東縣',
    'lienchiang-county':'連江縣',
    'kinmen-county':'金門縣',
    'penghu-county':'澎湖縣'
}

counties=['taipei-city','keelung-city',
          'new-taipei-city','taoyuan-city'
          ,'hsinchu-county','xinzhu-city',
           'miaoli-county','taichung-city',
           'changhua-county','nantou-county',
           'yunlin-county','chiayi-county',
           'chiayi-city','tainan-city','kaohsiung-city',
           'pingtung-county','yilan-county','hualien-county','taitung-county',
            'lienchiang-county','kinmen-county','penghu-county'
           ]

try:
    county_list=[]
    title_list=[]
    name_list=[]
    address_list=[]
    tel_list=[]
    for county in counties:
        url='https://www.century21.com.tw/store/'+county
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        div_list=soup.find_all('div','locationbox')
        for i in div_list:
            store_title=i.find('a',class_='locationbox__title').text
            store_name=i.find('div',class_='locationbox__name').text
            store_tel=i.find('a',class_='locationbox__tel').text
            store_address=i.find('a',class_='locationbox__addr').text
            # 將英文名稱轉為中為名稱
            chinese_county = county_mapping.get(county, county)
            # 將各數據放入空的 list 内以利之後建立 DataFrame
            county_list.append(chinese_county)
            title_list.append(store_title)
            name_list.append(store_name)
            address_list.append(store_address)
            tel_list.append(store_tel)
    print(len(title_list))
    print(len(name_list))
    print(len(address_list))
    print(len(tel_list))
    df=pd.DataFrame()
    df['店鋪所在縣市']=county_list
    df['店鋪名稱']=title_list
    df['店鋪詳細名稱']=name_list
    df['店鋪地址']=address_list
    df['店鋪電話']=tel_list
    df.to_csv(r'C:\Python\ 21世紀店鋪資料.csv', index=False,encoding='utf_8_sig')
    print('轉檔成功 !')
except Exception as e:
    print('轉檔失敗:', e)
