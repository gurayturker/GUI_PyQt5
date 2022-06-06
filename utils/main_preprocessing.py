from main_functions.utils.functions.preprocess_functions import *

def main_select_model(selected_model,
                model_list,data,f):
    P_ID = model_list[model_list["Model"]== selected_model]["SId"].values[0]
    selected_df = data[data["PId_x"] == P_ID]
    f.write("\n\n"+ str(10*" ") + str(selected_model) +str(" Modeli Seçilmiştir"))
    f.write("\n"+ 60*("-"))
    f.write("\n"+ str(selected_model) +str(" modeline ait ") + str(selected_df.shape[0]) + str(" satır ve ") + str(selected_df.shape[1]) + str(" sutün bulunmaktadır."))
    return selected_df

def drop_mould_over_percentage_scraprate(data,percentage,f):
    drop_mould_dict = {}
    for mould in data["Mould"].unique():
        try:
            good = data[data["Mould"] == mould]["scrapflag"].value_counts()[0]
            scrap = data[data["Mould"] == mould]["scrapflag"].value_counts()[1]
        except:
            good = data[data["Mould"] == mould]["scrapflag"].value_counts()[0]
            scrap = 0
    scrap_rate = (scrap / (scrap + good))*100
    if scrap_rate > percentage:
        
        drop_mould_dict[mould] = scrap_rate
    
    return drop_mould_dict

def main_delete_unique_columns(data,drop,f):
    if drop == "Sil":
        data, unique_cols = delete_unique_columns(data)
        f.write("\n\n"+"A.1 : Tek Eşsiz Değer İçeren Özniteliklerin Silinmesi ----- >  Good : " + str(data["scrapflag"].value_counts()[0]) + " Scrap : " + str(data["scrapflag"].value_counts()[1]))
        f.write("\n"+ "    Silininen Öznitelikler : "+ str(unique_cols))
    else:
        f.write("\n A.1 : Tek Değere Sahip Öznitelikler Silinmemiştir.")
    return data


def main_delete_most_include_9999(data,drop,percentage,f):
    if drop == "Sil":
        data, perc70_cols = delete_most_include_9999(data,percentage/100)
        f.write("\n\n"+"A.2 : %70'den fazla satırı -9999 olan Özniteliklerin Silinmesi ----- >  Good : " + str(data["scrapflag"].value_counts()[0]) + " Scrap : " + str(data["scrapflag"].value_counts()[1]))
        f.write("\n"+ "    Silininen Öznitelikler : "+ str(perc70_cols))
    else:
        f.write("\n A.2 :  %70'den fazla satırı -9999 olan Öznitelikler Silinmemiştir.")
    return data


def main_delete_missing_values(data,drop,f):
    data.replace(-9999,np.nan,inplace=True)
    eksik_index = data.isna().sum().sort_values(ascending=False)[list(np.where(data.isna().sum().sort_values(ascending=False)>0)[0])].index
    eksik_deger = data.isna().sum().sort_values(ascending=False)[list(np.where(data.isna().sum().sort_values(ascending=False)>0)[0])].values
    if drop == "Sil":
        data.dropna(axis=0,inplace=True)
        f.write("\n\n"+"A.3 : Eksik Verilerin Silinmesi ----- >  Good : " + str(data["scrapflag"].value_counts()[0]) + " Scrap : " + str(data["scrapflag"].value_counts()[1]))  
    else:
        f.write("\n A.3 : Eksik Veriler Silinmemiştir.")
    f.write("\n"+ "    Eksik Veri İçeren Öznitelikler ve Sayıları : ")
    for i in range(len(eksik_index)):
        f.write("\n    " + eksik_index[i] + " --- > " + str(eksik_deger[i]))   
    return data

def determine_anom_features(data,scope):
    numeric_cols = data.select_dtypes(exclude=[object, bool]).columns.values  
    numeric_cols = np.delete(numeric_cols, np.where(numeric_cols == "scrapflag"))
    time_features = [...]
    if scope == "Sürekli":
        anom_features = list(set(numeric_cols) - set(time_features))
    elif scope == "Sürekli + Kesikli":
        anom_features = numeric_cols
    return anom_features

def main_delete_anomaly_values(data,drop,method,target,scope,f):
    anom_features = determine_anom_features(data,scope)
    if drop:
        # Hangi anomali bulma methodunun kullanacağı seçilmektedir.
        if method == "Sigma":
            selected_df_scrap  = data[data["scrapflag"] == 1]
            selected_df_good  = data[data["scrapflag"] == 0]
            # Sadece Goodlara anomali uygulanmaktadır.
            if target == "Good":
                for i in anom_features:
                    mini, maxi = sigma_anomaly_bounds(i,selected_df_good)
                    selected_df_good[i] = selected_df_good[i].apply(lambda x: outlier_detect(x,mini, maxi))
                selected_df_good.replace(-9999, np.nan, inplace=True)
                anomali_index = selected_df_good.isna().sum().sort_values(ascending=False)[list(np.where(selected_df_good.isna().sum().sort_values(ascending=False)>0)[0])].index
                anomali_deger = selected_df_good.isna().sum().sort_values(ascending=False)[list(np.where(selected_df_good.isna().sum().sort_values(ascending=False)>0)[0])].values
                selected_df_good.dropna(axis=0,inplace = True)   
            # Sadece Scraplere anomali uygulanmaktadır.
            elif target == "Scrap":
                for i in anom_features:
                    mini, maxi = sigma_anomaly_bounds(i,selected_df_scrap)
                    selected_df_scrap[i] = selected_df_scrap[i].apply(lambda x: outlier_detect(x,mini, maxi))
                selected_df_scrap.replace(-9999, np.nan, inplace=True)
                anomali_index = selected_df_scrap.isna().sum().sort_values(ascending=False)[list(np.where(selected_df_scrap.isna().sum().sort_values(ascending=False)>0)[0])].index
                anomali_deger = selected_df_scrap.isna().sum().sort_values(ascending=False)[list(np.where(selected_df_scrap.isna().sum().sort_values(ascending=False)>0)[0])].values
                selected_df_scrap.dropna(axis=0,inplace = True)
            else:
                for i in anom_features:
                    mini, maxi = sigma_anomaly_bounds(i,data)
                    data[i] = data[i].apply(lambda x: outlier_detect(x,mini, maxi))
                data.replace(-9999, np.nan, inplace=True)
                anomali_index = data.isna().sum().sort_values(ascending=False)[list(np.where(data.isna().sum().sort_values(ascending=False)>0)[0])].index
                anomali_deger = data.isna().sum().sort_values(ascending=False)[list(np.where(data.isna().sum().sort_values(ascending=False)>0)[0])].values
                data.dropna(axis=0,inplace = True)
                selected_df_scrap  = data[data["scrapflag"] == 1]
                selected_df_good  = data[data["scrapflag"] == 0]
            df_model = pd.concat([selected_df_good,selected_df_scrap],axis=0)
            df_model.sort_index(inplace=True)
            f.write("\n\n"+"A.4 : " + target + " Anomalilerin Verilerin Silinmesi ----- >  Good : " + str(df_model["scrapflag"].value_counts()[0]) + " Scrap : " + str(df_model["scrapflag"].value_counts()[1]))
            f.write("\n"+ "    Anomali Veri İçeren Öznitelikler ve Sayıları : ")
            for j in range(len(anomali_index)):
                f.write("\n    " + anomali_index[j] + " --- > " + str(anomali_deger[j]))
        else:
            pass
    else:
        f.write("\n A.4 : Anomali Veriler Silinmemiştir.")

    return df_model
