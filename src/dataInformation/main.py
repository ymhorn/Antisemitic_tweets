import pandas as pd
from capitalWords import CapitalAmount
from commonWords import CommonWords
from longestTweets import LongestTweets
from tweetAmounts import TweetAmounts
from tweetLengths import TweetLengths
from pprint import pprint
import json

df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
final_dict = {}
column = 'Biased'
word_column = 'Text'
df[column].replace(0,'non_antisemitic',inplace=True)
df[column].replace(1,'antisemitic',inplace=True)
capital = CapitalAmount(df)
common = CommonWords(df)
longest = LongestTweets(df)
amounts = TweetAmounts(df)
length = TweetLengths(df)
final_dict['total_tweets'] = amounts.amounts(column)
final_dict['average_length'] = length.average(column, word_column)
final_dict['common_words'] = common.common(word_column)
final_dict['longest_3_tweets'] = longest.longest(column, word_column)
final_dict['uppercase_words'] = capital.capital_for_all(column, word_column)
pprint(final_dict)

with open('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\results\\results.json','w') as f:
    json.dump(final_dict,f)

