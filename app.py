import streamlit as st
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
    "其他": 0.87
}

st.set_page_config(page_title="批客報價系統", page_icon="📦")

st.title("📦 批客報價系統")

brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
eur_price = st.number_input("輸入商品歐元原價", min_value=0.0, step=1.0)
rate = st.number_input("輸入匯率（即期賣出 +0.5）", value=35.0, step=0.1)

if st.button("計算報價"):
    tax_rate = brand_tax[brand]
    net_price = eur_price * tax_rate

    # 運費邏輯
    shipping = 10 if eur_price < 3000 else 20

    # 利潤邏輯
    profit = 1000 if eur_price < 3000 else 3000

    # 計算最終報價（無條件進位）
    total = math.ceil(net_price * rate + shipping * rate + profit)

    st.subheader("報價結果")
    st.success(f"{brand} 報價：NT$ {total:,}")
