import yfinance as yf
import pandas as pd
from pathlib import Path

def download_prices(tickers, start="2018-01-01", end=None, 
                    save_path="data/raw/prices.parquet"):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True, 
                       group_by="ticker", progress=False)
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    data.to_parquet(save_path)
    return data
