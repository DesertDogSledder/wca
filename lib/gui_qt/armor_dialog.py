from PyQt5 import QtCore, QtWidgets

from data.equipment import armor
from lib.gui_qt.armor_dialog_ui import Ui_ArmorDialog

try:
    from custom import custom_armor
    custom_armor_loaded = True
except ImportError:
    custom_armor_loaded = False


class ArmorDialog(QtWidgets.QDialog, Ui_ArmorDialog):
    def __init__(self, parent=None):
        super(ArmorDialog, self).__init__(parent)
        self.setupUi(self)

        self.item_cost = 0

        self.quality_info = {'Standard': {'Cost': 'Normal', 'Dice Pool': '-', 'Rarity': 'Common', 'Min Skill': '-',
                                          'Upgrades': '-', 'Soak': '+0'},
                             'High': {'Cost': 'x3 then +100', 'Dice Pool': '+1d6', 'Rarity': 'Uncommon',
                                      'Min Skill': '1 (1d6; proficient)', 'Upgrades': '+1', 'Soak': '+2'},
                             'Exceptional': {'Cost': 'x5 then +250', 'Dice Pool': '+2d6', 'Rarity': 'Rare',
                                             'Min Skill': '3 (2d6; skilled)', 'Upgrades': '+1', 'Soak': '+4'},
                             'Mastercraft': {'Cost': 'x10 then +500', 'Dice Pool': '+3d6', 'Rarity': 'Very Rare',
                                             'Min Skill': '6 (3d6; expert)', 'Upgrades': '+2', 'Soak': '+6'},
                             'Artisanal': {'Cost': 'x100 then +1,000', 'Dice Pool': '+4d6', 'Rarity': 'Very Rare',
                                           'Min Skill': '10 (4d6; mastery)', 'Upgrades': '+2', 'Soak': '+8'},
                             'Legendary': {'Cost': 'x1000 then +2,500', 'Dice Pool': '+5d6', 'Rarity': 'Unique',
                                           'Min Skill': '15 (5d6; authority)', 'Upgrades': '+3', 'Soak': '+10'}}

        self.cb_ar_quality_val.currentIndexChanged.connect(self.on_quality_select)
        self.cb_ar_category.currentIndexChanged.connect(self.on_category_select)
        self.tw_ar_gear.currentItemChanged.connect(self.on_item_select)

        self.tw_ar_gear.sortItems(0, QtCore.Qt.AscendingOrder)
        self.tw_ar_gear.setColumnWidth(0, 250)
        self.tw_ar_gear.setColumnWidth(1, 100)
        self.tw_ar_gear.setColumnWidth(2, 120)
        self.tw_ar_gear.setColumnWidth(3, 60)
        self.tw_ar_gear.setColumnWidth(4, 70)
        self.tw_ar_gear.setColumnWidth(5, 70)
        self.tw_ar_gear.setColumnWidth(6, 100)
        self.tw_ar_gear.setColumnWidth(7, 90)
        self.tw_ar_gear.setColumnWidth(8, 100)
        self.tw_ar_gear.setColumnWidth(9, 100)

        self.category_list = [armor.archaic_armor_list, armor.archaic_shields_list, armor.eastern_armor_list,
                              armor.future_armor_list, armor.future_shields_list]

        if custom_armor_loaded:
            self.category_list.append(custom_armor.custom_armor_list)
            self.cb_ar_category.addItem('Custom Armor')

        self.on_category_select(0)
        self.tw_ar_gear.setCurrentItem(self.tw_ar_gear.topLevelItem(0))
        self.on_quality_select()

    def on_quality_select(self):
        quality = self.cb_ar_quality_val.currentText()
        self.l_ar_dice_pool_val.setText(self.quality_info[quality]['Dice Pool'])
        self.l_ar_rarity_val.setText(self.quality_info[quality]['Rarity'])
        self.l_ar_min_skill_val.setText(self.quality_info[quality]['Min Skill'])
        self.l_ar_upgrades_val.setText(self.quality_info[quality]['Upgrades'])
        self.l_ar_soak_val.setText(self.quality_info[quality]['Soak'])
        self.calc_cost()

    def on_category_select(self, index):
        self.tw_ar_gear.clear()
        twi_list = []
        for item in self.category_list[index]:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(item['Name']))
            twi_list[-1].setText(1, '{}'.format(item['Soak']))
            twi_list[-1].setText(2, '{}'.format(item['Defense']))
            twi_list[-1].setText(3, '{}'.format(item['Cost']))
            twi_list[-1].setText(4, '{}'.format(item['Type']))
            twi_list[-1].setText(5, '{}'.format(item['Weight']))
            twi_list[-1].setText(6, '{}'.format(item['Vulnerable']))
            twi_list[-1].setText(7, '{}'.format(item['Speed']))
            twi_list[-1].setText(8, '{}'.format(item['Special']))

        self.tw_ar_gear.addTopLevelItems(twi_list)
        self.tw_ar_gear.setCurrentItem(self.tw_ar_gear.topLevelItem(0))

    def on_item_select(self, current, previous):
        if current is not None:
            self.calc_cost()

    def calc_cost(self):
        selected_quality = self.cb_ar_quality_val.currentText()
        selected_item = self.tw_ar_gear.currentItem()
        if selected_quality == 'High':
            self.item_cost = (int(selected_item.text(3)) * 3) + 100
        elif selected_quality == 'Exceptional':
            self.item_cost = (int(selected_item.text(3)) * 5) + 250
        elif selected_quality == 'Mastercraft':
            self.item_cost = (int(selected_item.text(3)) * 10) + 500
        elif selected_quality == 'Artisanal':
            self.item_cost = (int(selected_item.text(3)) * 100) + 1000
        elif selected_quality == 'Legendary':
            self.item_cost = (int(selected_item.text(3)) * 1000) + 2500
        else:
            self.item_cost = (int(selected_item.text(3)))

        self.l_ar_cost_val.setText('{}'.format(self.item_cost))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ArmorDialog()
    ui.show()
    sys.exit(app.exec_())
