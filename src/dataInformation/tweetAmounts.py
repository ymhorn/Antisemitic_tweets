import pandas as pd

class TweetAmounts:
    def __init__(self,dataframe):
        self.df = dataframe

    def amounts(self,column):
        tweet_amounts = {}
        tweet_amounts['total'] = int(self.df[column].count())
        for val in self.df[column].unique():
            try:
                tweet_amounts[int(val)] = int(self.df[column].value_counts()[val])
            except ValueError:
                tweet_amounts[val] = int(self.df[column].value_counts()[val])
        return tweet_amounts




# df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
# a = TweetAmounts(df)
# print(a.amounts('Biased'))

