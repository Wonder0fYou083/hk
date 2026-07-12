from collections.abc import Sequence
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

def plot_returns(daily_returns : pd.DataFrame,
                 tickers : Sequence[str] | str) -> None:
    if tickers is None:
        raise ValueError("No ticker selected")
    ax = daily_returns[tickers].plot(figsize=(12, 6), title="Returns", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")
    ax.axhline()
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.tight_layout()
    plt.show()

def plot_cumulative_returns(daily_returns : pd.DataFrame,
                            tickers : Sequence[str] | str) -> None:
    cum_returns = (1 + daily_returns).cumprod() - 1
    plot_returns(cum_returns, tickers)