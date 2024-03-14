import requests
import json
import pandas as pd
url='https://online.senao.com.tw/FrontAPI/StoreV2/rawAllTypes'

response=requests.get(url)
json_response = json.loads(response.text)

name_list=[]
add_list=[]
tel_list=[]
try:
    for store_type in json_response['data']['stores']:
        for store_data in store_type['data']:
            for store_data2 in store_data['data']:
                store_name=store_data2['storeName']
                store_address=store_data['name']+store_data2['address']
                store_tel=store_data2['storeTEL']
                name_list.append(store_name)
                add_list.append(store_address)
                tel_list.append(store_tel)

    df=pd.DataFrame()
    df['特約店名稱']=name_list
    df['特約店地址']=add_list
    df['特約店電話']=tel_list
    print('轉檔成功 !')
    df.to_csv(r'C:\Python\ 神腦特約 & 服務中心資料.csv', index=False,encoding='utf_8_sig')
except Exception as e:
    print('轉檔失敗:', e)