import streamlit as st
import requests
from bs4 import BeautifulSoup
import math

# 品牌退稅比例設定
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
    "其他": 1.0
}

# 自動取得台灣銀行歐元匯率 +0.5
def get_eur_rate():
    try:
        url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        eur_row = soup.find("td", text="歐元 (EUR)").find_parent("tr")
        eur_sell = float(eur_row.find_all("td")[2].text.strip())
        return round(eur_sell + 0.5, 2)
    except:
        return 36.0  # 預設匯率

st.set_page_config(page_title="批客報價系統", layout="centered")
st.title("📦 批客報價系統")

brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
euro_price = st.number_input("輸入商品歐元原價", min_value=0.0, step=10.0)

if st.button("計算報價"):
    tax = brand_tax[brand]
    net_price = euro_price * tax
    shipping = 10 if euro_price < 3000 else 20
    total_eur = net_price + shipping
    rate = get_eur_rate()
    cost_ntd = total_eur * rate
    profit = 1000 if euro_price < 3000 else 3000
    final_ntd = math.ceil(cost_ntd + profit)

    st.subheader("報價結果")
    st.success(f"{brand} 報價：NT$ {final_ntd:,}")
