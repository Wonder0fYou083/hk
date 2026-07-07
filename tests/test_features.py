import unittest

import pandas as pd

from src.features import compute_daily_returns, get_close_prices


class FeatureTests(unittest.TestCase):
    def test_get_close_prices_extracts_multiindex_in_ticker_order(self):
        columns = pd.MultiIndex.from_product(
            [["9988.HK", "0700.HK"], ["Open", "Close"]],
            names=["Ticker", "Price"],
        )
        data = pd.DataFrame(
            [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]],
            columns=columns,
        )

        closes = get_close_prices(data, ["0700.HK", "9988.HK"])

        expected = pd.DataFrame(
            {"0700.HK": [4.0, 8.0], "9988.HK": [2.0, 6.0]}
        )
        pd.testing.assert_frame_equal(closes, expected)

    def test_get_close_prices_handles_single_ticker_download_shape(self):
        data = pd.DataFrame({"Open": [1.0, 2.0], "Close": [3.0, 4.0]})

        closes = get_close_prices(data, ["0700.HK"])

        expected = pd.DataFrame({"0700.HK": [3.0, 4.0]})
        pd.testing.assert_frame_equal(closes, expected)

    def test_compute_daily_returns_does_not_fill_missing_prices(self):
        close_prices = pd.DataFrame({"0700.HK": [100.0, None, 110.0]})

        returns = compute_daily_returns(close_prices)

        self.assertTrue(pd.isna(returns.loc[0, "0700.HK"]))
        self.assertTrue(pd.isna(returns.loc[1, "0700.HK"]))
        self.assertTrue(pd.isna(returns.loc[2, "0700.HK"]))


if __name__ == "__main__":
    unittest.main()
