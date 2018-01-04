# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\QtUI\set_defense_skills_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_SetDefenseSkillsDialog(object):
    def setupUi(self, SetDefenseSkillsDialog):
        SetDefenseSkillsDialog.setObjectName("SetDefenseSkillsDialog")
        SetDefenseSkillsDialog.resize(813, 300)
        self.vl_sdsd_dialog = QtWidgets.QVBoxLayout(SetDefenseSkillsDialog)
        self.vl_sdsd_dialog.setObjectName("vl_sdsd_dialog")
        self.l_sdsd_info = QtWidgets.QLabel(SetDefenseSkillsDialog)
        self.l_sdsd_info.setObjectName("l_sdsd_info")
        self.vl_sdsd_dialog.addWidget(self.l_sdsd_info)
        self.hl_sdsd_defenses = QtWidgets.QHBoxLayout()
        self.hl_sdsd_defenses.setObjectName("hl_sdsd_defenses")
        self.gb_sdsd_melee = QtWidgets.QGroupBox(SetDefenseSkillsDialog)
        self.gb_sdsd_melee.setObjectName("gb_sdsd_melee")
        self.vl_sdsd_melee = QtWidgets.QVBoxLayout(self.gb_sdsd_melee)
        self.vl_sdsd_melee.setObjectName("vl_sdsd_melee")
        self.cb_sdsd_melee_val = QtWidgets.QComboBox(self.gb_sdsd_melee)
        self.cb_sdsd_melee_val.setObjectName("cb_sdsd_melee_val")
        self.vl_sdsd_melee.addWidget(self.cb_sdsd_melee_val)
        self.hl_sdsd_defenses.addWidget(self.gb_sdsd_melee)
        self.gb_sdsd_ranged = QtWidgets.QGroupBox(SetDefenseSkillsDialog)
        self.gb_sdsd_ranged.setObjectName("gb_sdsd_ranged")
        self.vl_sdsd_ranged = QtWidgets.QVBoxLayout(self.gb_sdsd_ranged)
        self.vl_sdsd_ranged.setObjectName("vl_sdsd_ranged")
        self.cb_sdsd_ranged_val = QtWidgets.QComboBox(self.gb_sdsd_ranged)
        self.cb_sdsd_ranged_val.setObjectName("cb_sdsd_ranged_val")
        self.vl_sdsd_ranged.addWidget(self.cb_sdsd_ranged_val)
        self.hl_sdsd_defenses.addWidget(self.gb_sdsd_ranged)
        self.gb_sdsd_mental = QtWidgets.QGroupBox(SetDefenseSkillsDialog)
        self.gb_sdsd_mental.setObjectName("gb_sdsd_mental")
        self.vl_sdsd_mental = QtWidgets.QVBoxLayout(self.gb_sdsd_mental)
        self.vl_sdsd_mental.setObjectName("vl_sdsd_mental")
        self.cb_sdsd_mental_val = QtWidgets.QComboBox(self.gb_sdsd_mental)
        self.cb_sdsd_mental_val.setObjectName("cb_sdsd_mental_val")
        self.vl_sdsd_mental.addWidget(self.cb_sdsd_mental_val)
        self.hl_sdsd_defenses.addWidget(self.gb_sdsd_mental)
        self.gb_sdsd_vital = QtWidgets.QGroupBox(SetDefenseSkillsDialog)
        self.gb_sdsd_vital.setObjectName("gb_sdsd_vital")
        self.vl_sdsd_vital = QtWidgets.QVBoxLayout(self.gb_sdsd_vital)
        self.vl_sdsd_vital.setObjectName("vl_sdsd_vital")
        self.cb_sdsd_vital_val = QtWidgets.QComboBox(self.gb_sdsd_vital)
        self.cb_sdsd_vital_val.setObjectName("cb_sdsd_vital_val")
        self.vl_sdsd_vital.addWidget(self.cb_sdsd_vital_val)
        self.hl_sdsd_defenses.addWidget(self.gb_sdsd_vital)
        self.vl_sdsd_dialog.addLayout(self.hl_sdsd_defenses)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetDefenseSkillsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vl_sdsd_dialog.addWidget(self.buttonBox)

        self.retranslateUi(SetDefenseSkillsDialog)
        self.buttonBox.accepted.connect(SetDefenseSkillsDialog.accept)
        self.buttonBox.rejected.connect(SetDefenseSkillsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDefenseSkillsDialog)

    def retranslateUi(self, SetDefenseSkillsDialog):
        _translate = QtCore.QCoreApplication.translate
        SetDefenseSkillsDialog.setWindowTitle(_translate("SetDefenseSkillsDialog", "Set Defense Skills - WOIN Character Assistant"))
        self.l_sdsd_info.setText(_translate("SetDefenseSkillsDialog", "<html><head/><body><p>For <span style=\" font-weight:600;\">MELEE</span> and <span style=\" font-weight:600;\">RANGED DEFENSE</span>, you may use <span style=\" font-style:italic;\">acrobatics</span>, <span style=\" font-style:italic;\">dodging</span>, or <span style=\" font-style:italic;\">foresight</span>.</p><p>For <span style=\" font-weight:600;\">MENTAL DEFENSE</span> you may use <span style=\" font-style:italic;\">concentration</span>, <span style=\" font-style:italic;\">meditation</span>, <span style=\" font-style:italic;\">bravery</span>, <span style=\" font-style:italic;\">discipline</span>, <span style=\" font-style:italic;\">religion</span>, <span style=\" font-style:italic;\">conviction</span>, <span style=\" font-style:italic;\">leadership</span>, <span style=\" font-style:italic;\">psychology</span>, or <span style=\" font-style:italic;\">rulership</span>.</p><p>For <span style=\" font-weight:600;\">VITAL DEFENSE</span> you may use <span style=\" font-style:italic;\">resistance</span>.</p><p>Skill with a melee weapon or unarmed combat applies to <span style=\" font-weight:600;\">MELEE DEFENSE</span>, but not ranged attacks.</p></body></html>"))
        self.gb_sdsd_melee.setTitle(_translate("SetDefenseSkillsDialog", "Melee Defense"))
        self.gb_sdsd_ranged.setTitle(_translate("SetDefenseSkillsDialog", "Ranged Defense"))
        self.gb_sdsd_mental.setTitle(_translate("SetDefenseSkillsDialog", "Mental Defense"))
        self.gb_sdsd_vital.setTitle(_translate("SetDefenseSkillsDialog", "Vital Defense"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetDefenseSkillsDialog = QtWidgets.QDialog()
    ui = Ui_SetDefenseSkillsDialog()
    ui.setupUi(SetDefenseSkillsDialog)
    SetDefenseSkillsDialog.show()
    sys.exit(app.exec_())

