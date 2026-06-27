from src.data_loader import download_prices

TICKERS = [
    "0700.HK", "9988.HK", "3690.HK", "1299.HK", "0388.HK",
    "0005.HK", "0939.HK", "1810.HK", "2318.HK", "9618.HK"
]

data = download_prices(TICKERS)
print(data.tail())