import ta
import pandas as pd
import numpy as np

def add_indicators(df):
    # Ensure 'Close' exists
    if 'Close' not in df.columns:
        raise ValueError("DataFrame does not have a 'Close' column")
    
    # Convert to numeric and drop invalid rows
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=['Close'])
    
    # Ensure Close is 1-D Series
    close_series = df['Close'].squeeze()
    if not isinstance(close_series, pd.Series):
        close_series = pd.Series(close_series)
    
    # Check enough data for EMA50
    if len(close_series) < 50:
        raise ValueError("Not enough data to calculate EMA50. Try a longer period or shorter interval.")
    
    # Calculate indicators
    df['EMA50'] = ta.trend.EMAIndicator(close_series, window=50).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close_series, window=14).rsi()
    
    return df
