from collections.abc import Sequence
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

def plot_daily_returns(daily_returns: pd.DataFrame,
                 tickers: Sequence[str] | str) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    ax = daily_returns[tickers].plot(figsize=(12, 6), title="Returns", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")
    ax.axhline(0)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.tight_layout()
    plt.show()

def plot_cumulative_returns(cumulative_returns : pd.DataFrame,
                            tickers : Sequence[str] | str) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    ax = cumulative_returns[tickers].plot(
        figsize=(12, 6), title="Cumulative Returns", linewidth=1
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")
    ax.axhline(0)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.tight_layout()
    plt.show()

def plot_normalized_prices(normalized_prices: pd.DataFrame,
                           tickers : Sequence[str] | str | None = None) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    ax = normalized_prices[tickers].plot(
        figsize=(12, 6), title="Normalized Prices", linewidth=1
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized Price")
    ax.yaxis.set_major_formatter("{x:,.2f}")
    plt.tight_layout()
    plt.show()

def plot_z_scores(z_scores: pd.DataFrame) -> None:
    ax = z_scores.plot(figsize=(12, 6), title="Z-Score", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("z-score")
    ax.axhline(0)
    ax.yaxis.set_major_formatter("{x:,.2f}")
    plt.tight_layout()
    plt.show()
