from src.data_loader import download_prices
from src.features import compute_daily_returns, get_close_prices
from src.plot import *

TICKERS = [
    "0700.HK", "9988.HK", "3690.HK", "1299.HK", "0388.HK",
    "0005.HK", "0939.HK", "1810.HK", "2318.HK", "9618.HK"
]


def main() -> None:
    data = download_prices(TICKERS, start="2026-01-01", use_cache=True)
    close_prices = get_close_prices(data, TICKERS)
    daily_returns = compute_daily_returns(close_prices)

    print("Close prices:")
    print(close_prices.tail())
    print("\nDaily returns:")
    print(daily_returns.tail())
    plot_cumulative_returns(daily_returns, ["0700.HK", "9988.HK"])


if __name__ == "__main__":
    main()
