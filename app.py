import streamlit as st
import math

# 品牌退稅比例設定
brand_tax = {
    "CHANEL": 0.94,
    "Louisvuitton": 0.94,
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

st.set_page_config(page_title="批發報價系統", layout="centered")
st.title("📦 批發報價系統")

brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
euro_price = st.number_input("輸入商品歐元原價", min_value=0, value=0, step=10)

if st.button("計算報價"):
    tax_rate = brand_tax[brand]
    price_after_tax = euro_price * tax_rate

    # 運費邏輯
    if euro_price < 800:
        shipping = 15
    elif euro_price <= 1500:
        shipping = 20
    else:
        shipping = 25

    # 利潤邏輯
    if euro_price < 600:
    profit = 1000
elif euro_price < 800:
    profit = 2000
elif euro_price < 1000:
    profit = 2500
elif euro_price <= 1500:
    profit = 3000
else:
    profit = 3000

    total_euro = price_after_tax + shipping
    rate = 36.5  # 匯率您可自行變更此值
    tw_cost = total_euro * rate
    final_price = math.ceil((tw_cost + profit) / 100) * 100

    st.subheader("報價結果")
    st.success(f"{brand} 報價：NT$ {final_price:,}")
