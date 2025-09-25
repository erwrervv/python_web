import requests

url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

response = requests.get(url)
#print(type(response))

if response.status_code == 200:
    print("下載成功")
else:
    print("下載失敗")
