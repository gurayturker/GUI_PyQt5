def calculate_scrap_rate(value,feature,data):
    try:
        scrap_count = data[data[feature] == value]["scrapflag"].value_counts()[1]
        good_count = data[data[feature] == value]["scrapflag"].value_counts()[0]
        scrap_rate = (scrap_count / (scrap_count + good_count))*100
    except:
        #print("Scrap Yok")
        scrap_rate = 0
    return scrap_rate


def create_recipe(data,threshold):
    dict_best_set_params = dict()
    for i in  data.columns:
        # tek değer sahip değişkenler
        if len(data[i].value_counts()) == 1:
            selected_param_value = data[i].unique()[0]
        # Birden fazla değere sahip değişkenler
        if len(data[i].value_counts()) > 1:
            type_mask = data[i].value_counts().index.dtype
            # int64 veya flaot
            if type_mask == "int64"  or type_mask == "float64" or type_mask == "int32" or type_mask =="float32":
                indexes = data[i].value_counts().sort_values(ascending=False).index[:2].values
                set_param1_count =  data[i].value_counts()[indexes[0]]
                set_param2_count =  data[i].value_counts()[indexes[1]]
                if (set_param1_count / set_param2_count) > 1.5:
                    selected_param_value = indexes[0]
                else:
                    scrap_rate_first = calculate_scrap_rate(indexes[0],i,data)
                    scrap_rate_second = calculate_scrap_rate(indexes[1],i,data)
                    #print("scrap_rate",i,scrap_rate_first,scrap_rate_second)
                    if scrap_rate_first > scrap_rate_second:
                        selected_param_value = indexes[1]
                    else:
                        selected_param_value = indexes[0]
            #object 
            elif  type_mask == "object" or type_mask == "boolen":
                true_count = data[i].value_counts()[True]
                false_count = data[i].value_counts()[False]
                if true_count >= false_count:
                    if (true_count / false_count) > threshold:
                        selected_param_value = "True"
                    else:
                        scrap_rate_true = calculate_scrap_rate(True,i,data)
                        scrap_rate_false = calculate_scrap_rate(False,i,data)
                        if scrap_rate_true > scrap_rate_false:
                            selected_param_value = "False"
                        else:
                            selected_param_value = "True"
                else:
                    if (false_count / true_count) > threshold:
                        selected_param_value = "False"
                    else:
                        scrap_rate_true = calculate_scrap_rate(True,i,data)
                        scrap_rate_false = calculate_scrap_rate(False,i,data)
                        if scrap_rate_true > scrap_rate_false:
                            selected_param_value = "False"
                        else:
                            selected_param_value = "True"

        dict_best_set_params[i] = selected_param_value
    return dict_best_set_params