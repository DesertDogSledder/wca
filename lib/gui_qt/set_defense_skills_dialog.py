from PyQt5 import QtWidgets

from lib.gui_qt.set_defense_skills_dialog_ui import Ui_SetDefenseSkillsDialog


class SetDefenseSkillsDialog(QtWidgets.QDialog, Ui_SetDefenseSkillsDialog):
    def __init__(self, parent=None):
        super(SetDefenseSkillsDialog, self).__init__(parent)
        self.setupUi(self)