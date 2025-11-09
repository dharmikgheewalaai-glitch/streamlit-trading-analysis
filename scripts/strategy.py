def generate_signals(df):
    df['Signal'] = 0
    df['Position'] = 0
    stop_loss_pct = 0.02
    take_profit_pct = 0.03

    for i in range(1, len(df)):
        if df['Close'][i] > df['EMA50'][i] and df['RSI'][i] < 70 and df['Position'][i-1] == 0:
            entry_price = df['Close'][i]
            stop_loss = entry_price * (1 - stop_loss_pct)
            take_profit = entry_price * (1 + take_profit_pct)
            df.at[i, 'Position'] = 1
        elif df['Position'][i-1] == 1:
            if df['Close'][i] <= stop_loss or df['Close'][i] >= take_profit:
                df.at[i, 'Position'] = 0
            else:
                df.at[i, 'Position'] = 1
    return df
