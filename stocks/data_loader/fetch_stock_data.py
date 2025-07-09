import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol="RELIANCE.NS", period="60d", interval="1d"):
    """
    Fetch historical stock data using Yahoo Finance.

    Args:
        symbol (str): Stock symbol (e.g., 'RELIANCE.NS')
        period (str): Time duration (e.g., '60d', '1y')
        interval (str): Time granularity (e.g., '1d', '1h', '5m')

    Returns:
        pd.DataFrame: DataFrame containing stock OHLCV data
    """
    df = yf.download(symbol, period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

# Test call
if __name__ == "__main__":
    df = fetch_stock_data("RELIANCE.NS", period="30d", interval="1d")
    print(df.head())
