## Lesson 9: Flask 專案說明

這個資料夾包含一個示範用的 Flask 應用，示範如何在教學中使用 Flask 搭配靜態檔案（CSS/JS/圖片）與簡單的 API（例如線性回歸示例）。以下為更新後的專案結構與執行說明。

### 建議專案結構

```
lesson9/
├── app.py                  # Flask 應用程式主檔案（包含 route 與 API 範例）
├── requirements.txt       # 建議放置專案依賴（例如 flask, scikit-learn 等）
├── static/                # 靜態資源
│   ├── css/
│   ├── js/
│   ├── img/
│   └── vendor/            # 第三方套件前端檔（例如 Chart.js）
└── templates/             # HTML 樣板（Jinja2）
	├── index.html
	└── test.html
```

### 開發環境與安裝（建議）

1. 建議使用虛擬環境（venv / virtualenv / uv 皆可）。以下示範使用 venv：

   Powershell (Windows)

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

   macOS / Linux

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. 建議在 `requirements.txt` 中列出至少：

   - flask
   - scikit-learn
   - numpy

   範例 `requirements.txt` 可放在 `lesson9/requirements.txt`：

   ```text
   flask>=3.0
   scikit-learn
   numpy
   ```

### 啟動應用（開發）

在啟動前確認已啟用虛擬環境並安裝依賴。

Powershell 範例：

```powershell
cd .\lesson9
python app.py
# 或使用 uv: uv run python app.py
```

啟動後預設會監聽在 http://127.0.0.1:5000（若 `app.run(debug=True)` 未改變）。

### 常見注意事項

- 靜態文件請放在 `static/`，樣板放 `templates/`。
- 若需要中文 JSON 回應，確保在 `Flask` 應用中設定：

  ```python
  app.config['JSON_AS_ASCII'] = False
  # 新版 Flask 可能不需要 JSON_UTF8，但若有可設定
  try:
    app.config['JSON_UTF8'] = True
  except Exception:
    pass
  ```

- 若專案需在教學機器上執行，請在 `requirements.txt` 鎖定較穩定的版本號，並提供簡短的啟動說明。

### 建議的後續改進

- 新增 `run.ps1`（或 Makefile）來對 Windows/macOS 提供一鍵啟動腳本。
- 把 Chart.js、CSS 等放到 `static/vendor` 或使用 CDN；若使用 CDN，請在 `templates` 中註明來源。
- 若希望範例可在無網路環境運作，請把必要的前端檔案放入 `static/vendor`。

如果你有偏好的執行工具（例如 `uv`），我可以把文件改為使用 `uv` 的說明，或是直接建立 `requirements.txt` 與一個簡單的 `run.ps1` 啟動腳本。告訴我你要我做哪一件事，我就進行下一步。
