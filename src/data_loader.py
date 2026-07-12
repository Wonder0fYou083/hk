from collections.abc import Sequence
from pathlib import Path

import pandas as pd


DEFAULT_PRICE_PATH = Path("data/raw/prices.parquet")


def download_prices(
    tickers: Sequence[str] | str,
    start: str = "2018-01-01",
    end: str | None = None,
    save_path: str | Path | None = DEFAULT_PRICE_PATH,
) -> pd.DataFrame:
    path = Path(save_path) if save_path is not None else None

    import yfinance as yf

    data = yf.download(
        tickers,
        start=start,
        end=end,
        interval='1d',
        auto_adjust=True,
        group_by="ticker",
        progress=True,
        threads=True,
    )
    if data.empty:
        raise ValueError("no price data downloaded")

    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        data.to_parquet(path)
    return data
