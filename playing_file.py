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

df['len_text'] = df['Text'].str.split(' ').str.len()
print(df.groupby('Biased')['len_text'].mean())
print(df.head())
df.drop('len_text',axis=1,inplace=True)
print(df.head())
