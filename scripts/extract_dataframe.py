import pandas as pd

def read_csv_file(filePath:str)->pd.DataFrame:
    return pd.read_csv(filePath)
def save_as_csv(dataframe, filePath:str):
    dataframe.to_csv(filePath)
    return filePath


class ExtractDataframe:
    
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def get_rows(self, colName, colValue):
        return self.dataframe.loc[self.dataframe[colName]==colValue]
    
    def get_unique_categories(self, dataframe):
        return self.get_categories(dataframe).nunique()
    
    def get_categories(self,dataframe):
        return dataframe.select_dtypes(exclude=['number'])
    
    def get_online_user_reply(self,dataframe,colName):
        return dataframe.groupby(colName).agg({'yes':'sum','no':'sum'}).sort_values(by=['yes','no'], ascending=False)

