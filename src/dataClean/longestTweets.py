import pandas as pd

class LongestTweets:
    def __init__(self,dataframe):
        self.df = dataframe

    def longest(self,column,word_column):
        longest_tweets = {}
        for val in self.df[column].unique():
            con = self.df[column] == val
            df_split = self.df[con]
            df_split['len_text'] = df_split[word_column].str.len()
            df_split.sort_values('len_text',inplace=True)
            long_tweets = []
            for tweet in df_split[word_column][-3:]:
                long_tweets.append(tweet)
            try:
                longest_tweets[int(val)] = long_tweets
            except ValueError:
                longest_tweets[val] = long_tweets
        return longest_tweets

df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
a = LongestTweets(df)
print(a.longest('Biased','Text'))