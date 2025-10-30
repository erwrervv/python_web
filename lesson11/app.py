
from flask import Flask,render_template
from knn.app import knn_bp
from regression.app import regression_bp
app = Flask(__name__)
app.register_blueprint(knn_bp)
app.register_blueprint(regression_bp)
# 讓app輸出json時,繁體中文不會出現亂碼
# 必須放在 jsonify 之前設定
app.config['JSON_AS_ASCII'] = False
# 讓app輸出json時,繁體中文不會出現亂碼,支援新的flask版本
app.config['JSON_SORT_KEYS'] = False  # 可選，防止自動排序 key
@app.route("/")
def index():
    return render_template("index.html")
def main():
    """啟動應用（教學用：啟用 debug 模式）"""
    # 在開發環境下使用 debug=True，部署時請關閉
    app.run(debug=True)

if __name__ == "__main__":
    main()