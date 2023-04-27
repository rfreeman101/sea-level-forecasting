# Required imports for below functions:
import numpy as np
import pandas as pd
import calendar
import datetime

####################################################################################################################

def basic_eda(df):
    """
    Returns basic information about the dataframe
    - Shape
    - Column data types
    - Number of null values per column
    - Number of duplicate rows and columns

    Arguments:
        df (dataframe): dataframe containing the data for analysis
        df_name (string): name of the dataframe
    """
    print('SHAPE')
    print(f"Rows: {df.shape[0]} \t Columns: {df.shape[1]}")
    print()
    print('DATATYPES')
    print(f'Columns: \n{df.dtypes}')
    print(f'Index: {df.index.inferred_type}')
    print()
    print('UNIQUE VALUES')
    print(df.nunique())
    print()
    print('NULL VALUES')
    print(f"Total null rows: {df.isnull().sum().sum()}")
    print(f"Percentage null rows: {round(df.isnull().sum().sum() / df.shape[0]*100, 2)}%")
    if df.isnull().sum().sum() > 0:
        print('Null values:')
        print(df.isnull().sum())
    print()
    print('DUPLICATES')      
    print(f"Total duplicate rows: {df[df.duplicated(keep=False)].shape[0]}")
    print(f"Percentage duplicate rows: {round(df[df.duplicated(keep=False)].shape[0] / df.shape[0] * 100, 2)}%")
    print()
    print("-----\n")

####################################################################################################################

def resample_timeseries(df):
    """
    Resamples a timeseries pandas dataframe to run from April 2002 until November 2022 and sets the reading interval 
    to a monthly reading.

    Arguments:
        df (dataframe)
    """
    # Resample to take entries from April 2002 to November 2022 inclusive.
    df = df['2002-04-01':'2022-11-30']

    # Resample to monthly means.
    df = df.resample('M').mean()
    return df

####################################################################################################################

def decimal_to_datetime(decimal_date):
    """
    Takes a float and returns a date.

    Arguments:
        decimal_date (float) - a yearly decimal, e.g. 2002.5 would return 2002-06-01.
    """
    # Extract first four digits as year.
    year = int(str(decimal_date)[0:4])

    # Calculate elapsed days from the 1st of January within each respective year.
    elapsed_days = (round(decimal_date - year,2))*(365 + calendar.isleap(year))

    # Add elapsed time to 1st January to return calendar date.
    return pd.to_datetime(datetime.datetime(year,1,1) + datetime.timedelta(days=elapsed_days)).strftime('%Y-%m-%d')

####################################################################################################################