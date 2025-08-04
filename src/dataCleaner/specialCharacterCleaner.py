import pandas as pd
import re

class SpecialCharacterCleaner:
    def __init__(self,dataframe):
        self.df = dataframe

    def clean(self,column):
        for val in self.df[column]:

