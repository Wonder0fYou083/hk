from collections.abc import Sequence
import pandas as pd

def _close_level(columns: pd.MultiIndex) -> int:
    for level in reversed(range(columns.nlevels)):
        if "Close" in columns.get_level_values(level):
            return level
    raise KeyError("data must include a 'Close' price level")


def get_close_prices(
    data: pd.DataFrame,
    tickers: Sequence[str] | None = None,
) -> pd.DataFrame:
    if isinstance(data.columns, pd.MultiIndex):
        closes = data.xs("Close", axis=1, level=_close_level(data.columns))
        closes.columns.name = None
        if tickers is not None:
            ordered_tickers = list(tickers)
            missing = [
                ticker for ticker in ordered_tickers if ticker not in closes.columns
            ]
            if missing:
                raise KeyError(f"missing close prices for tickers: {missing}")
            closes = closes.loc[:, ordered_tickers]
        return closes.dropna(how="all")

    if "Close" not in data.columns:
        raise KeyError("data must include a 'Close' column")

    closes = data.loc[:, ["Close"]].copy()
    if tickers is not None:
        ordered_tickers = list(tickers)
        if len(ordered_tickers) != 1:
            raise ValueError("single-ticker data can only be labeled with one ticker")
        closes.columns = ordered_tickers
    return closes.dropna(how="all")


def compute_daily_returns(close_prices: pd.DataFrame) -> pd.DataFrame:
    return close_prices.pct_change(fill_method=None)
