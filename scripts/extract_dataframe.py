import pandas as pd

categorical_var = ["device_make","platform_os","browser"]
def read_csv_file(filePath:str)->pd.DataFrame:
    return pd.read_csv(filePath)

class ExtractDataframe:
    
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def get_rows(self, colName, colValue):
        return self.dataframe.loc[self.dataframe[colName]==colValue]
    
    def get_unique_categories(self, colName):
        return self.dataframe[colName].nunique()
    
    def get_categories(self):
        return categorical_var

