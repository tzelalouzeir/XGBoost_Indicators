import pandas as pd
import pandas_ta as ta
import datetime
import yfinance as yf

# Fetching 120 days of data with 1hour timeframe and save as csv
df= yf.download("BTC-USD",period="120d",interval="1h")
df.to_csv('btc120d.csv')

# Load your data from CSV
df = pd.read_csv('btc120d.csv', parse_dates=['Datetime']) # For day timeframe using 'Date' column and for Hours and Minutes is 'Datetime'
df.set_index('Datetime', inplace=True)

# Calculate 12 indicators using pandas_ta
df.ta.sma(length=50, append=True)
df.ta.ema(length=50, append=True)
df.ta.wma(length=50, append=True)
df.ta.macd(fast=12, slow=26, append=True)
df.ta.rsi(length=14, append=True)
df.ta.bbands(length=20, append=True)
df.ta.adx(length=14, append=True)
df.ta.stoch(length=14, append=True)
df.ta.willr(length=14, append=True)
df.ta.roc(length=10, append=True)
df.ta.cci(length=20, append=True)
df.ta.atr(length=14, append=True)


# Create an empty column for long/short/neutral signals
df['Signal'] = None

# Identify long and short positions based on Close price for labeling, window_size is bar or canlde to look
window_size = 1
for i in range(window_size, len(df)):
    close_diff = df['Close'].iloc[i] - df['Close'].iloc[i - window_size]
    
    if close_diff > 0:
        df.at[df.index[i], 'Signal'] = 'long'
    elif close_diff < 0:
        df.at[df.index[i], 'Signal'] = 'short'
    else:
        df.at[df.index[i], 'Signal'] = 'neutral'

# Drop OHLC and Adj Close cause we need only indicators
df.drop(['Open', 'High', 'Low', 'Close', 'Adj Close'], axis=1, inplace=True)

# Now you can analyze indicator values at each signal point
long_condition = df['Signal'] == 'long'
short_condition = df['Signal'] == 'short'
neutral_condition = df['Signal'] == 'neutral'

long_indicators = df.loc[long_condition].select_dtypes(include=['float64']).mean()
short_indicators = df.loc[short_condition].select_dtypes(include=['float64']).mean()
neutral_indicators = df.loc[neutral_condition].select_dtypes(include=['float64']).mean()


# Finding relations between indicators, for example correlation matrix
correlation_matrix = df.select_dtypes(include=['float64']).corr()

print(f'\nCandle Look: {window_size}\n')
print('Long Indicators:\n', long_indicators)
print('Short Indicators:\n', short_indicators)
print('Neutral Indicators:\n', neutral_indicators)
print('Correlation Matrix:\n', correlation_matrix)
