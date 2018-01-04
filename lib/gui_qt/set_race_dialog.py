from data.races import *
try:
    from custom import custom_races
    custom_races_loaded = True
except ImportError:
    custom_races_loaded = False
from PyQt5 import QtWidgets
from lib.gui_qt.set_race_dialog_ui import Ui_SetRaceDialog


class SetRaceDialog(QtWidgets.QDialog, Ui_SetRaceDialog):
    def __init__(self, parent=None):
        super(SetRaceDialog, self).__init__(parent)
        self.setupUi(self)

        if not custom_races_loaded:
            self.rb_srd_custom.setEnabled(False)

        self.race_list = []

        self.rb_srd_old.toggled.connect(self.on_source_select)
        self.rb_srd_now.toggled.connect(self.on_source_select)
        self.rb_srd_new.toggled.connect(self.on_source_select)
        self.rb_srd_custom.toggled.connect(self.on_source_select)

        self.lw_srd_races_val.currentRowChanged.connect(self.on_race_select)
        self.lw_srd_exploits_val.currentRowChanged.connect(self.on_exploit_select)

        self.rb_srd_old.setChecked(True)
        self.on_source_select(True)
        self.race_source = ''

    def on_source_select(self, checked):
        # Check if checked is True so this code isn't fully executed twice
        if checked:
            if self.rb_srd_old.isChecked():
                self.race_list = races_old.race_old_list
                self.race_source = 'old'
            elif self.rb_srd_now.isChecked():
                self.race_list = races_now.race_now_list
                self.race_source = 'now'
            elif self.rb_srd_new.isChecked():
                self.race_list = races_new.race_new_list
                self.race_source = 'new'
            elif self.rb_srd_custom.isChecked():
                self.race_list = custom_races.custom_race_list
                self.race_source = 'custom'

        self.lw_srd_races_val.clear()
        for race in self.race_list:
            self.lw_srd_races_val.addItem(race.name)

        self.lw_srd_races_val.setCurrentRow(0)
        self.on_race_select(0)

    def on_race_select(self, current_row):
        if current_row != -1:
            selected_race = self.race_list[current_row]

            self.pte_srd_race_desc.setPlainText(selected_race.desc)

            skill_list = ''
            for skill in selected_race.available_skills:
                skill_list += '{}, '.format(skill)
            self.pte_srd_skills.setPlainText(skill_list[:-2])

            self.lw_srd_exploits_val.clear()
            for exploit in selected_race.exploits:
                self.lw_srd_exploits_val.addItem(exploit['Name'])

            self.sb_srd_str_val.setValue(selected_race.stats['STR'])
            self.sb_srd_agi_val.setValue(selected_race.stats['AGI'])
            self.sb_srd_end_val.setValue(selected_race.stats['END'])
            self.sb_srd_int_val.setValue(selected_race.stats['INT'])
            self.sb_srd_log_val.setValue(selected_race.stats['LOG'])
            self.sb_srd_wil_val.setValue(selected_race.stats['WIL'])
            self.sb_srd_cha_val.setValue(selected_race.stats['CHA'])
            self.sb_srd_luc_val.setValue(selected_race.stats['LUC'])
            self.sb_srd_rep_val.setValue(selected_race.stats['REP'])
            self.sb_srd_mag_val.setValue(selected_race.stats['MAG'])
            self.sb_srd_chi_val.setValue(selected_race.stats['CHI'])
            self.sb_srd_psi_val.setValue(selected_race.stats['PSI'])

            self.lw_srd_exploits_val.setCurrentRow(0)
            self.on_exploit_select(0)

    def on_exploit_select(self, current_row):
        if current_row != -1:
            selected_race = self.race_list[self.lw_srd_races_val.currentRow()]
            selected_exploit = current_row
            self.pte_srd_exploit_desc.setPlainText(selected_race.exploits[selected_exploit]['Desc'])


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SetRaceDialog()
    ui.show()
    sys.exit(app.exec_())
