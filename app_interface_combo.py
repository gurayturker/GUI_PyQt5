# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_interface_combo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recete_form(object):
    def setupUi(self, recete_form):
        recete_form.setObjectName("recete_form")
        recete_form.resize(684, 351)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("maxion_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        recete_form.setWindowIcon(icon)
        self.max_depth_min_text = QtWidgets.QTabWidget(recete_form)
        self.max_depth_min_text.setGeometry(QtCore.QRect(0, -1, 851, 751))
        self.max_depth_min_text.setMaximumSize(QtCore.QSize(851, 751))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_depth_min_text.setFont(font)
        self.max_depth_min_text.setObjectName("max_depth_min_text")
        self.tab_preprocessing = QtWidgets.QWidget()
        self.tab_preprocessing.setObjectName("tab_preprocessing")
        self.select_model_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.select_model_label.setGeometry(QtCore.QRect(50, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.select_model_label.setFont(font)
        self.select_model_label.setObjectName("select_model_label")
        self.max_mould_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.max_mould_label.setGeometry(QtCore.QRect(50, 50, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_mould_label.setFont(font)
        self.max_mould_label.setObjectName("max_mould_label")
        self.tek_essiz_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.tek_essiz_label.setGeometry(QtCore.QRect(50, 80, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tek_essiz_label.setFont(font)
        self.tek_essiz_label.setObjectName("tek_essiz_label")
        self.fazla9999_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.fazla9999_label.setGeometry(QtCore.QRect(50, 110, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fazla9999_label.setFont(font)
        self.fazla9999_label.setObjectName("fazla9999_label")
        self.fazla9999_yuzde_text = QtWidgets.QTextEdit(self.tab_preprocessing)
        self.fazla9999_yuzde_text.setGeometry(QtCore.QRect(600, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fazla9999_yuzde_text.setFont(font)
        self.fazla9999_yuzde_text.setObjectName("fazla9999_yuzde_text")
        self.eksik_veriler_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.eksik_veriler_label.setGeometry(QtCore.QRect(50, 140, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eksik_veriler_label.setFont(font)
        self.eksik_veriler_label.setObjectName("eksik_veriler_label")
        self.anomali_veriler_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.anomali_veriler_label.setGeometry(QtCore.QRect(50, 170, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anomali_veriler_label.setFont(font)
        self.anomali_veriler_label.setObjectName("anomali_veriler_label")
        self.anomali_belirleme_metot_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.anomali_belirleme_metot_label.setGeometry(QtCore.QRect(50, 200, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anomali_belirleme_metot_label.setFont(font)
        self.anomali_belirleme_metot_label.setObjectName("anomali_belirleme_metot_label")
        self.anomali_uygulanacak_etiket_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.anomali_uygulanacak_etiket_label.setGeometry(QtCore.QRect(50, 230, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anomali_uygulanacak_etiket_label.setFont(font)
        self.anomali_uygulanacak_etiket_label.setObjectName("anomali_uygulanacak_etiket_label")
        self.anomali_uygulanacak_oznitelikler_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.anomali_uygulanacak_oznitelikler_label.setGeometry(QtCore.QRect(50, 260, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anomali_uygulanacak_oznitelikler_label.setFont(font)
        self.anomali_uygulanacak_oznitelikler_label.setObjectName("anomali_uygulanacak_oznitelikler_label")
        self.fazla9999_yuzde_label = QtWidgets.QLabel(self.tab_preprocessing)
        self.fazla9999_yuzde_label.setGeometry(QtCore.QRect(530, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fazla9999_yuzde_label.setFont(font)
        self.fazla9999_yuzde_label.setObjectName("fazla9999_yuzde_label")
        self.selected_model_text = QtWidgets.QTextEdit(self.tab_preprocessing)
        self.selected_model_text.setGeometry(QtCore.QRect(400, 20, 71, 21))
        self.selected_model_text.setObjectName("selected_model_text")
        self.max_mould_scrap_text = QtWidgets.QTextEdit(self.tab_preprocessing)
        self.max_mould_scrap_text.setGeometry(QtCore.QRect(400, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_mould_scrap_text.setFont(font)
        self.max_mould_scrap_text.setObjectName("max_mould_scrap_text")
        self.tek_essiz_deger_sil_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.tek_essiz_deger_sil_combo.setGeometry(QtCore.QRect(400, 80, 69, 22))
        self.tek_essiz_deger_sil_combo.setObjectName("tek_essiz_deger_sil_combo")
        self.tek_essiz_deger_sil_combo.addItem("")
        self.tek_essiz_deger_sil_combo.addItem("")
        self.fazla9999_sil_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.fazla9999_sil_combo.setGeometry(QtCore.QRect(400, 110, 69, 22))
        self.fazla9999_sil_combo.setObjectName("fazla9999_sil_combo")
        self.fazla9999_sil_combo.addItem("")
        self.fazla9999_sil_combo.addItem("")
        self.eksik_veriler_sil_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.eksik_veriler_sil_combo.setGeometry(QtCore.QRect(400, 140, 69, 22))
        self.eksik_veriler_sil_combo.setObjectName("eksik_veriler_sil_combo")
        self.eksik_veriler_sil_combo.addItem("")
        self.eksik_veriler_sil_combo.addItem("")
        self.anomali_veriler_sil_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.anomali_veriler_sil_combo.setGeometry(QtCore.QRect(400, 170, 69, 22))
        self.anomali_veriler_sil_combo.setObjectName("anomali_veriler_sil_combo")
        self.anomali_veriler_sil_combo.addItem("")
        self.anomali_veriler_sil_combo.addItem("")
        self.anomali_metot_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.anomali_metot_combo.setGeometry(QtCore.QRect(400, 200, 69, 22))
        self.anomali_metot_combo.setObjectName("anomali_metot_combo")
        self.anomali_metot_combo.addItem("")
        self.anomali_metot_combo.addItem("")
        self.anomali_target_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.anomali_target_combo.setGeometry(QtCore.QRect(400, 230, 69, 22))
        self.anomali_target_combo.setObjectName("anomali_target_combo")
        self.anomali_target_combo.addItem("")
        self.anomali_target_combo.addItem("")
        self.anomali_target_combo.addItem("")
        self.anomaly_scope_combo = QtWidgets.QComboBox(self.tab_preprocessing)
        self.anomaly_scope_combo.setGeometry(QtCore.QRect(400, 260, 69, 22))
        self.anomaly_scope_combo.setObjectName("anomaly_scope_combo")
        self.anomaly_scope_combo.addItem("")
        self.anomaly_scope_combo.addItem("")
        self.max_depth_min_text.addTab(self.tab_preprocessing, "")
        self.tab_model = QtWidgets.QWidget()
        self.tab_model.setObjectName("tab_model")
        self.min_max_depth_text = QtWidgets.QTextEdit(self.tab_model)
        self.min_max_depth_text.setGeometry(QtCore.QRect(230, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.min_max_depth_text.setFont(font)
        self.min_max_depth_text.setObjectName("min_max_depth_text")
        self.max_depth_label = QtWidgets.QLabel(self.tab_model)
        self.max_depth_label.setGeometry(QtCore.QRect(50, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_depth_label.setFont(font)
        self.max_depth_label.setObjectName("max_depth_label")
        self.min_max_features_text = QtWidgets.QTextEdit(self.tab_model)
        self.min_max_features_text.setGeometry(QtCore.QRect(230, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.min_max_features_text.setFont(font)
        self.min_max_features_text.setObjectName("min_max_features_text")
        self.max_features_label = QtWidgets.QLabel(self.tab_model)
        self.max_features_label.setGeometry(QtCore.QRect(50, 50, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_features_label.setFont(font)
        self.max_features_label.setObjectName("max_features_label")
        self.min_min_samples_leaf_text = QtWidgets.QTextEdit(self.tab_model)
        self.min_min_samples_leaf_text.setGeometry(QtCore.QRect(230, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.min_min_samples_leaf_text.setFont(font)
        self.min_min_samples_leaf_text.setObjectName("min_min_samples_leaf_text")
        self.min_samples_leaf_label = QtWidgets.QLabel(self.tab_model)
        self.min_samples_leaf_label.setGeometry(QtCore.QRect(50, 80, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.min_samples_leaf_label.setFont(font)
        self.min_samples_leaf_label.setObjectName("min_samples_leaf_label")
        self.min_max_leaf_nodes_text = QtWidgets.QTextEdit(self.tab_model)
        self.min_max_leaf_nodes_text.setGeometry(QtCore.QRect(230, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.min_max_leaf_nodes_text.setFont(font)
        self.min_max_leaf_nodes_text.setObjectName("min_max_leaf_nodes_text")
        self.max_leaf_nodes_label = QtWidgets.QLabel(self.tab_model)
        self.max_leaf_nodes_label.setGeometry(QtCore.QRect(50, 110, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_leaf_nodes_label.setFont(font)
        self.max_leaf_nodes_label.setObjectName("max_leaf_nodes_label")
        self.max_mould_scrap_text_7 = QtWidgets.QTextEdit(self.tab_model)
        self.max_mould_scrap_text_7.setGeometry(QtCore.QRect(680, 360, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_mould_scrap_text_7.setFont(font)
        self.max_mould_scrap_text_7.setObjectName("max_mould_scrap_text_7")
        self.max_mould_label_7 = QtWidgets.QLabel(self.tab_model)
        self.max_mould_label_7.setGeometry(QtCore.QRect(330, 360, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_mould_label_7.setFont(font)
        self.max_mould_label_7.setObjectName("max_mould_label_7")
        self.criterion_label = QtWidgets.QLabel(self.tab_model)
        self.criterion_label.setGeometry(QtCore.QRect(50, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.criterion_label.setFont(font)
        self.criterion_label.setObjectName("criterion_label")
        self.max_max_depth_text = QtWidgets.QTextEdit(self.tab_model)
        self.max_max_depth_text.setGeometry(QtCore.QRect(320, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_max_depth_text.setFont(font)
        self.max_max_depth_text.setObjectName("max_max_depth_text")
        self.max_max_leaf_nodes_text = QtWidgets.QTextEdit(self.tab_model)
        self.max_max_leaf_nodes_text.setGeometry(QtCore.QRect(320, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_max_leaf_nodes_text.setFont(font)
        self.max_max_leaf_nodes_text.setObjectName("max_max_leaf_nodes_text")
        self.max_min_samples_leaf_text = QtWidgets.QTextEdit(self.tab_model)
        self.max_min_samples_leaf_text.setGeometry(QtCore.QRect(320, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_min_samples_leaf_text.setFont(font)
        self.max_min_samples_leaf_text.setObjectName("max_min_samples_leaf_text")
        self.max_max_features_text = QtWidgets.QTextEdit(self.tab_model)
        self.max_max_features_text.setGeometry(QtCore.QRect(320, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_max_features_text.setFont(font)
        self.max_max_features_text.setObjectName("max_max_features_text")
        self.gini_label = QtWidgets.QLabel(self.tab_model)
        self.gini_label.setGeometry(QtCore.QRect(230, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gini_label.setFont(font)
        self.gini_label.setObjectName("gini_label")
        self.entropy_label = QtWidgets.QLabel(self.tab_model)
        self.entropy_label.setGeometry(QtCore.QRect(320, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entropy_label.setFont(font)
        self.entropy_label.setObjectName("entropy_label")
        self.max_depth_min_text.addTab(self.tab_model, "")
        self.tab_parameters = QtWidgets.QWidget()
        self.tab_parameters.setObjectName("tab_parameters")
        self.olcum_param_label = QtWidgets.QLabel(self.tab_parameters)
        self.olcum_param_label.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.olcum_param_label.setFont(font)
        self.olcum_param_label.setObjectName("olcum_param_label")
        self.tum_param_label = QtWidgets.QLabel(self.tab_parameters)
        self.tum_param_label.setGeometry(QtCore.QRect(20, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tum_param_label.setFont(font)
        self.tum_param_label.setObjectName("tum_param_label")
        self.tum_param_text = QtWidgets.QPlainTextEdit(self.tab_parameters)
        self.tum_param_text.setGeometry(QtCore.QRect(200, 170, 481, 141))
        self.tum_param_text.setObjectName("tum_param_text")
        self.olcum_param_text = QtWidgets.QPlainTextEdit(self.tab_parameters)
        self.olcum_param_text.setGeometry(QtCore.QRect(200, 20, 481, 141))
        self.olcum_param_text.setObjectName("olcum_param_text")
        self.max_depth_min_text.addTab(self.tab_parameters, "")
        self.tab_recete = QtWidgets.QWidget()
        self.tab_recete.setObjectName("tab_recete")
        self.recete_text = QtWidgets.QPlainTextEdit(self.tab_recete)
        self.recete_text.setGeometry(QtCore.QRect(10, 40, 691, 231))
        self.recete_text.setObjectName("recete_text")
        self.recete_uret_button = QtWidgets.QPushButton(self.tab_recete)
        self.recete_uret_button.setGeometry(QtCore.QRect(10, 282, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recete_uret_button.setFont(font)
        self.recete_uret_button.setObjectName("recete_uret_button")
        self.recipe_threshold_text = QtWidgets.QTextEdit(self.tab_recete)
        self.recipe_threshold_text.setGeometry(QtCore.QRect(350, 10, 104, 21))
        self.recipe_threshold_text.setObjectName("recipe_threshold_text")
        self.recipe_thresold_label = QtWidgets.QLabel(self.tab_recete)
        self.recipe_thresold_label.setGeometry(QtCore.QRect(20, 10, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recipe_thresold_label.setFont(font)
        self.recipe_thresold_label.setObjectName("recipe_thresold_label")
        self.max_depth_min_text.addTab(self.tab_recete, "")

        self.retranslateUi(recete_form)
        self.max_depth_min_text.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(recete_form)

    def retranslateUi(self, recete_form):
        _translate = QtCore.QCoreApplication.translate
        recete_form.setWindowTitle(_translate("recete_form", "Re??ete ??retme Uygulamas??"))
        self.select_model_label.setText(_translate("recete_form", "Se??ilen Model"))
        self.max_mould_label.setText(_translate("recete_form", "Maximum Mould Scrap Rate Y??zde(%)"))
        self.tek_essiz_label.setText(_translate("recete_form", "Tek E??siz De??er ????eren ??znitelikler"))
        self.fazla9999_label.setText(_translate("recete_form", "Belirli Bir Orandan Fazla-9999 ????eren ??znitelikler"))
        self.fazla9999_yuzde_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">70</span></p></body></html>"))
        self.eksik_veriler_label.setText(_translate("recete_form", "Eksik Veriler"))
        self.anomali_veriler_label.setText(_translate("recete_form", "Anomali Veriler"))
        self.anomali_belirleme_metot_label.setText(_translate("recete_form", "Anomali Belirleme Methodu"))
        self.anomali_uygulanacak_etiket_label.setText(_translate("recete_form", "Anomali Uygulanacak Etiket"))
        self.anomali_uygulanacak_oznitelikler_label.setText(_translate("recete_form", "Anomali Uygulanacak ??zntilelikler"))
        self.fazla9999_yuzde_label.setText(_translate("recete_form", "Y??zde %"))
        self.selected_model_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">8784</span></p></body></html>"))
        self.max_mould_scrap_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">10</span></p></body></html>"))
        self.tek_essiz_deger_sil_combo.setItemText(0, _translate("recete_form", "Sil"))
        self.tek_essiz_deger_sil_combo.setItemText(1, _translate("recete_form", "Silme"))
        self.fazla9999_sil_combo.setItemText(0, _translate("recete_form", "Sil"))
        self.fazla9999_sil_combo.setItemText(1, _translate("recete_form", "Silme"))
        self.eksik_veriler_sil_combo.setItemText(0, _translate("recete_form", "Sil"))
        self.eksik_veriler_sil_combo.setItemText(1, _translate("recete_form", "Silme"))
        self.anomali_veriler_sil_combo.setItemText(0, _translate("recete_form", "Sil"))
        self.anomali_veriler_sil_combo.setItemText(1, _translate("recete_form", "Silme"))
        self.anomali_metot_combo.setItemText(0, _translate("recete_form", "Sigma"))
        self.anomali_metot_combo.setItemText(1, _translate("recete_form", "Isolation Forest"))
        self.anomali_target_combo.setItemText(0, _translate("recete_form", "Good"))
        self.anomali_target_combo.setItemText(1, _translate("recete_form", "Scrap"))
        self.anomali_target_combo.setItemText(2, _translate("recete_form", "Good + Scrap"))
        self.anomaly_scope_combo.setItemText(0, _translate("recete_form", "S??rekli"))
        self.anomaly_scope_combo.setItemText(1, _translate("recete_form", "S??rekli + Kesikli"))
        self.max_depth_min_text.setTabText(self.max_depth_min_text.indexOf(self.tab_preprocessing), _translate("recete_form", "??n ????leme"))
        self.min_max_depth_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>"))
        self.max_depth_label.setText(_translate("recete_form", "Max Depth"))
        self.min_max_features_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.max_features_label.setText(_translate("recete_form", "Max Features"))
        self.min_min_samples_leaf_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.min_samples_leaf_label.setText(_translate("recete_form", "Min Samples Leaf"))
        self.min_max_leaf_nodes_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.max_leaf_nodes_label.setText(_translate("recete_form", "Max Leaf Nodes"))
        self.max_mould_label_7.setText(_translate("recete_form", "Maximum Mould Scrap Rate Y??zde(%) :"))
        self.criterion_label.setText(_translate("recete_form", "Criterion"))
        self.max_max_depth_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></body></html>"))
        self.max_max_leaf_nodes_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))
        self.max_min_samples_leaf_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))
        self.max_max_features_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></body></html>"))
        self.gini_label.setText(_translate("recete_form", "Gini"))
        self.entropy_label.setText(_translate("recete_form", "Entropy"))
        self.max_depth_min_text.setTabText(self.max_depth_min_text.indexOf(self.tab_model), _translate("recete_form", "Model"))
        self.olcum_param_label.setText(_translate("recete_form", "??l????m Parametreleri"))
        self.tum_param_label.setText(_translate("recete_form", "T??m Parametreler"))
        self.tum_param_text.setPlainText(_translate("recete_form", "\"TC1 SET\", \"TC2 SET\", \"TC3 SET\", \"TC4 SET\", \"TC5 SET\", \"TC6 SET\", \"H1 FLOW SET\", \"H2 SET\", \"H3 SET\", \"H4 SET\", \"H5 SET\", \"H6 SET\", \"H7 SET\", \"H8 SET\", \"H9 SET\", \"H10 SET\", \"H11 SET\", \"H12 SET\", \"H1 COOLING TIME\", \"H2 COOLING TIME\", \"H3 COOLING TIME\", \"H4 COOLING TIME\", \"H5 COOLING TIME\", \"H6 COOLING TIME\", \"H7 COOLING TIME\", \"H8 COOLING TIME\", \"H9 COOLING TIME\", \"H10 COOLING TIME\", \"H11 COOLING TIME\", \"H12 COOLING TIME\", \"H1 WAIT TIME\", \"H2 WAIT TIME\", \"H3 WAIT TIME\", \"H4 WAIT TIME\", \"H5 WAIT TIME\", \"H6 WAIT TIME\", \"H7 WAIT TIME\", \"H8 WAIT TIME\", \"H9 WAIT TIME\", \"H10 WAIT TIME\", \"H11 WAIT TIME\", \"H12 WAIT TIME\", \"S1 FLOW SET\", \"S1.2 FLOW  SET\", \"S1.3 FLOW  SET\", \"S1.4 FLOW  SET\", \"S1.1 FLOW WAIT .TIME\", \"S1.2 FLOW WAIT .TIME\", \"S1.3 FLOW WAIT .TIME\", \"S1.4 FLOW WAIT .TIME\", \"S1.1 COOLING  TIME\", \"S1.2 COOLING TIME\", \"S1.3 COOLING  TIME\", \"S1.4 COOLING  TIME\", \"S2 FLOW SET\", \"S2  FLOW WAIT .TIME\", \"S2  COOLING  TIME\", \"S3  FLOW  SET\", \"S3  FLOW WAIT .TIME\", \"S3 COOLING TIME\", \"PHASE 1 TIME\", \"PHASE 2 TIME\", \"PHASE 3 TIME\", \"PHASE 4 TIME\", \"PHASE 5 TIME\", \"PHASE 6 TIME\", \"PHASE 7 TIME\", \"PHASE 8 TIME\", \"PHASE 1 PRESSURE\", \"PHASE 2 PRESSURE\", \"PHASE 3 PRESSURE\", \"PHASE 4 PRESSURE\", \"PHASE 5 PRESSURE\", \"PHASE 6 PRESSURE\", \"PHASE 7 PRESSURE\", \"PHASE 8 PRESSURE\", \"H1 CONNECTIVITY\", \"H2 CONNECTIVITY\", \"H3 CONNECTIVITY\", \"H4 CONNECTIVITY\", \"H5 CONNECTIVITY\", \"H6 CONNECTIVITY\", \"H7 CONNECTIVITY\", \"H8 CONNECTIVITY\", \"H9 CONNECTIVITY\", \"H10 CONNECTIVITY\", \"H11 CONNECTIVITY\", \"H12 CONNECTIVITY\", \"MAIN  LINE  MINIMUM SET  VALUE PRESSURE  OF AIR AT LPDC\", \"MAIN  LINE MAXIMUM SET  VALUE PRESSURE  OF AIR AT LPDC\", \"METAL TEMPERATURE SET VALUE IN LPDC\", \"scrapflag\""))
        self.olcum_param_text.setPlainText(_translate("recete_form", "\"PId_x\", \"SLNO\", \"MOULD ID\", \"METAL TEMPERATURE ACTUAL VALUE IN LPDC\", \"MAIN AIR  PRESSURE ACTUAL VALUES AT LPDC\", \"MOISTURE ACTUEL  VALUE IN THE  LPDC\", \"ACTUAL  DISTANCE   VALUES OF STROKE ON THE SIDE CORE\", \"MAIN AIR  PRESSURE ACTUAL VALUES\", \"AVERAGE OF H1 FLOW\", \"AVERAGE OF H2 FLOW\", \"AVERAGE OF H3 FLOW\", \"AVERAGE OF H4 FLOW\", \"AVERAGE OF H5 FLOW\", \"AVERAGE OF H6 FLOW\", \"AVERAGE OF H7 FLOW\", \"AVERAGE OF H8 FLOW\", \"AVERAGE OF H9 FLOW\", \"AVERAGE OF H10 FLOW\", \"AVERAGE OF S1.1 FLOW\", \"AVERAGE OF S1.2 FLOW\", \"AVERAGE OF S1.3 FLOW\", \"AVERAGE OF S1.4 FLOW\", \"AVERAGE OF S2 FLOW\", \"AVERAGE OF S3 FLOW\", \"PHASE 1 TIME\", \"PHASE 2 TIME\", \"PHASE 3 TIME\", \"PHASE 4 TIME\", \"PHASE 5 TIME\", \"PHASE 6 TIME\", \"PHASE 7 TIME\", \"PHASE 8 TIME\", \"PHASE 1 PRESSURE\", \"PHASE 2 PRESSURE\", \"PHASE 3 PRESSURE\", \"PHASE 4 PRESSURE\", \"PHASE 5 PRESSURE\", \"PHASE 6 PRESSURE\", \"PHASE 7 PRESSURE\", \"PHASE 8 PRESSURE\", \"H1 WAIT TIME\", \"H2 WAIT TIME\", \"H3 WAIT TIME\", \"H4 WAIT TIME\", \"H5 WAIT TIME\", \"H6 WAIT TIME\", \"H7 WAIT TIME\", \"H8 WAIT TIME\", \"H9 WAIT TIME\", \"H10 WAIT TIME\", \"H11 WAIT TIME\", \"H12 WAIT TIME\", \"H1 COOLING TIME\", \"H2 COOLING TIME\", \"H3 COOLING TIME\", \"H4 COOLING TIME\", \"H5 COOLING TIME\", \"H6 COOLING TIME\", \"H7 COOLING TIME\", \"H8 COOLING TIME\", \"H9 COOLING TIME\", \"H10 COOLING TIME\", \"H11 COOLING TIME\", \"H12 COOLING TIME\", \"S1.1 FLOW WAIT .TIME\", \"S1.1 COOLING  TIME\", \"S1.2 FLOW WAIT .TIME\", \"S1.2 COOLING TIME\", \"S1.3 FLOW WAIT .TIME\", \"S1.3 COOLING  TIME\", \"S1.4 FLOW WAIT .TIME\", \"S1.4 COOLING  TIME\", \"S2  FLOW WAIT .TIME\", \"S2  COOLING  TIME\", \"S3  FLOW WAIT .TIME\", \"S3 COOLING TIME\", \"scrapflag\", \"Mould\", \"Model\", \"EId\", \"ACTUAL MAIN  LINE TEMPERATURE OF WATER\""))
        self.max_depth_min_text.setTabText(self.max_depth_min_text.indexOf(self.tab_parameters), _translate("recete_form", "Parametreler"))
        self.recete_uret_button.setText(_translate("recete_form", "RE??ETE ??RET"))
        self.recipe_threshold_text.setHtml(_translate("recete_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.25</span></p></body></html>"))
        self.recipe_thresold_label.setText(_translate("recete_form", "Scrap Rate Baz Almak ????in E??ik De??eri"))
        self.max_depth_min_text.setTabText(self.max_depth_min_text.indexOf(self.tab_recete), _translate("recete_form", "Re??ete"))
