import requests
from json.decoder import JSONDecodeError  # 正確的錯誤類型

def download_youbike_data()->list:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

    try:
        response = requests.get(url)
        response.raise_for_status()
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as jsonError:
            raise Exception(f"發生轉換格式錯誤:jsonError")
    except requests.exceptions.HTTPError as err_http:
        raise Exception(f"發生 HTTP 錯誤: {err_http}")
    except requests.exceptions.ConnectionError as err_conn:
        raise Exception(f"發生連線錯誤 (例如 DNS 查詢失敗、連線被拒): {err_conn}")
    except requests.exceptions.Timeout as err_timeout:
        raise Exception(f"請求超時: {err_timeout}")
    except requests.exceptions.RequestException as err:
        # 這是所有 requests 例外的父類別，可以用來捕捉其他未預期的錯誤
        raise Exception(f"發生未預期的請求錯誤: {err}")
    else:
        return data
def main():
    ##希望在main這裡顯示錯誤
   try:
    data = download_youbike_data()
    print(data)
   except Exception as e:
       print("發生錯誤\n{e}")

if __name__ == "__main__":
    main()
# def download_youbike_data()->list:
#     url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         try:
#             data = response.json()
#         except JSONDecodeError as json_err:
#             print(f"發生轉換格式錯誤: {json_err}")
#         else:
#             print("沒有出錯 (內層):\n", data[:3])  # 看前三筆
#     except requests.exceptions.HTTPError as err_http:
#         print(f"發生 HTTP 錯誤: {err_http}")
#     except requests.exceptions.ConnectionError as err_conn:
#         print(f"發生連線錯誤 (例如 DNS 查詢失敗、連線被拒): {err_conn}")
#     except requests.exceptions.Timeout as err_timeout:
#         print(f"請求超時: {err_timeout}")
#     except requests.exceptions.RequestException as err:
#         print(f"發生未預期的請求錯誤: {err}")
#     else:  # 這個 else 是外層 try 沒有錯誤時才執行
#         return data
# def main():
#    data = download_youbike_data()
#    print(data)

# if __name__ == "__main__":
#     main()

    ###############################
# import requests

# url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

# response = requests.get(url)
# #print(type(response)) #查看資料型


# if response.status_code == 200:
#     print("下載成功")
#     print("下載的內容如下")
#     #print(response.text)
#     #print(type(response.json()))
#     for item in response.json():
#         print(item)
# else:
#     print("下載失敗")
    