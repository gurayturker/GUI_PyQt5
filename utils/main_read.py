from main_functions.utils.functions.read_and_export_data import read_json,info_data_path,original_merged_datasets_folder_path,pd

def main_read_config_and_data(parameter_json,
                              model_list_file,merged_data_file,merged_set_file,f,
                              info_data = info_data_path,
                              merged_data = original_merged_datasets_folder_path,):
    parameter_file = read_json(parameter_json)
    model_list = pd.read_excel(info_data + model_list_file)
    df = pd.read_csv(merged_data + merged_data_file)
    df_all = pd.read_csv(merged_data + merged_set_file)
    f.write("\n"+ str(df["Month"].nunique()) +str(" aylık birleştirilmiş veri seti okundu."))
    f.write("\n"+ str("Veri seti ") + str(df.shape[0]) +str(" satır ve ") + str(df.shape[1])+ str(" sutün içermektedir."))
    return parameter_file, model_list, df , df_all

