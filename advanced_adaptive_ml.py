import time
import logging
import numpy as np
from scipy import stats

# SENIOR MACRO CONFIGURATION: Advanced SRE Data Science Logging Grid
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s.%(msecs)03d] [%(levelname)s] [ADAPTIVE-AI] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("AdaptiveMLCore")

class RollingWindowPredictiveEngine:
    def __init__(self, window_capacity=5, risk_ceiling=55000.0):
        """
        Initializes an advanced rolling data matrix buffer.
        Automatically flushes stale data out of memory to prevent historical drift tracking lag.
        """
        self.window_capacity = window_capacity
        self.risk_ceiling = risk_ceiling

        # Internal sliding window matrices
        self.time_buffer = []
        self.value_buffer = []

        # Trained coefficients
        self.slope = 0.0
        self.intercept = 0.0
        self.r_squared = 0.0

    def ingest_live_tick_and_retrain(self, current_time: float, current_value: float):
        """
        Ingests a live data point, shifts the memory frame, and executes an automated
        on-the-fly model re-training sequence to adapt to volatile market conditions.
        """
        start_bench = time.perf_counter()

        # 1. Enforce strict sliding window data capacity boundaries
        self.time_buffer.append(current_time)
        self.value_buffer.append(current_value)

        if len(self.time_buffer) > self.window_capacity:
            self.time_buffer.pop(0) # Evict stale time coordinates
            self.value_buffer.pop(0) # Evict stale telemetry coordinates
            logger.debug("BUFFER MAINTENANCE: Evicted oldest out-of-frame matrix point.")

        # 2. Check for sufficient telemetry coordinates to compute trend vectors
        if len(self.time_buffer) < 3:
            logger.info(f"BUFFERING: Ingested point ({current_time}, ${current_value:.2f}). Waiting for cluster synchronization...")
            return None

        # 3. Convert buffers to high-velocity NumPy arrays
        x_matrix = np.array(self.time_buffer, dtype=float)
        y_matrix = np.array(self.value_buffer, dtype=float)

        # 4. Compute the live mathematical linear regression trajectory
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_matrix, y_matrix)

        self.slope = slope
        self.intercept = intercept
        self.r_squared = r_value ** 2

        latency_ms = (time.perf_counter() - start_bench) * 1000

        logger.info(
            f"🔄 LIVE RE-TRAINED | Frame Size: {len(self.time_buffer)} | "
            f"Trajectory: {self.slope:+.2f} | Confidence (R²): {self.r_squared*100:.1f}% | "
            f"Compute Latency: {latency_ms:.4f}ms"
        )
        return self.r_squared

    def generate_horizon_forecast(self, lookahead_steps=2.0) -> float:
        """
        Projects current trend trajectories into future vector horizons.
        Triggers critical macro containment flags if the prediction cuts through the safety ceiling.
        """
        if len(self.time_buffer) < 3:
            return 0.0

        # Calculate future target timeline intersection point (y = mx + b)
        latest_time = self.time_buffer[-1]
        future_horizon = latest_time + lookahead_steps
        predicted_outcome = (self.slope * future_horizon) + self.intercept

        # Predictive Risk Analytics Layer
        if predicted_outcome >= self.risk_ceiling:
            logger.critical(
                f"🚨 BREAKOUT VOLATILITY DETECTED! Rolling forecast projects a BREACH! "
                f"Predicted: ${predicted_outcome:.2f} breaks Risk Ceiling [${self.risk_ceiling:.2f}] "
                f"at time horizon {future_horizon}!"
            )
        else:
            logger.info(f"🔮 PREDICTIVE HORIZON: Projected state at time {future_horizon} is Stable: ${predicted_outcome:.2f}")

        return predicted_outcome

if __name__ == "__main__":
    print("Launching Advanced Rolling-Window Adaptive AI Pipeline...")
    adaptive_ai = RollingWindowPredictiveEngine(window_capacity=5, risk_ceiling=55000.0)

    # Simulated Stream: An asset climbing steadily, taking a sharp sudden spike, then leveling off
    simulated_live_stream = [
        (1.0, 42000.0), (2.0, 43000.0), (3.0, 44500.0), # Initial buffer setup
        (4.0, 46000.0), (5.0, 48500.0), # Steady climb
        (6.0, 53000.0), # Massive shock wave surge! Triggers Predictive Critical Breach
        (7.0, 53200.0), (8.0, 53400.0) # Sudden market stabilization - AI adapts live and clears the alarm!
    ]

    for timestamp, price in simulated_live_stream:
        time.sleep(0.1) # Simulated network transmission interval
        adaptive_ai.ingest_live_tick_and_retrain(timestamp, price)
        adaptive_ai.generate_horizon_forecast(lookahead_steps=1.5)
        print("-" * 80)