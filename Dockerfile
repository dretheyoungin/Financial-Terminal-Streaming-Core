# 1. Use the official lightweight Python runtime environment as our foundation
FROM python:3.10-slim

# 2. Set an isolated, high-security working directory inside the virtual server
WORKDIR /app

# 3. Copy our trading core and test suite from your laptop straight into the container
COPY crypto_ticker_engine.py .
COPY test_ticker_engine.py .

# 4. Flush Python print streams instantly to the logs to prevent data caching delays
ENV PYTHONUNBUFFERED=1

# 5. Define the execution hook command to run the financial test suite automatically on boot
CMD ["python", "-m", "unittest", "test_ticker_engine.py"]