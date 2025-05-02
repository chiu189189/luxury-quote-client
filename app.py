import streamlit as st
import requests
from bs4 import BeautifulSoup
import math

# 品牌退稅比例設定 (品牌: 退稅後價格比例)
brand_tax = {
    "CHANEL": 0.94,
    "LV": 0.94,
    "HERMES": 0.94,
    "DIOR": 0.87,
    "CELINE": 0.87,
    "GUCCI": 0.87,
    "YSL": 0.87,
    "LOEWE": 0.87,
    "BURBERRY": 0.87,
    "CHLOÉ": 0.87,
    "BALENCIAGA": 0.87,
    "其他": 0.90
}

# 應用程式標題
st.title("📦 批客報價系統")

# 輸入介面：品牌下拉選單與商品原價（歐元）
brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
price_eur = st.number_input("輸入商品歐元原價", value=0.00, format="%.2f")

# 按鈕觸發計算
if st.button("計算報價"):
    # 嘗試抓取臺灣銀行即期賣出匯率（歐元）
    exchange_rate = None
    try:
        url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        # 尋找幣別為 EUR 的表格列
        currency_cells = soup.find_all("td", {"data-table": "幣別"})
        for cell in currency_cells:
            # 幣別代號通常在該欄位最後一個 <div> 中
            divs = cell.find_all("div")
            if divs and divs[-1].get_text().strip() == "EUR":
                # 找到同一列中 data-table 為 即期匯率-本行賣出 的欄位
                row = cell.find_parent("tr")
                rate_cell = row.find("td", {"data-table": "即期匯率-本行賣出"})
                if rate_cell:
                    exchange_rate = float(rate_cell.get_text().strip())
                break
    except Exception as e:
        exchange_rate = None

    if exchange_rate is None:
        # 如果匯率取得失敗，提示錯誤訊息
        st.error("無法取得最新匯率，請稍後再試。")
    else:
        # 套用品牌退稅比例計算報價並無條件進位取整數
        final_rate = exchange_rate + 0.5  # 即期賣出匯率加 0.5
        price_twd = math.ceil(price_eur * brand_tax[brand] * final_rate)
        # 顯示報價結果
        st.subheader("報價結果")
        st.success(f"{brand} 報價：NT$ {price_twd:,}")
