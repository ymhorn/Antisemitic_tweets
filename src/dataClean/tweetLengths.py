import pandas as pd

class TweetLengths:
    def __init__(self,dataframe):
        self.df = dataframe

    def average(self,column,word_column):
        tweet_lengths = {}
        self.df['len_text'] = self.df[word_column].str.split(' ').str.len()
        tweet_lengths['total'] = float(self.df['len_text'].mean())
        for val in self.df[column].unique():
            try:
                tweet_lengths[int(val)] = float(self.df.groupby(column)['len_text'].mean()[val])
            except ValueError:
                tweet_lengths[val] = float(self.df.groupby(column)['len_text'].mean()[val])
        self.df.drop('len_text',axis=1,inplace=True)
        return tweet_lengths

# df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
# a = TweetLengths(df)
# print(a.average('Biased','Text'))