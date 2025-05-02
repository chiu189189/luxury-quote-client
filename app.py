
import streamlit as st

# 品牌退稅比例設定
brand_tax = {
    "CHANEL": 0.93,
    "LV": 0.94,
    "HERMES": 0.93,
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

st.set_page_config(page_title="批客報價系統", layout="centered")
st.title("📦 批客報價系統")

brand = st.selectbox("選擇品牌", list(brand_tax.keys()))
euro_price = st.number_input("輸入商品歐元原價", min_value=0.0, value=0.0, step=10.0)

if st.button("計算報價"):
    tax_rate = brand_tax[brand]
    price_after_tax = euro_price * tax_rate
    shipping = 10 if euro_price < 3000 else 20
    total_euro = price_after_tax + shipping
    rate = 35.0  # 匯率固定（不顯示）
    tw_cost = total_euro * rate
    profit = 1000 if euro_price < 3000 else 3000
    final_price = int(tw_cost + profit)

    st.subheader("報價結果")
    st.success(f"{brand} 報價：NT$ {final_price:,}")
    st.text_area("可複製報價內容", f"{brand} 報價：NT$ {final_price:,}", height=100)
