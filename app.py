import sys
from app_interface_combo import *
from main_functions.main import run

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_recete_form()
        self.ui.setupUi(self)
        self.ui.recete_uret_button.clicked.connect(self.take_model)

    def take_model(self):
        # Ön İşleme
        dict_preprocess_config = dict()
        print("Ön İşleme Parametreleri Belirlendi")
        dict_preprocess_config["selected_model"] = int(self.ui.selected_model_text.toPlainText())
        dict_preprocess_config["max_mould_percentage"] = int(self.ui.max_mould_scrap_text.toPlainText())
        dict_preprocess_config["drop_feature_including_one"] = self.ui.tek_essiz_deger_sil_combo.currentText()
        dict_preprocess_config["drop_feature_including_over_percentage_9999"] = self.ui.fazla9999_sil_combo.currentText()
        dict_preprocess_config["percentage_value"] = int(self.ui.fazla9999_yuzde_text.toPlainText())
        dict_preprocess_config["drop_missing_values"] = self.ui.eksik_veriler_sil_combo.currentText()
        dict_preprocess_config["drop_anomalies"] = self.ui.anomali_veriler_sil_combo.currentText()
        dict_preprocess_config["anomaly_method"] = self.ui.anomali_metot_combo.currentText()
        dict_preprocess_config["anomaly_target_values"] = self.ui.anomali_target_combo.currentText()
        dict_preprocess_config["anomaly_scope"] = self.ui.anomaly_scope_combo.currentText()
        dict_preprocess_config["recipe_threshold"] = float(self.ui.recipe_threshold_text.toPlainText())
        # Hiper Parametre
        dict_model_config = dict()
        dict_model_config["max_depth"] = [int(self.ui.min_max_depth_text.toPlainText()),
                                   int(self.ui.max_max_depth_text.toPlainText())]
        dict_model_config["max_features"] = [int(self.ui.min_max_features_text.toPlainText()),
                                      int(self.ui.max_max_features_text.toPlainText())]
        dict_model_config["min_samples_leaf"] = [int(self.ui.min_min_samples_leaf_text.toPlainText()),
                                          int(self.ui.max_min_samples_leaf_text.toPlainText())]
        dict_model_config["max_leaf_nodes"] = [int(self.ui.min_max_leaf_nodes_text.toPlainText()),
                                        int(self.ui.max_max_leaf_nodes_text.toPlainText())]
        dict_model_config["criterion"] = ["gini", "entropy"]
        print(dict_preprocess_config)
        print(dict_model_config)
        try:
            run("arayüz_run1", dict_preprocess_config, dict_model_config)
            print("Reçete Üretildi.")
        except Exception as e:
            print("Run'da Hata")
            print(e)

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
