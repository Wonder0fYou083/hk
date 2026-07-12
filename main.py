from src.data_loader import download_prices
from src.features import (
    compute_normalized_prices,
    get_close_prices,
)
from src.pair_features import *
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

PAIR = ["0939.HK", "1398.HK"]
WINDOW = 20

def main() -> None:
    data = download_prices(TICKERS, start="2026-01-01", end="2026-07-01")
    close_prices = get_close_prices(data)
    pair_prices = clean_pair_prices(close_prices, PAIR)
    normalized_pair_prices = compute_normalized_prices(pair_prices)
    ratios = compute_ratios(normalized_pair_prices, PAIR)
    rolling_means = compute_rolling_means(ratios, WINDOW)
    rolling_std = compute_rolling_std(ratios, WINDOW)
    z_score = compute_z_score(ratios, rolling_means, rolling_std)
    plot_z_scores(z_score)
    
if __name__ == "__main__":
    main()
