import requests
import json
import pandas as pd

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Authorization':'bearer d_YlxwPw-Ox5LxVSFk5z5ZcQkCM'
}

county_list=[]
title_list=[]
address_list=[]
tel_list=[]

try:
    for i in range(0,29):
        url = f'https://api.watsons.com.tw/api/v2/wtctw/stores/watStores?currentPage={i}&pageSize=20&isCceOrCc=false&fields=FULL&lang=zh_TW&curr=TWD'
        response=requests.get(url,headers=headers)
        json_response=json.loads(response.text)

        for store_info in json_response['stores']:
            store_county=store_info['address']['displayAddress3']
            store_title = store_info['displayName']
            store_address = store_info['address']['displayAddress1']
             # 檢查 store_tel 是否為空值
            if 'phone' in store_info['address'] and store_info['address']['phone']:
                store_tel = store_info['address']['phone']
            else:
                store_tel = ''  # 如果是空值，設定為空字

            county_list.append(store_county)
            title_list.append(store_title)
            address_list.append(store_address)
            tel_list.append(store_tel)

    df=pd.DataFrame()
    df['店鋪所在縣市']=county_list
    df['店鋪名稱']=title_list
    df['店鋪地址']=address_list
    df['店鋪電話']=tel_list
    df.to_csv(r'C:\Python\ 屈臣氏店鋪資料.csv', index=False,encoding='utf_8_sig')
    print('轉檔成功 !')
except Exception as e:
    print('轉檔失敗:', e)