from collections.abc import Sequence
import pandas as pd

def clean_pair_prices(prices: pd.DataFrame,
                      tickers: Sequence[str]) -> pd.DataFrame:
    if len(tickers) != 2:
        raise ValueError("Not a pair")
    return prices.loc[:, list(tickers)].dropna(how="any")

def compute_ratios(normalized_prices: pd.DataFrame, 
                   tickers: Sequence[str]) -> pd.Series:
    if len(tickers) != 2:
        raise ValueError("Not a pair")
    pair_prices = normalized_prices[tickers]
    ratios = pair_prices.iloc[:, 0] / pair_prices.iloc[:, 1]
    return ratios

def compute_rolling_means(df: pd.DataFrame, window: int) -> pd.DataFrame:
    rolling_means = df.rolling(window=window).mean()
    return rolling_means

def compute_rolling_std(df: pd.DataFrame, window: int) -> pd.DataFrame:
    rolling_std = df.rolling(window=window).std()
    return rolling_std

def compute_z_score(df: pd.DataFrame,
                    rolling_means: pd.DataFrame,
                    rolling_std: pd.DataFrame) -> pd.DataFrame:
    z_score = (df - rolling_means) / rolling_std
    return z_score
