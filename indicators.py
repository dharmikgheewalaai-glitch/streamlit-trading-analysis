import ta
import pandas as pd
import numpy as np

def add_indicators(df):
    # Check 'Close' exists
    if 'Close' not in df.columns:
        raise ValueError("DataFrame does not have a 'Close' column")

    # Flatten column if multi-indexed (happens with yfinance sometimes)
    if isinstance(df['Close'], pd.DataFrame):
        df['Close'] = df['Close'].iloc[:,0]

    # Convert to numeric
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # Remove invalid values
    df['Close'] = df['Close'].replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=['Close'])

    # Ensure 1D Series
    close_series = df['Close']
    if not isinstance(close_series, pd.Series):
        close_series = pd.Series(close_series)

    # Check length
    if len(close_series) < 50:
        raise ValueError("Not enough data to calculate EMA50. Try a longer period or shorter interval.")

    # Calculate indicators
    df['EMA50'] = ta.trend.EMAIndicator(close_series, window=50).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close_series, window=14).rsi()

    return df
