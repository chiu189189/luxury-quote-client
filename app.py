import streamlit as st
import math

# 品牌退稅比例設定（依實際需求可擴充）
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

# 預設匯率（自行於 GitHub 修改此數值）
exchange_rate = 36.5

st.set_page_config(page_title="批客報價系統", layout="centered")
st.title("📦 批客報價系統")

# 使用者選品牌與輸入價格（整數）
brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
euro_price = st.number_input("輸入商品歐元原價", min_value=0, step=10, value=0, format="%d")

if st.button("計算報價"):
    tax_rate = brand_tax[brand]
    after_tax = euro_price * tax_rate
    shipping = 10 if euro_price < 3000 else 20
    total_eur = after_tax + shipping
    profit = 1000 if euro_price < 3000 else 3000
    final_twd = math.ceil(total_eur * exchange_rate + profit)

    st.subheader("報價結果")
    st.success(f"{brand} 報價：NT$ {final_twd:,}")
