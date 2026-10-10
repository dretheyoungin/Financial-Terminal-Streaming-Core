import unittest
import json
from crypto_ticker_engine import EnterpriseFinTechTicker

class TestFinTechTickerArchitecture(unittest.TestCase):
    def setUp(self):
        """Executed automatically before each test case to mount the trading engine node."""
        self.ticker = EnterpriseFinTechTicker()

    def test_volatility_interception_matrix(self):
        """CRITICAL RISK TEST: Verifies that extreme market drops (like ETH crashing) are intercepted."""
        # Simulated payload with high-volatility drop (ETH dropping from $3400 to $3190)
        high_volatility_feed = [
        '{"AssetSymbol": "ETH", "OpeningPrice": 3400.00, "CurrentPrice": 3190.00}'
        ]

        # Execute ticker parsing array
        self.ticker.calculate_price_volatility_delta(high_volatility_feed)

        # Read file onto disk to confirm the volatile record was dropped from safe ledger streams
        with open("market_ticker_ledger.json", "r") as f:
            ledger_data = json.load(f)

        # Assertions: Prove the record list remained empty because the spike was blocked/isolated
        self.assertEqual(len(ledger_data), 0)
        print("\n📈 TEST PASSED: Algorithmic Volatility Compliance Intercept Is Fully Functional.")

    def test_stable_ticker_routing(self):
        """DATA QUALITY TEST: Verifies that normal, stable price data routes safely into the ledger."""
        stable_feed = [
        '{"AssetSymbol": "BTC", "OpeningPrice": 62000.00, "CurrentPrice": 62150.00}'
        ]

        self.ticker.calculate_price_volatility_delta(stable_feed)

        with open("market_ticker_ledger.json", "r") as f:
            ledger_data = json.load(f)

        # Assertions: Prove that exactly 1 verified record made it safely through the pipeline
        self.assertEqual(len(ledger_data), 1)
        self.assertEqual(ledger_data[0]["Asset_Ticker"], "BTC")
        print("✅ TEST PASSED: Stable Asset Transaction Route successfully synchronized to disk.")

if __name__ == "__main__":
    unittest.main()