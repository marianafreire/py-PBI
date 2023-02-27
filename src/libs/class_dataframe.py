import pandas as pd
import os

class Dataframe:
    '''
    This class provides methods to read a CSV file, reduce it, modify the types of some columns and write
    the resulting data to a new CSV file.
    '''
    def __init__(self, old_df_path):
        self.old_df_path = old_df_path
        self.old_df = pd.read_csv(self.old_df_path, dtype={"('P3_b ', 'Quais desses papéis/cargos fazem parte do time (ou chapter) de dados da sua empresa?')" : str})

    def reduce_columns(self, preserved_columns):
        '''This method preserves certain columns and saves them in a new dataframe variable'''
        self.preserved_columns = preserved_columns
        self.new_df = self.old_df.loc[:,self.preserved_columns]
    
    def change_columns_type(self, numeric_columns):
        '''
        This method eliminates empty rows and converts selected columns to numeric type. 
        If any columns or rows cannot be converted to numeric type, they will be converted to NaN.
        '''
        self.new_df = self.new_df.dropna(subset=numeric_columns)
        try:
            for col in numeric_columns:
                self.new_df[col] = self.new_df[col].apply(pd.to_numeric)
        except:
            for col in numeric_columns:
                self.new_df[col] = pd.to_numeric(self.new_df[col], errors='coerce')
            print('Some columns/rows of your dataframe couldnt be converted to a numeric type and were replaced to NaN instead')
                
    def create_csv(self,csv_folder_path,csv_name):
        '''This method saves the new dataframe on a CSV file'''
        self.csv_folder_path = csv_folder_path
        self.csv_name = csv_name
        new_df_path = os.path.join(csv_folder_path,csv_name)
        self.new_df.to_csv(new_df_path, index=False)

    # TODO: summarize and replace the data of some columns