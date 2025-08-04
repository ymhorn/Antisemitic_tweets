import pandas as pd
from pandas import RangeIndex

df = pd.read_csv('data/tweets_dataset.csv')
# print(df.head())
# print(df.columns)
# print(df['Biased'].unique())
# print(df['Keyword'].unique())
# # print(df['Username'].nunique())
# print(df.shape)
# for val in df['Biased'].unique():
#     print(val,df['Biased'].value_counts()[val])

# df['len_text'] = df['Text'].str.split(' ').str.len()
# a = df['Text'][df['Text'].str.len().max()]
# print(df['Text'][df['Text'].str.len().max()])
# con = df['Biased'] == 1
# df1 = df[con]
# df1['len_text'] = df1['Text'].str.len()
# df1.sort_values(by='len_text',inplace=True)
# # print(df1['Text'].str.len())
# print(df1['Text'][:3])
all = []
for a in df['Text']:
    all.append(a.split(' '))
dict = {}
for i in all:
    for j in i:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
# print(df['Text'].str.split(' '))
df1 = pd.DataFrame(dict.items(),columns=['words','amount'])
df1.sort_values('amount',inplace=True)
a = []
for word in df1['words'][-10:]:
    a.append(word)
print(a)
