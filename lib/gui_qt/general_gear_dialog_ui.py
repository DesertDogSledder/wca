# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\QtUI\general_gear_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_GeneralGearDialog(object):
    def setupUi(self, GeneralGearDialog):
        GeneralGearDialog.setObjectName("GeneralGearDialog")
        GeneralGearDialog.resize(678, 566)
        self.vl_ggd_main = QtWidgets.QVBoxLayout(GeneralGearDialog)
        self.vl_ggd_main.setObjectName("vl_ggd_main")
        self.cb_ggd_category = QtWidgets.QComboBox(GeneralGearDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_ggd_category.sizePolicy().hasHeightForWidth())
        self.cb_ggd_category.setSizePolicy(sizePolicy)
        self.cb_ggd_category.setObjectName("cb_ggd_category")
        self.cb_ggd_category.addItem("")
        self.vl_ggd_main.addWidget(self.cb_ggd_category)
        self.tw_ggd_gear = QtWidgets.QTreeWidget(GeneralGearDialog)
        self.tw_ggd_gear.setAnimated(False)
        self.tw_ggd_gear.setHeaderHidden(False)
        self.tw_ggd_gear.setColumnCount(4)
        self.tw_ggd_gear.setObjectName("tw_ggd_gear")
        self.vl_ggd_main.addWidget(self.tw_ggd_gear)
        self.fl_ggd_quantity = QtWidgets.QFormLayout()
        self.fl_ggd_quantity.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.fl_ggd_quantity.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fl_ggd_quantity.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fl_ggd_quantity.setObjectName("fl_ggd_quantity")
        self.l_ggd_quantity = QtWidgets.QLabel(GeneralGearDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_ggd_quantity.sizePolicy().hasHeightForWidth())
        self.l_ggd_quantity.setSizePolicy(sizePolicy)
        self.l_ggd_quantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_ggd_quantity.setObjectName("l_ggd_quantity")
        self.fl_ggd_quantity.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_ggd_quantity)
        self.sb_ggd_quantity_val = QtWidgets.QSpinBox(GeneralGearDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_ggd_quantity_val.sizePolicy().hasHeightForWidth())
        self.sb_ggd_quantity_val.setSizePolicy(sizePolicy)
        self.sb_ggd_quantity_val.setMinimum(1)
        self.sb_ggd_quantity_val.setObjectName("sb_ggd_quantity_val")
        self.fl_ggd_quantity.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sb_ggd_quantity_val)
        self.vl_ggd_main.addLayout(self.fl_ggd_quantity)
        self.buttonBox = QtWidgets.QDialogButtonBox(GeneralGearDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.vl_ggd_main.addWidget(self.buttonBox)

        self.retranslateUi(GeneralGearDialog)
        self.buttonBox.accepted.connect(GeneralGearDialog.accept)
        self.buttonBox.rejected.connect(GeneralGearDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GeneralGearDialog)

    def retranslateUi(self, GeneralGearDialog):
        _translate = QtCore.QCoreApplication.translate
        GeneralGearDialog.setWindowTitle(_translate("GeneralGearDialog", "General Gear - WOIN Character Assistant"))
        self.cb_ggd_category.setItemText(0, _translate("GeneralGearDialog", "Base Gear"))
        self.tw_ggd_gear.setSortingEnabled(True)
        self.tw_ggd_gear.headerItem().setText(0, _translate("GeneralGearDialog", "Name"))
        self.tw_ggd_gear.headerItem().setText(1, _translate("GeneralGearDialog", "Cost"))
        self.tw_ggd_gear.headerItem().setText(2, _translate("GeneralGearDialog", "Weight"))
        self.tw_ggd_gear.headerItem().setText(3, _translate("GeneralGearDialog", "Availability"))
        self.l_ggd_quantity.setText(_translate("GeneralGearDialog", "Quantity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeneralGearDialog = QtWidgets.QDialog()
    ui = Ui_GeneralGearDialog()
    ui.setupUi(GeneralGearDialog)
    GeneralGearDialog.show()
    sys.exit(app.exec_())

