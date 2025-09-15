# def main():
#     print("Hello from python-web!")


# if __name__ == "__main__":
#     main()

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():  # 處理根目錄請求的函式
#     return 'Hello, Flask!'

# if __name__ == '__main__':
#     app.run(debug=True)  # 啟動 Flask 伺服器
from flask import Flask

app = Flask(__name__)
@app.route("/")
## __name__代表是這個檔案的名稱main.py，並且賦值給app
##route後面必須宣告一個方法
##route代表只要進入根目錄就使用Flask與main.py檔案
def index():
    return '<h1 style="color:red">您好! Flaks!</h1>'
@app.route("/name")
def name():
    return '<h1>name頁面</h1>'
##return 服務器能編譯的內容，html
if __name__ == "__main__":
    app.run(debug=True)
## app.run(debug=True) 啟動app，並且使用debug模式