import json
import pandas as pd
import numpy as np
import os

json_path = "..."
info_data_path = "..."
original_monthly_datasets_folder_path = "..."
original_merged_datasets_folder_path = "..."
output_datasets_folder_path = "..."

def read_json(file_name,json_path=json_path):
    with open(json_path + file_name , 'r') as f:
        json_file = json.loads(f.read())
    return json_file


def add_json(file_name, new_key, new_item, json_path=json_path):
    with open(json_path+file_name, "r") as file:
        data = json.load(file)
    data[new_key] = new_item
    with open(json_path+file_name, "w") as file:
        json.dump(data, file)

def read_dataset(data_path,headers, month, filter_headers=True):
    df = pd.read_excel(data_path)
    if filter_headers == True:
        df = df[headers]
    df["Month"] = month
    return df

def merge_and_export_datasets(json_file_name,output_file_name,data_folder = original_monthly_datasets_folder_path,
                              output_path=original_merged_datasets_folder_path,filter_headers=True):
    parameters_json_file = read_json(json_file_name)
    headers = parameters_json_file["for_model_params"] 
    os.chdir(data_folder)
    dataframe_path_list = os.listdir()
    df = pd.DataFrame(columns = headers)
    for data in dataframe_path_list:
        month_name = data.split("_")[0].lower()
        print("{} Ayı Başladı".format(month_name))
        if month_name == "temmuz":
            df = pd.concat([df,read_dataset(data_folder + data, 
                                               headers, month_name,filter_headers).loc[8618:]])
        df = pd.concat([df,read_dataset(data_folder + data, 
                                               headers, month_name,filter_headers)])
        print("{} Ayı Okundu".format(month_name))
    #temmuz_df = temmuz_df.loc
    #df = pd.concat([temmuz_df, agustos_df, eylul_df,
    #           ekim_df, kasım_df, aralık_df, ocak_df,
    #            subat_df, mart_df],axis=0)
    df.reset_index(drop="index", inplace=True)
    df.to_csv(output_path + output_file_name,index=False)
