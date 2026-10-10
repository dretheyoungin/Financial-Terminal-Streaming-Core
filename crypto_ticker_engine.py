import time
import json
import uuid
import random
from datetime import datetime

class EnterpriseFinTechTicker:
    def __init__(self):
        # Generates a unique node cluster ledger key for tracking transaction records
        self.node_id = str(uuid.uuid4())
        self.market_sector = "Digital-Assets-V"
        print(f"💰 FINTECH ENGINE ONLINE: Core Trading Node Active [{self.node_id}]")
        print("📈 STREAM MODE: Real-Time Market Ticker Listening...")

    def calculate_price_volatility_delta(self, raw_stream_ticks: list) -> list:
        """
        FINANCIAL RISK ALGORITHMIC MATRIX:
        Parses live asset feeds, computes price movement percentages,
        and flags high-volatility trading spikes automatically for rapid execution.
        """
        print(f"\n⚡ INGESTING MARKET FEED: Evaluating {len(raw_stream_ticks)} Live Asset Packets...")
        processed_ledger = []

        for tick in raw_stream_ticks:
            try:
                data = json.loads(tick)
                asset = data.get("AssetSymbol")
                opening_price = data.get("OpeningPrice")
                current_price = data.get("CurrentPrice")

                # Math Analytics Layer: Calculate exact price change percentage
                price_delta = current_price - opening_price
                percentage_movement = (price_delta / opening_price) * 100

                # RISK COMPLIANCE INTERCEPT: Flag sharp volatility alerts (> 5.0% change)
                if abs(percentage_movement) >= 5.0:
                    print(f"🚨 VOLATILITY ALERT: Sharp Market Swing for {asset}! Movement: {percentage_movement:.2f}%... Dispatching to Order Desks.")
                    continue

                # Structure the data into a clean, normalized ledger node
                ledger_node = {
                    "Transaction_UUID": str(uuid.uuid4()),
                    "Asset_Ticker": asset,
                    "Market_Metrics": {
                        "Open_USD": opening_price,
                        "Current_USD": current_price,
                        "Delta_Percent": round(percentage_movement, 4)
                    },
                    "Processing_Cluster": self.node_id,
                    "Timestamp_UTC": datetime.utcnow().isoformat()
                }
                processed_ledger.append(ledger_node)
                print(f"✅ TICKER ROUTE SUCCESS: Verified {asset} at ${current_price:.2f} (Delta: {percentage_movement:.2f}%)")

            except Exception as e:
                print(f"❌ PIPELINE METRIC FAILURE: Could not parse feed data. Raw: {str(e)}")

        # Simulate an atomic write commit to a transaction log ledger database
        with open("market_ticker_ledger.json", "w") as f:
            json.dump(processed_ledger, f, indent=4)
        print("\n💾 TRANSACTION LEDGER WRITE SYNC COMPLETE: Local data storage flushed successfully.")

if __name__ == "__main__":
    ticker = EnterpriseFinTechTicker()

    # SIMULATED LIVE ECOSYSTEM MARKET TICKER FEED (Simulating high-frequency crypto trading burst)
    simulated_market_feed = [
        '{"AssetSymbol": "BTC", "OpeningPrice": 62000.00, "CurrentPrice": 62150.00}',
        '{"AssetSymbol": "ETH", "OpeningPrice": 3400.00, "CurrentPrice": 3190.00}',
        '{"AssetSymbol": "SOL", "OpeningPrice": 140.00, "CurrentPrice": 142.10}'
    ]

    # SENIOR PERFORMANCE BENCHMARKING TIME MATRIX
    start = time.perf_counter()
    ticker.calculate_price_volatility_delta(simulated_market_feed)
    end = time.perf_counter()

    print("\n======================================================================")
    print("📊 FINTECH INTEGRATION PERFORMANCE PROFILE")
    print(f"⏱️ TICKER TRANSACTION LATENCY: {(end - start) * 1000:.4f} ms")
    print("======================================================================")