
from sklearn.model_selection import train_test_split, RandomizedSearchCV

from sklearn.tree import DecisionTreeClassifier, plot_tree, _tree

from sklearn.metrics import log_loss, accuracy_score, classification_report, confusion_matrix, \
                            precision_score, recall_score
                            
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import numpy as np

def deviance(X, y, model):
    return 2 * log_loss(y, model.predict_proba(X), normalize=False)

def print_report(X_shuffled_test, y_shuffled_test, model,pred,file):
    file.write("\n\n Deviance : "+ str(deviance(X_shuffled_test,y_shuffled_test,model)))
    file.write("\n"+ str(classification_report(y_shuffled_test, pred)))
    file.write("\n"+ str(confusion_matrix(y_shuffled_test, pred)))

def shuffle_x_y_selection(data, target_feature):
    X = data.drop(target_feature,axis=1)
    y = data[target_feature]
    print(X.select_dtypes(include=[object]).empty)
    X_shuffled = shuffle(X,random_state=42)
    y_shuffled = shuffle(y,random_state=42)
    return X_shuffled, y_shuffled

def hyper_param_tuning(X_shuffled,y_shuffled,dict_model_config):
    param_dist = {"max_depth": range(dict_model_config["max_depth"][0],dict_model_config["max_depth"][1]),
                "max_features": range(dict_model_config["max_features"][0],dict_model_config["max_features"][1]),
                "min_samples_leaf": range(dict_model_config["min_samples_leaf"][0],dict_model_config["min_samples_leaf"][1]),
                "max_leaf_nodes": range(dict_model_config["max_leaf_nodes"][0],dict_model_config["max_leaf_nodes"][1]),
                "criterion": dict_model_config["criterion"]}

    # Instantiate a Decision Tree classifier: tree
    trees = DecisionTreeClassifier()

    # Instantiate the RandomizedSearchCV object: tree_cv
    tree_cv = RandomizedSearchCV(trees, param_dist, cv=10,random_state=42)
    # Fit it to the data
    tree_cv.fit(X_shuffled,y_shuffled)

    return tree_cv.best_params_

def draw_tree_rules(model,X,png_name):
    plt.figure(figsize=(25,7))
    plot_tree(model,feature_names=X.columns,class_names=["No Scrap","Scrap"],
            rounded=True,
            filled=True,
            fontsize=4,
            impurity=True)
    plt.savefig(png_name, dpi=100)
    plt.clf();


def select_best_params(model,data_shuffled,df):
    n_nodes = model.tree_.node_count
    children_left = model.tree_.children_left
    children_right = model.tree_.children_right
    feature = model.tree_.feature
    threshold = model.tree_.threshold
    
    def find_path(node_numb, path, x):
        path.append(node_numb)
        if node_numb == x:
            return True
        left = False
        right = False
        if (children_left[node_numb] !=-1):
            left = find_path(children_left[node_numb], path, x)
        if (children_right[node_numb] !=-1):
            right = find_path(children_right[node_numb], path, x)
        if left or right :
            return True
        path.remove(node_numb)
        return False


    def get_rule(path, column_names):
        mask = ''
        for index, node in enumerate(path):
            #We check if we are not in the leaf
            if index!=len(path)-1:
                # Do we go under or over the threshold ?
                if (children_left[node] == path[index+1]):
                    mask += "(df['{}']<= {}) \t ".format(column_names[feature[node]], threshold[node])
                else:
                    mask += "(df['{}']> {}) \t ".format(column_names[feature[node]], threshold[node])
        # We insert the & at the right places
        mask = mask.replace("\t", "&", mask.count("\t") - 1)
        mask = mask.replace("\t", "")
        return mask
    leave_id = model.apply(data_shuffled)

    paths ={}
    for leaf in np.unique(leave_id):
        path_leaf = []
        find_path(0, path_leaf, leaf)
        paths[leaf] = np.unique(np.sort(path_leaf))

    rules = {}
    for key in paths:
        rules[key] = get_rule(paths[key], data_shuffled.columns)
        
    dict_rules_best = {}
    for i in rules.keys():
        dict_rules_best[i] = len(df[eval(rules[i])])
    inverse = [(value, key) for key, value in dict_rules_best.items()]
    best_rule = max(inverse)[1]
    return rules, dict_rules_best, best_rule