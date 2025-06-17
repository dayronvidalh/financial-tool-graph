
import streamlit as st
import matplotlib.pyplot as plt
from backtest import run_backtest
from alerts import send_email_alert
from projections import get_top_20_gainers_with_projections, get_new_hot_stocks_with_projections

st.set_page_config(page_title="Financial Sentiment Dashboard", layout="wide")
st.title("📊 Financial Sentiment Dashboard")

auto_trade = st.checkbox("Enable Auto Trade Execution", value=False)

# Section 1: Top 20 Gainers
st.subheader("🏆 Top 20 Gainers with News-Based Projections")
gainers = get_top_20_gainers_with_projections()

fig1, ax1 = plt.subplots()
colors = gainers['Projection'].map({'Bullish': 'green', 'Neutral': 'orange', 'Bearish': 'red'})
ax1.bar(gainers['Ticker'], gainers['Sentiment Score'], color=colors)
ax1.set_title("Top 20 Gainers Sentiment")
ax1.set_ylabel("Sentiment Score")
ax1.set_xticklabels(gainers['Ticker'], rotation=45, ha='right')
st.pyplot(fig1)
st.dataframe(gainers)

# Section 2: Hot Stocks
st.subheader("🔥 New Hot Stocks (Outside Top 20)")
hot_stocks = get_new_hot_stocks_with_projections()

fig2, ax2 = plt.subplots()
colors2 = hot_stocks['Projection'].map({'Bullish': 'green', 'Neutral': 'orange', 'Bearish': 'red'})
ax2.bar(hot_stocks['Ticker'], hot_stocks['Sentiment Score'], color=colors2)
ax2.set_title("Hot Stocks Sentiment")
ax2.set_ylabel("Sentiment Score")
ax2.set_xticklabels(hot_stocks['Ticker'], rotation=45, ha='right')
st.pyplot(fig2)
st.dataframe(hot_stocks)

# Strategy logic
if st.button("Run Strategy"):
    results = run_backtest(auto=auto_trade)
    st.write(results)
    if results['signal'] == 'buy':
        send_email_alert("Buy signal triggered.")
    elif results['signal'] == 'sell':
        send_email_alert("Sell signal triggered.")
