import pandas as pd

JPM_df = pd.read_csv('JPM.csv')
JPM_df.isnull().sum()
JPM_df.info()