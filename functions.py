import numpy as np
import pandas as pd
from scipy import stats
import pdb

def strip_spaces(df):            
    df = df.applymap(lambda x: x.strip() if type(x) == str else x)
    print("stripped leading/trailing spaces from all cells of string type")
    return df

def check_duplicates(df):
    num_of_duplicates = df.duplicated().sum()
    if num_of_duplicates:
        print("there are {} duplicates".format(num_of_duplicates))
    else:
        print("You're all clear of duplicates")

def replace_column_w_nan(df, list_of_columns, replace):
    for column in list_of_columns:
        df[column] = df[column].replace(to_replace=replace, value=np.nan)
    print("Replaced {} values from these columns:{}".format(replace, list_of_columns))
    return df
    
def drop_na_rows(df, list_of_columns):
    print("Removed NA rows from these columns:{}.".format(list_of_columns))
    return df.dropna(axis=0, subset=list_of_columns)

def drop_columns(df, list_of_columns):
    print("Dropped these columns:{}".format(list_of_columns))
    return df.drop(axis=1, columns=list_of_columns)
                
def remove_outliers(df, col_names):
    for col in col_names:
        df.reset_index(inplace=True,drop=True)
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3-q1 #Interquartile range
        fence = 1.5*iqr
        fence_low = q1-fence
        fence_high = q3+fence
        df = df.loc[(df[col] > fence_low) & (df[col] < fence_high)]
    df.reset_index(inplace=True,drop=True)
    return df

# Useful function, but incorrectly used in this project.
# 
# def remove_outliers(df, list_of_columns, zthreshold=3):
#     """zthreshold is an optional parameter default set to 3"""
#     for column in list_of_columns:
#         df.reset_index(inplace=True,drop=True)
#         column_zscore = get_z_score(df[column])
#         df = drop_high_zscores(df, column_zscore, zthreshold)
#     print("Removed outliers from these columns:{}".format(list_of_columns))
#     return df

# def get_z_score(df_column):
#     zscore_list = np.abs(stats.zscore(df_column))
#     return enumerate(zscore_list)

# def drop_high_zscores(df, enumerated_zscores,zthreshold):
#     for index, element in enumerated_zscores:
#         if element > zthreshold:
#             df = df.drop([index])
#     return df

