import time
import unittest
from crypto_ticker_engine import CryptoTickerEngine
from macro_telemetry_harness import log_system_metrics, run_performance_benchmark

class MacroPerformanceStressSuite(unittest.TestCase):
    def setUp(self):
        """Initializes a specialized high-velocity tracking state for stress analysis."""
        self.engine = CryptoTickerEngine()
        self.start_time = time.perf_counter()

        # SRE Performance Metrics Counters
        self.success_count = 0
        self.quarantine_count = 0
        self.rate_limited_count = 0

    def test_high_density_macro_load_throughput(self):
        """Simulates an institutional high-frequency data burst to benchmark engine limits."""
        print("\n⚡ STARTING SENIOR MACRO LOAD TEST SIMULATION...")

        # 1. Generate a heavy, high-volume synthetic transactional data stream
        synthetic_stream = [
            {"account": f"InstitutionalClient_{i}", "price": 100.0 + i, "asset": "BTC"}
            for i in range(25)
        ]

        # 2. Inject an extreme market flash-crash outlier transaction
        synthetic_stream.append({"account": "WhaleAccount_X", "price": 99000.0, "asset": "BTC"})

        # 3. Process the high-velocity stream and route to our telemetry hooks
        for tick in synthetic_stream:
            tick_start = time.perf_counter()

            # Apply your engine's token bucket compliance
            if not self.engine.apply_token_bucket():
                self.rate_limited_count += 1
                continue

            # Apply your engine's zero-knowledge masking logic
            masked_token = self.engine.hash_account(tick["account"])

            # Pipe metrics directly into the standalone macro telemetry log system
            is_valid = log_system_metrics(tick["asset"], tick["price"], masked_token, tick_start)

            if is_valid:
                self.success_count += 1
            else:
                self.quarantine_count += 1

        # 4. Compile and output an official SRE infrastructure report
        run_performance_benchmark(
            self.success_count,
            self.quarantine_count,
            self.rate_limited_count,
            self.start_time
        )

        # Senior-Level Invariant Assertions
        self.assertGreater(self.success_count, 0, "System processed zero valid transactions.")
        self.assertEqual(self.quarantine_count, 1, "The Volatility Quarantine Engine failed to isolate the hazard.")

if __name__ == '__main__':
    unittest.main()