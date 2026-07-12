from src.data_loader import download_prices
from src.features import compute_daily_returns, get_close_prices
from src.plot import *


TICKERS = [
    "0700.HK",  # Tencent
    "1398.HK",  # ICBC
    "1288.HK",  # Agricultural Bank of China
    "0939.HK",  # China Construction Bank
    "3988.HK",  # Bank of China
    "0857.HK",  # PetroChina
    "0941.HK",  # China Mobile
    "2628.HK",  # China Life Insurance
    "0883.HK",  # CNOOC
    "1088.HK",  # China Shenhua Energy
] 

TICKERS_TO_LOOK_INTO = ["0939.HK", "1398.HK"]


def main() -> None:
    data = download_prices(TICKERS, start="2026-01-01", end="2026-07-01")
    close_prices = get_close_prices(data)
    daily_returns = compute_daily_returns(close_prices)
    print("Close prices:")
    print(close_prices.tail())
    print("\nDaily returns:")
    print(daily_returns.tail())
    plot_normalized_prices(close_prices, TICKERS_TO_LOOK_INTO)
    plot_cumulative_returns(daily_returns, TICKERS_TO_LOOK_INTO)

if __name__ == "__main__":
    main()
