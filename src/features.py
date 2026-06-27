import pandas as pd

def get_close_prices(data, tickers):
    closes = pd.DataFrame()
    for ticker in tickers:
        closes[ticker] = data[ticker]["Close"]
    return closes.dropna(how="all")

def compute_daily_returns(close_prices):
    return close_prices.pct_change()