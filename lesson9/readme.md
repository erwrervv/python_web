- 簡介  
    - 這三個指標常用於迴歸模型的效能評估，用以衡量預測值 ŷ 和實際值 y 之間的差距與解釋能力。

- 定義與公式  
    - MSE（Mean Squared Error，均方誤差）  
        - 公式：MSE = (1/n) * Σ (y_i - ŷ_i)²  
        - 說明：平均每筆預測的平方誤差。值越小越好。單位為 y 的平方。  
    - RMSE（Root Mean Squared Error，均方根誤差）  
        - 公式：RMSE = sqrt(MSE)  
        - 說明：MSE 的平方根，與目標變數 y 同單位，直觀上更好解讀。值越小越好。  
    - R²（Coefficient of Determination，決定係數）  
        - 公式：R² = 1 - (SS_res / SS_tot)，其中 SS_res = Σ (y_i - ŷ_i)²，SS_tot = Σ (y_i - ȳ)²  
        - 說明：表示模型解釋的變異比例。範圍通常在 (-∞, 1]，越接近 1 表示模型解釋力越好；若為負值，表示模型表現還不如只預測平均值 ȳ。

- 解讀重點  
    - MSE vs RMSE：MSE 對大誤差（outliers）懲罰更強（平方），RMSE 保持同量綱，適合直接比較目標變數尺度。  
    - R² 提供解釋變異的比例，但對樣本數與模型複雜度不敏感（可搭配調整後的 R² 使用）。  
    - 不能單靠一個指標判斷好壞：通常同時看 R²（解釋力）與 RMSE（實際誤差量級）。

- 使用情境建議  
    - 若關心「誤差的實際量級」，使用 RMSE（或 MAE）更直觀。  
    - 若想知道模型能解釋多少變異，用 R²。  
    - 比較不同模型時，用同一資料集計算 RMSE 與 R²；若資料尺度不同，需標準化或使用相對誤差指標。

- 範例（Python，使用 numpy）  
    - 程式片段：
        - import numpy as np
        - y = np.array([...])
        - y_pred = np.array([...])
        - mse = np.mean((y - y_pred)**2)
        - rmse = np.sqrt(mse)
        - r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)

- 小提醒  
    - RMSE 與 MSE 受極端值影響大；如需穩健評估，可考慮 MAE（Mean Absolute Error）或使用中位數相關指標。  
    - R² 在非線性或變異非均勻的情況下可能誤導，需要搭配殘差分析檢視模型假設是否成立。

簡潔結論：MSE/ RMSE 衡量誤差量級，RMSE 與目標同單位最直觀；R² 衡量模型解釋變異比例，三者合用可提供完整的迴歸模型評估視角。
