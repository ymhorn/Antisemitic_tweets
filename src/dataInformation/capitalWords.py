import pandas as pd

class CapitalAmount:
    def __init__(self,dataframe):
        self.df = dataframe

    def capital_for_all(self,column,word_column):
        capital_amount_dict ={}
        capital_amount_dict['total'] = self.capital_amount(self.df,word_column)
        for val in self.df[column].unique():
            con = self.df[column] == val
            df_split = self.df[con]
            try:
                capital_amount_dict[int(val)] = self.capital_amount(df_split,word_column)
            except ValueError:
                capital_amount_dict[val] = self.capital_amount(df_split,word_column)
        return capital_amount_dict

    @staticmethod
    def capital_amount(dataframe,word_column):
        all_words = []
        for text in dataframe[word_column]:
            all_words.append(text.split(' '))
        capital = 0
        for i in all_words:
            for j in i:
                if j.isupper():
                    capital += 1
        return capital

# df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
# a = CapitalAmount(df)
# print(a.capital_for_all('Biased','Text'))