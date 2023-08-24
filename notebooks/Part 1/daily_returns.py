import pandas as pd

JPM_df = pd.read_csv('JPM.csv')
JPM_df['Daily Return'] = JPM_df['Adj Close'].pct_change(1) * 100
print(JPM_df['Daily Return'].max())