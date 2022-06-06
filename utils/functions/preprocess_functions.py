import pandas as pd
import numpy as np


def delete_unique_columns(data):
    col = []
    for column in data.columns:
        if len(data[column].unique()) == 1:
            col.append(column)
    data.drop(col, axis=1, inplace=True)
    return data,col

def delete_most_include_9999(data, perc):
    col = []
    for column in data.columns:
        if perc*len(data) <= len(data[data[column] == -9999]):
            col.append(column)
    data.drop(col,axis=1,inplace=True)
    return data, col

def sigma_anomaly_bounds(feature,df):
    mini = float(df[feature].mean() - 3* df[feature].std())
    maxi = float(df[feature].mean() + 3* df[feature].std())
    return mini, maxi

def outlier_detect(x,min_,max_):
    if (x <= min_) | (x >= max_):
        return int(-9999)
    else:
        return x

def create_df_status(columns):
    df_status = pd.DataFrame(columns = columns)
    return df_status

def add_transaction_to_df_status(process_index, process_type, data,df_status):
    df_status.loc[process_index,"Process Step"] = process_type
    df_status.loc[process_index,"Good"] = data["scrapflag"].value_counts()[0]
    df_status.loc[process_index,"Scrap"] = data["scrapflag"].value_counts()[1]
    return df_status