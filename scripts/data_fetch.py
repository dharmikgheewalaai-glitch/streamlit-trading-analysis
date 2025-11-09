import yfinance as yf
import pandas as pd
import os

def fetch_data(symbol='^NSEI', period='3mo', interval='15m'):
    os.makedirs("data", exist_ok=True)
    df = yf.download(symbol, period=period, interval=interval)
    df.reset_index(inplace=True)
    file_name = f"data/{symbol.replace('^','')}_{interval}.csv"
    df.to_csv(file_name, index=False)
    print(f"✅ Data saved to {file_name}")
    return df
