from PyQt5 import QtWidgets

from data.exploits import exploits_traits
from lib.gui_qt.set_trait_dialog_ui import Ui_SetTraitDialog


class SetTraitDialog(QtWidgets.QDialog, Ui_SetTraitDialog):
    def __init__(self, parent=None):
        super(SetTraitDialog, self).__init__(parent)
        self.setupUi(self)

        self.trait_list = exploits_traits.exploit_traits_list

        for trait in self.trait_list:
            self.lw_std_traits.addItem(trait['Name'])

        self.lw_std_traits.setCurrentRow(0)
        self.on_trait_select()

        self.lw_std_traits.itemClicked.connect(self.on_trait_select)

    def on_trait_select(self):
        trait_index = self.lw_std_traits.currentRow()
        self.pte_std_traits_desc.setPlainText('{}'.format(exploits_traits.exploit_traits_list[trait_index]['Desc']))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SetTraitDialog()
    ui.show()
    sys.exit(app.exec_())
