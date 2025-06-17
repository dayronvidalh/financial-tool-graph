
import pandas as pd
import random

def generate_projections(tickers):
    sentiments = [round(random.uniform(-0.5, 0.9), 2) for _ in tickers]
    outlook = ['Bearish' if s < -0.1 else 'Neutral' if s < 0.2 else 'Bullish' for s in sentiments]
    return pd.DataFrame({
        'Ticker': tickers,
        'Sentiment Score': sentiments,
        'Projection': outlook
    })

def get_top_20_gainers_with_projections():
    tickers = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'AMZN', 'TSLA', 'META', 'NFLX', 'AMD', 'CRM',
               'INTC', 'BA', 'DIS', 'ABNB', 'SQ', 'COIN', 'SHOP', 'PLTR', 'PYPL', 'ROKU']
    return generate_projections(tickers)

def get_new_hot_stocks_with_projections():
    tickers = ['UBER', 'LYFT', 'DOCU', 'BIDU', 'NIO', 'MRNA', 'FUBO', 'BMBL', 'RIOT', 'DKNG']
    return generate_projections(tickers)
