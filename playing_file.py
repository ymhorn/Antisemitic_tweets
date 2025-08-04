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

# df['len_text'] = df['Text'].str.split(' ').str.len()
# a = df['Text'][df['Text'].str.len().max()]
# print(df['Text'][df['Text'].str.len().max()])
con = df['Biased'] == 1
df1 = df[con]
df1['len_text'] = df1['Text'].str.len()
df1.sort_values(by='len_text',inplace=True)
# print(df1['Text'].str.len())
print(df1['Text'][:3])
