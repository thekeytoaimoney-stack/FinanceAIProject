import streamlit as st
import yfinance as yf

st.title("FinanceAI Dashboard")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

try:
    stock = yf.Ticker(ticker)

    info = stock.info

    st.subheader(info.get("longName", "Unknown Company"))

    st.write("Current Price:", info.get("currentPrice", "N/A"))

    st.write("Market Cap:", info.get("marketCap", "N/A"))

    hist = stock.history(period="1y")

    st.line_chart(hist["Close"])

except Exception as e:
    st.error(f"Error loading stock data: {e}")