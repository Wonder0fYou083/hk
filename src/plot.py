from collections.abc import Sequence
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

def plot_returns(daily_returns : pd.DataFrame,
                 tickers : Sequence[str] | str) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    cleaned_daily_returns = daily_returns[tickers].dropna(how="any")
    ax = cleaned_daily_returns[tickers].plot(figsize=(12, 6), title="Returns", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")
    ax.axhline()
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.tight_layout()
    plt.show()

def plot_cumulative_returns(daily_returns : pd.DataFrame,
                            tickers : Sequence[str] | str) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    cleaned_daily_returns = daily_returns[tickers].dropna(how="any")
    cum_returns = (1 + cleaned_daily_returns).cumprod() - 1
    ax = cum_returns[tickers].plot(figsize=(12, 6), title="Returns", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")
    ax.axhline()
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.tight_layout()
    plt.show()

def plot_normalized_prices(closes : pd.DataFrame,
                           tickers : Sequence[str] | str | None = None) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    normalized = closes / closes.iloc[0]
    cleaned_normalized = normalized[tickers].dropna(how="any")
    ax = cleaned_normalized.plot(figsize=(12, 6), title="Normalized Prices", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Prices")
    ax.yaxis.set_major_formatter("${x:,.2f}")
    plt.tight_layout()
    plt.show()