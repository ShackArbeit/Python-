
import requests

url='https://www.u-trust.com.tw/CG2/CG02.asp'
response=requests.get(url,verify=False)
print(response.text)
