from PyQt5 import QtCore, QtWidgets

from data.equipment import general_gear
from lib.gui_qt.general_gear_dialog_ui import Ui_GeneralGearDialog

try:
    from custom import custom_general_gear
    custom_general_gear_loaded = True
except ImportError:
    custom_general_gear_loaded = False


class GeneralGearDialog(QtWidgets.QDialog, Ui_GeneralGearDialog):
    def __init__(self, parent=None):
        super(GeneralGearDialog, self).__init__(parent)
        self.setupUi(self)

        self.cb_ggd_category.currentIndexChanged.connect(self.on_category_select)

        self.tw_ggd_gear.sortItems(0, QtCore.Qt.AscendingOrder)
        self.tw_ggd_gear.setColumnWidth(0, 250)

        self.category_list = [general_gear.general_gear_list]

        if custom_general_gear_loaded:
            self.category_list.append(custom_general_gear.custom_general_gear_list)
            self.cb_ggd_category.addItem('Custom General Gear')

        self.on_category_select(0)

    def on_category_select(self, index):
        self.tw_ggd_gear.clear()
        twi_list = []
        for item in self.category_list[index]:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(item['Name']))
            twi_list[-1].setText(1, '{}'.format(str(item['Cost'])))
            twi_list[-1].setText(2, '{}'.format(item['Weight']))
            twi_list[-1].setText(3, '{}{}'.format(item['Tech Level'], item['Genre']))

        self.tw_ggd_gear.addTopLevelItems(twi_list)
        self.tw_ggd_gear.setCurrentItem(self.tw_ggd_gear.topLevelItem(0))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = GeneralGearDialog()
    ui.show()
    sys.exit(app.exec_())
