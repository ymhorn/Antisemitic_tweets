import pandas as pd

class CommonWords:
    def __init__(self,dataframe):
        self.df = dataframe

    def common(self,word_column):
        all_words = []
        for text in self.df[word_column]:
            all_words.append(text.split(' '))
        dict_of_words = {}
        for i in all_words:
            for j in i:
                if j in dict_of_words:
                    dict_of_words[j] += 1
                else:
                    dict_of_words[j] = 1
        df_words = pd.DataFrame(dict_of_words.items(),columns=['words','amount'])
        df_words.sort_values('amount',inplace=True)
        common_words = []
        for word in df_words['words'][-10:]:
            common_words.append(word)
        return common_words

# df = pd.read_csv('C:\\Users\\Yisroel Meir\\PycharmProjects\\Antisemitic_tweets\\data\\tweets_dataset.csv')
# a = CommonWords(df)
# print(a.common('Text'))