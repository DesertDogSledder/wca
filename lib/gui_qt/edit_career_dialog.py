from data.careers import *
try:
    from custom import custom_careers
    custom_careers_loaded = True
except ImportError:
    custom_careers_loaded = False
from PyQt5 import QtWidgets
from lib.gui_qt.edit_career_dialog_ui import Ui_EditCareerDialog


class EditCareerDialog(QtWidgets.QDialog, Ui_EditCareerDialog):
    def __init__(self, parent=None):
        super(EditCareerDialog, self).__init__(parent)
        self.setupUi(self)

        if not custom_careers_loaded:
            self.rb_ecd_custom.setEnabled(False)

        self.career_list = []
        self.career_source = ''

        self.rb_ecd_origins.toggled.connect(self.on_source_select)
        self.rb_ecd_old.toggled.connect(self.on_source_select)
        self.rb_ecd_now.toggled.connect(self.on_source_select)
        self.rb_ecd_new.toggled.connect(self.on_source_select)
        self.rb_ecd_martial_arts.toggled.connect(self.on_source_select)
        self.rb_ecd_custom.toggled.connect(self.on_source_select)

        self.lw_ecd_careers_val.currentRowChanged.connect(self.on_career_select)
        self.lw_ecd_exploits_val.currentRowChanged.connect(self.on_exploit_select)

        self.rb_ecd_origins.setChecked(True)
        self.on_source_select(True)

    def on_source_select(self, checked):
        # Check if checked is True so this code isn't fully executed twice
        if checked:
            if self.rb_ecd_origins.isChecked():
                self.career_list = origins.career_woin_origin_list
                self.career_source = 'origins'
            elif self.rb_ecd_old.isChecked():
                self.career_list = careers_old.career_old_list
                self.career_source = 'old'
            elif self.rb_ecd_now.isChecked():
                self.career_list = careers_now.career_now_list
                self.career_source = 'now'
            elif self.rb_ecd_new.isChecked():
                self.career_list = careers_new.career_new_list
                self.career_source = 'new'
            elif self.rb_ecd_martial_arts.isChecked():
                self.career_list = careers_martial_arts.career_ma_list
                self.career_source = 'martial arts'
            elif self.rb_ecd_custom.isChecked():
                self.career_list = custom_careers.custom_career_list
                self.career_source = 'custom'

        self.lw_ecd_careers_val.clear()
        for career in self.career_list:
            self.lw_ecd_careers_val.addItem(career.name)

        self.lw_ecd_careers_val.setCurrentRow(0)
        self.on_career_select(0)

    def on_career_select(self, current_row):
        if current_row != -1:
            selected_career = self.career_list[current_row]
            self.pte_ecd_career_desc.setPlainText('Prerequisites: {}\n\n{}'.format(selected_career.prereq,
                                                                                   selected_career.desc))

            available_skills_str = ''
            for skill in selected_career.available_skills:
                available_skills_str += '{}, '.format(skill)
            self.pte_ecd_available_skills.setPlainText(available_skills_str[:-2])

            self.lw_ecd_exploits_val.clear()
            for exploit in selected_career.available_exploits:
                self.lw_ecd_exploits_val.addItem(exploit['Name'])

            self.sb_ecd_str_val.setValue(selected_career.stats['STR'])
            self.sb_ecd_agi_val.setValue(selected_career.stats['AGI'])
            self.sb_ecd_end_val.setValue(selected_career.stats['END'])
            self.sb_ecd_int_val.setValue(selected_career.stats['INT'])
            self.sb_ecd_log_val.setValue(selected_career.stats['LOG'])
            self.sb_ecd_wil_val.setValue(selected_career.stats['WIL'])
            self.sb_ecd_cha_val.setValue(selected_career.stats['CHA'])
            self.sb_ecd_luc_val.setValue(selected_career.stats['LUC'])
            self.sb_ecd_rep_val.setValue(selected_career.stats['REP'])
            self.sb_ecd_mag_val.setValue(selected_career.stats['MAG'])
            self.sb_ecd_chi_val.setValue(selected_career.stats['CHI'])
            self.sb_ecd_psi_val.setValue(selected_career.stats['PSI'])

            self.lw_ecd_exploits_val.setCurrentRow(0)
            self.on_exploit_select(0)

    def on_exploit_select(self, current_row):
        if current_row != -1:
            selected_career = self.career_list[self.lw_ecd_careers_val.currentRow()]
            selected_exploit = current_row
            self.pte_ecd_exploit_desc.setPlainText(selected_career.available_exploits[selected_exploit]['Desc'])

