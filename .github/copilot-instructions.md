# Copilot Instructions for `python_web`

## 專案架構總覽

- 本專案以 Python 為主，結構分為主程式 (`main.py`)、課程資料夾 (`lesson1`, `lesson2`, `lesson3`) 及相關說明文件。
- 課程資料夾內含 Jupyter Notebook (`.ipynb`)、Python 腳本 (`.py`)、Markdown 說明 (`.md`)。
- 主要教學內容聚焦於 Python 基礎語法、函數、類別、錯誤處理與實作練習。

## 關鍵開發流程

- **執行主程式**：直接執行 `main.py`，通常用於整合或展示課程成果。
- **互動式學習**：建議使用 Jupyter Notebook (`lesson*/lesson*_*.ipynb`) 進行互動式練習與教學。
- **課程內容參考**：`lesson2/AGENTS.md` 詳細說明 Python 函數設計、常見錯誤與練習題，適合 AI agent 產生教學或練習題目。

## 專案慣例與模式

- **函數設計**：強調明確的參數命名、預設值安全設計（避免可變物件作為預設參數），回傳值可為單一或多值 tuple。
- **錯誤處理**：常用 `try/except/else` 結構，並以 `Exception as e` 捕捉例外，回報錯誤訊息。
- **教學範例**：所有教學程式碼皆附有註解，並以簡單範例（如溫度轉換、成績計算）說明核心概念。
- **練習題**：每個課程結尾會附上練習題，鼓勵 AI agent 產生自動化測驗或解題。

## 重要檔案與目錄

- `main.py`：主程式入口。
- `lesson2/AGENTS.md`：Python 函數教學與練習題重點。
- `lesson*/lesson*_*.ipynb`：互動式教學與練習。
- `lesson3/tools.py`：可能包含輔助工具函數。
- `README.md`：專案簡介。

## 外部依賴與整合

- 目前未見明確第三方套件依賴，若 Notebook 需額外套件請於 cell 內明確安裝。
- 若需擴充，請遵循現有教學模式與註解風格。

## 典型 AI Agent 工作範例

- 產生教學型 Notebook，內容結構可參考 `lesson2/AGENTS.md`。
- 自動化產生練習題與解答，並附上註解。
- 依據現有錯誤處理模式，補充程式碼健壯性。
- 產生互動式教學內容時，優先使用 Notebook 格式。

---

如有不明確或未涵蓋的部分，請回報以便補充說明。
