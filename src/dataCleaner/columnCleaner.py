import pandas as pd

class ColumnCleaner:
    def __init__(self,dataframe):
        self.df = dataframe

    def clean(self,columns):
        return self.df.drop(columns,axis=1,inplace=True)
