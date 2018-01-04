from data.homeworlds import *
try:
    from custom import custom_homeworlds
    custom_homeworlds_loaded = True
except ImportError:
    custom_homeworlds_loaded = False
from PyQt5 import QtWidgets
from lib.gui_qt.set_homeworld_dialog_ui import Ui_SetHomeworldDialog


class SetHomeworldDialog(QtWidgets.QDialog, Ui_SetHomeworldDialog):
    def __init__(self, parent=None):
        super(SetHomeworldDialog, self).__init__(parent)
        self.setupUi(self)

        if not custom_homeworlds_loaded:
            self.rb_shd_custom.setEnabled(False)

        self.rb_shd_new.toggled.connect(self.on_source_select)
        self.rb_shd_custom.toggled.connect(self.on_source_select)
        self.lw_shd_homeworlds_val.itemSelectionChanged.connect(self.on_homeworld_select)

        self.homeworld_list = []
        self.homeworld_source = ''

        self.rb_shd_new.setChecked(True)
        self.on_source_select(True)

    def on_source_select(self, checked):
        # Check if checked is True so this code isn't fully executed twice
        if checked:
            if self.rb_shd_new.isChecked():
                self.homeworld_list = homeworlds_new.homeworld_new_list
                self.homeworld_source = 'new'
            elif self.rb_shd_custom.isChecked():
                self.homeworld_list = custom_homeworlds.custom_homeworld_list
                self.homeworld_list = 'custom'

        self.lw_shd_homeworlds_val.clear()
        for homeworld in self.homeworld_list:
            self.lw_shd_homeworlds_val.addItem(homeworld.name)

        self.lw_shd_homeworlds_val.setCurrentRow(0)
        self.on_homeworld_select()
            
    def on_homeworld_select(self):
        selected_homeworld = self.homeworld_list[self.lw_shd_homeworlds_val.currentRow()]

        available_skills_str = ''
        for skill in selected_homeworld.available_skills:
            available_skills_str += '{}, '.format(skill)
        self.pte_shd_skills.setPlainText(available_skills_str[:-2])

        self.sb_shd_str_val.setValue(selected_homeworld.stats['STR'])
        self.sb_shd_agi_val.setValue(selected_homeworld.stats['AGI'])
        self.sb_shd_end_val.setValue(selected_homeworld.stats['END'])
        self.sb_shd_int_val.setValue(selected_homeworld.stats['INT'])
        self.sb_shd_log_val.setValue(selected_homeworld.stats['LOG'])
        self.sb_shd_wil_val.setValue(selected_homeworld.stats['WIL'])
        self.sb_shd_cha_val.setValue(selected_homeworld.stats['CHA'])
        self.sb_shd_luc_val.setValue(selected_homeworld.stats['LUC'])
        self.sb_shd_rep_val.setValue(selected_homeworld.stats['REP'])
        self.sb_shd_mag_val.setValue(selected_homeworld.stats['MAG'])
        self.sb_shd_chi_val.setValue(selected_homeworld.stats['CHI'])
        self.sb_shd_psi_val.setValue(selected_homeworld.stats['PSI'])

