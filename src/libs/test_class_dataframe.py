import os
import pandas as pd
import pytest
from class_dataframe import Dataframe
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='module')
def choose_columns():
    return {
        'preserved_columns': ['codigo','nome','marca','preco'],
        'numeric_columns'  : ['codigo','preco'],
        'nan_columns'      : ['nome','marca']
    }

@pytest.fixture(scope ='module')
def create_dataframe(choose_columns):
    csv_folder_path = os.getenv('PATH_CSV')
    old_df_path = os.path.join(csv_folder_path, 'csv_test.csv')

    df = Dataframe(old_df_path)
    df.reduce_columns(choose_columns['preserved_columns'])
    df.change_columns_type(choose_columns['numeric_columns'])
    return df

# happy path testing
def test_read_csv(create_dataframe):
    assert isinstance(create_dataframe.old_df, pd.DataFrame)

def test_reduce_columns(create_dataframe,choose_columns):
    assert set(create_dataframe.new_df.columns) == set(choose_columns['preserved_columns'])

def test_columns_numeric(create_dataframe,choose_columns):
    for col in choose_columns['numeric_columns']:
        assert pd.api.types.is_numeric_dtype(create_dataframe.new_df[col])

def test_create_csv(create_dataframe):
    csv_folder_path = os.getenv('PATH_CSV')
    new_df_path = os.path.join(csv_folder_path, 'new_df_test.csv')
    create_dataframe.create_csv(csv_folder_path, 'new_df_test.csv')
    expected_df = pd.read_csv(new_df_path)
    pd.testing.assert_frame_equal(create_dataframe.new_df, expected_df)

# sad path testing
def test_columns_NaN(create_dataframe,choose_columns):
    create_dataframe.change_columns_type(choose_columns['nan_columns'])
    for col in choose_columns['nan_columns']:
        assert pd.isna(create_dataframe.new_df[col]).any()

# TODO: sad path testing to improve test coverage