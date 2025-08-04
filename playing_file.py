import pandas as pd

df = pd.read_csv('data/tweets_dataset.csv')
print(df.head())
print(df.columns)
print(df['Biased'].unique())
print(df['Keyword'].unique())
# print(df['Username'].nunique())
print(df.shape)
for val in df['Biased'].unique():
    print(val,df['Biased'].value_counts()[val])