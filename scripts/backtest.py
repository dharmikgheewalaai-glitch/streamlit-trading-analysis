def backtest(df):
    df['Returns'] = df['Close'].pct_change() * df['Position'].shift(1)
    df['Cumulative'] = (1 + df['Returns']).cumprod()
    return df
