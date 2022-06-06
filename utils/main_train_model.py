from main_functions.utils.functions.train_model import *
from main_functions.utils.functions.read_and_export_data import output_datasets_folder_path

def main_train_model(model_type,X,y,df,dict_model_config,f,output_path = output_datasets_folder_path):
    if model_type == "basic":
        model = DecisionTreeClassifier(max_depth=15,random_state=42)
    if model_type == "tuned":
        tuned_params = hyper_param_tuning(X, y,dict_model_config)
        model = DecisionTreeClassifier(min_samples_leaf=tuned_params['min_samples_leaf'],
                                    max_leaf_nodes=tuned_params["max_leaf_nodes"],
                                    max_features=tuned_params["max_features"],
                                    max_depth=tuned_params["max_depth"],
                                    criterion=tuned_params["criterion"],random_state=42)
    model.fit(X, y)
    pred = model.predict(X)
    f.write("\n\n Deviance : "+ str(deviance(X,y,model)))
    f.write("\n"+ str(classification_report(y, pred)))
    f.write("\n"+ str(confusion_matrix(y, pred)))
    draw_tree_rules(model,X,model_type + "_model_tree_high_dpi")
    model_rules, model_dict_rules_best, model_best_rule = select_best_params(model, X, df)
    # Model Kurallara Göre Filtreleme
    model_filtered_data = df[eval(model_rules[model_best_rule])]
    model_filtered_data
    model_filtered_data.to_csv(output_path + model_type + "_model_filtered_data.csv")
    # Model Good Accuracy, Support, Scrap Rate
    model_support_count = len(model_filtered_data)
    if model_filtered_data["scrapflag"].nunique() > 1:
    
        model_scrap_rate = (model_filtered_data["scrapflag"].value_counts()[1] / model_support_count)*100
        
    else:
        model_scrap_rate = 0
    model_good_accuracy = 100 - model_scrap_rate
    print(model_scrap_rate)
    f.write("\n\n" + model_type + "Model Support Sayısı : "+str(model_support_count))
    f.write("\n" + model_type + "Model Good Accuracy : "+str(model_good_accuracy))
    f.write("\n" + model_type + "Model Scrap Rate : "+str(model_scrap_rate))
    # Model Kural Paktei
    model_rule_packet = model_rules[model_best_rule]
    f.write("\n" + model_type +  "Model Rule Packet : " + str(model_rule_packet))
    return model_rule_packet
    