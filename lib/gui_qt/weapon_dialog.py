from PyQt5 import QtCore, QtWidgets

from data.equipment import weapons
from lib.gui_qt.weapon_dialog_ui import Ui_WeaponDialog

try:
    from custom import custom_weapons
    custom_weapons_loaded = True
except ImportError:
    custom_weapons_loaded = False


class WeaponDialog(QtWidgets.QDialog, Ui_WeaponDialog):
    def __init__(self, parent=None):
        super(WeaponDialog, self).__init__(parent)
        self.setupUi(self)

        self.item_cost = 0

        self.quality_info = {'Standard': {'Cost': 'Normal', 'Dice Pool': '-', 'Rarity': 'Common', 'Min Skill': '-',
                                          'Upgrades': '-'},
                             'High': {'Cost': 'x3 then +100', 'Dice Pool': '+1d6', 'Rarity': 'Uncommon',
                                      'Min Skill': '1 (1d6; proficient)', 'Upgrades': '+1'},
                             'Exceptional': {'Cost': 'x5 then +250', 'Dice Pool': '+2d6', 'Rarity': 'Rare',
                                             'Min Skill': '3 (2d6; skilled)', 'Upgrades': '+1'},
                             'Mastercraft': {'Cost': 'x10 then +500', 'Dice Pool': '+3d6', 'Rarity': 'Very Rare',
                                             'Min Skill': '6 (3d6; expert)', 'Upgrades': '+2'},
                             'Artisanal': {'Cost': 'x100 then +1,000', 'Dice Pool': '+4d6', 'Rarity': 'Very Rare',
                                           'Min Skill': '10 (4d6; mastery)', 'Upgrades': '+2'},
                             'Legendary': {'Cost': 'x1000 then +2,500', 'Dice Pool': '+5d6', 'Rarity': 'Unique',
                                           'Min Skill': '15 (5d6; authority)', 'Upgrades': '+3'}}

        self.cb_wd_quality_val.currentIndexChanged.connect(self.on_quality_select)
        self.cb_wd_category.currentIndexChanged.connect(self.on_category_select)
        self.tw_wd_gear.currentItemChanged.connect(self.on_item_select)

        self.tw_wd_gear.sortItems(0, QtCore.Qt.AscendingOrder)
        self.tw_wd_gear.setColumnWidth(0, 250)
        self.tw_wd_gear.setColumnWidth(1, 100)
        self.tw_wd_gear.setColumnWidth(2, 120)
        self.tw_wd_gear.setColumnWidth(3, 60)
        self.tw_wd_gear.setColumnWidth(4, 70)
        self.tw_wd_gear.setColumnWidth(5, 70)
        self.tw_wd_gear.setColumnWidth(6, 100)
        self.tw_wd_gear.setColumnWidth(7, 90)
        self.tw_wd_gear.setColumnWidth(8, 100)
        self.tw_wd_gear.setColumnWidth(9, 100)

        self.category_list = [weapons.archaic_axes_list, weapons.archaic_gunpowder_list, weapons.archaic_misc_list,
                              weapons.archaic_polearm_list, weapons.archaic_ranged_list, weapons.archaic_swords_list,
                              weapons.eastern_melee_list, weapons.future_explosive_ordnance_list,
                              weapons.future_exotic_ranged_list, weapons.future_exotic_melee_list,
                              weapons.future_ranged_list, weapons.future_melee_list, weapons.laser_swords_list,
                              weapons.modern_firearms_list, weapons.western_handguns_list,
                              weapons.western_longarms_list, weapons.ww2_firearms_list]

        if custom_weapons_loaded:
            self.category_list.append(custom_weapons.custom_weapons_list)
            self.cb_wd_category.addItem('Custom Weapons')

        self.on_category_select(0)
        self.tw_wd_gear.setCurrentItem(self.tw_wd_gear.topLevelItem(0))
        self.on_quality_select()

    def on_quality_select(self):
        quality = self.cb_wd_quality_val.currentText()
        self.l_wd_dice_pool_val.setText(self.quality_info[quality]['Dice Pool'])
        self.l_wd_rarity_val.setText(self.quality_info[quality]['Rarity'])
        self.l_wd_min_skill_val.setText(self.quality_info[quality]['Min Skill'])
        self.l_wd_upgrades_val.setText(self.quality_info[quality]['Upgrades'])
        self.calc_cost()

    def on_category_select(self, index):
        self.tw_wd_gear.clear()
        twi_list = []
        for item in self.category_list[index]:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(item['Name']))
            twi_list[-1].setText(1, '{}'.format(item['Damage']))
            type_str = ''
            for type in item['Type']:
                type_str += '{}, '.format(type)
            twi_list[-1].setText(2, '{}'.format(type_str[:-2]))
            twi_list[-1].setText(3, '{}'.format(item['Range']))
            twi_list[-1].setText(4, '{}'.format(item['Cost']))
            twi_list[-1].setText(5, '{}'.format(item['Size']))
            twi_list[-1].setText(6, '{}'.format(item['Weight']))
            twi_list[-1].setText(7, '{}{}'.format(item['Tech Level'], item['Genre']))
            twi_list[-1].setText(8, '{}'.format(item['Special']))

        self.tw_wd_gear.addTopLevelItems(twi_list)
        self.tw_wd_gear.setCurrentItem(self.tw_wd_gear.topLevelItem(0))

    def on_item_select(self, current, previous):
        if current is not None:
            self.calc_cost()

    def calc_cost(self):
        selected_quality = self.cb_wd_quality_val.currentText()
        selected_item = self.tw_wd_gear.currentItem()
        if selected_quality == 'High':
            self.item_cost = (int(selected_item.text(4)) * 3) + 100
        elif selected_quality == 'Exceptional':
            self.item_cost = (int(selected_item.text(4)) * 5) + 250
        elif selected_quality == 'Mastercraft':
            self.item_cost = (int(selected_item.text(4)) * 10) + 500
        elif selected_quality == 'Artisanal':
            self.item_cost = (int(selected_item.text(4)) * 100) + 1000
        elif selected_quality == 'Legendary':
            self.item_cost = (int(selected_item.text(4)) * 1000) + 2500
        else:
            self.item_cost = (int(selected_item.text(4)))

        self.l_wd_cost_val.setText('{}'.format(self.item_cost))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = WeaponDialog()
    ui.show()
    sys.exit(app.exec_())
