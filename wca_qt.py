import collections
import copy
import pickle
import re
import sys

from PyQt5 import QtCore, QtWidgets

from data.homeworlds import *
from data.races import *
from lib import dice, character
from lib.generate_character_sheet import generate_character_sheet
from lib.gui_qt.armor_dialog import ArmorDialog
from lib.gui_qt.edit_career_dialog import EditCareerDialog
from lib.gui_qt.exploit_dialog import ExploitDialog
from lib.gui_qt.general_gear_dialog import GeneralGearDialog
from lib.gui_qt.set_defense_skills_dialog import SetDefenseSkillsDialog
from lib.gui_qt.set_homeworld_dialog import SetHomeworldDialog
from lib.gui_qt.set_race_dialog import SetRaceDialog
from lib.gui_qt.set_trait_dialog import SetTraitDialog
from lib.gui_qt.skills_dialog import SkillsDialog
from lib.gui_qt.wca_window import Ui_MainWindow
from lib.gui_qt.weapon_dialog import WeaponDialog


class WCA(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(WCA, self).__init__(parent)
        self.setupUi(self)

        self.tw_main.hide()

        # Menubar events
        self.actionNew.triggered.connect(self.new)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionExport.triggered.connect(self.export)
        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout.triggered.connect(self.show_about)

        # Overview tab events
        self.le_overview_name_val.textEdited.connect(self.set_name)
        self.pb_overview_trait_val.clicked.connect(self.set_trait)
        self.le_overview_hook_val.textEdited.connect(self.set_hook)
        self.pb_set_defense_skills.clicked.connect(self.set_defense_skills)

        # Race tab events
        self.pb_race_race_val.clicked.connect(self.set_race)
        self.cb_race_size_val.currentIndexChanged.connect(self.set_size)
        self.pb_race_set_skills.clicked.connect(self.set_race_skills)
        self.lw_race_exploits_val.currentRowChanged.connect(self.show_race_exploit_desc)

        # Homeworld tab events
        self.pb_homeworld_homeworld_val.clicked.connect(self.set_homeworld)
        self.pb_homeworld_set_skills.clicked.connect(self.set_homeworld_skills)

        # Careers tab events
        self.pb_careers_add.clicked.connect(self.add_career)
        self.pb_careers_edit.clicked.connect(self.edit_career)
        self.pb_careers_remove.clicked.connect(self.remove_career)
        self.pb_careers_move_up.clicked.connect(self.move_career_up)
        self.pb_careers_move_down.clicked.connect(self.move_career_down)
        self.pb_careers_set_skills.clicked.connect(self.set_career_skills)
        self.pb_careers_set_exploit.clicked.connect(self.set_career_exploit)
        self.lw_careers_careers_val.currentRowChanged.connect(self.on_career_select)

        # Exploits tab events
        self.pb_exploits_add.clicked.connect(self.add_misc_exploit)
        self.pb_exploits_remove.clicked.connect(self.remove_misc_exploit)
        self.lw_exploits_exploits_val.currentRowChanged.connect(self.on_misc_exploit_select)

        # Equipment tab events
        ## General tab events
        self.pb_eq_gn_add.clicked.connect(self.add_general_gear)
        self.pb_eq_gn_remove.clicked.connect(self.remove_general_gear)
        ## Weapons tab events
        self.pb_eq_wp_add.clicked.connect(self.add_weapon)
        self.pb_eq_wp_remove.clicked.connect(self.remove_weapon)
        self.pb_eq_wp_ammo_add.clicked.connect(self.add_ammunition)
        self.pb_eq_wp_ammo_remove.clicked.connect(self.remove_ammunition)
        self.tw_eq_wp_val.currentItemChanged.connect(self.on_weapon_select)
        ## Armor tab events
        self.pb_eq_ar_add.clicked.connect(self.add_armor)
        self.pb_eq_ar_remove.clicked.connect(self.remove_armor)

        self.user_character = None
        self.file_path = None
        self.file_name = 'untitled'
        self.character_saved = True
        self.size_choices = ['tiny', 'small', 'medium', 'large', 'enormous', 'gigantic', 'colossal', 'titanic']
        self.version = 'v0.21.0'

        self.tw_eq_gn_val.setColumnWidth(0, 250)
        self.tw_eq_gn_val.setColumnWidth(2, 80)
        self.tw_eq_gn_val.setColumnWidth(3, 100)

        self.tw_eq_wp_val.setColumnWidth(0, 250)
        self.tw_eq_wp_val.setColumnWidth(1, 90)
        self.tw_eq_wp_val.setColumnWidth(3, 60)
        self.tw_eq_wp_val.setColumnWidth(4, 100)
        self.tw_eq_wp_val.setColumnWidth(5, 70)
        self.tw_eq_wp_val.setColumnWidth(6, 90)
        self.tw_eq_wp_val.setColumnWidth(7, 100)

        self.tw_eq_ar_val.setColumnWidth(0, 250)
        self.tw_eq_ar_val.setColumnWidth(1, 60)
        self.tw_eq_ar_val.setColumnWidth(2, 70)
        self.tw_eq_ar_val.setColumnWidth(3, 70)
        self.tw_eq_ar_val.setColumnWidth(5, 80)
        self.tw_eq_ar_val.setColumnWidth(6, 90)
        self.tw_eq_ar_val.setColumnWidth(7, 100)

    def save_changes_dialog(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle('WOIN Character Assistant')
        dialog.setIcon(QtWidgets.QMessageBox.Question)
        dialog.setText('There are currently unsaved changes. Would you like to save?')
        dialog.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)

        return dialog.exec_()

    ##################
    # Menu Functions #
    ##################
    def new(self):
        if not self.character_saved:
            ret_val = self.save_changes_dialog()
            # User clicks yes to save
            if ret_val == QtWidgets.QMessageBox.Yes:
                self.save()
                # If the user cancels the save dialog, we don't want to continue
                if not self.character_saved:
                    return
            # User clicks cancel, we don't want to continue
            elif ret_val == QtWidgets.QMessageBox.Cancel:
                return
            # Otherwise, user has clicked no and we can continue
        self.user_character = character.Character(race={'Race': copy.deepcopy(races_new.race_new_human),
                                                        'Source': 'new',
                                                        'Skills': [],
                                                        'Size': 'medium',
                                                        'Stats': copy.deepcopy(races_new.race_new_human.stats)},
                                                  homeworld={'Homeworld': copy.deepcopy(homeworlds_new.homeworld_none),
                                                             'Source': 'new',
                                                             'Skills': []},
                                                  age_descriptor='young')
        self.tw_main.show()

        self.actionSave.setEnabled(True)
        self.actionSave_As.setEnabled(True)
        self.actionExport.setEnabled(True)

        self.update_overview_tab()
        self.update_race_tab()
        self.update_homeworld_tab()
        self.update_careers_tab()
        self.update_exploits_tab()
        self.update_general_equipment_tab()
        self.update_weapons_equipment_tab()
        self.update_armor_equipment_tab()
        self.character_saved = True
        self.setWindowTitle('untitled - WOIN Character Assistant')

    def open(self):
        if not self.character_saved:
            ret_val = self.save_changes_dialog()
            # User clicks yes to save
            if ret_val == QtWidgets.QMessageBox.Yes:
                self.save()
                # If the user cancels the save dialog, we don't want to continue
                if not self.character_saved:
                    return
            # User clicks cancel, we don't want to continue
            elif ret_val == QtWidgets.QMessageBox.Cancel:
                return
            # Otherwise, user has clicked no and we can continue
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Character - WOIN Character Assistant",
                                                             "", "WCA Files (*.wca)",
                                                             options=options)
        if path_name:
            try:
                with open(path_name, 'rb') as file:
                    match = re.search('.*[/\\\\](.*?)\.wca', path_name)
                    self.file_path = path_name
                    self.file_name = match.group(1)
                    self.user_character = pickle.load(file)
                    self.tw_main.show()

                    self.actionSave.setEnabled(True)
                    self.actionSave_As.setEnabled(True)
                    self.actionExport.setEnabled(True)

                    self.update_overview_tab()
                    self.update_race_tab()
                    self.update_homeworld_tab()
                    self.update_careers_tab()
                    self.update_exploits_tab()
                    self.update_general_equipment_tab()
                    self.update_weapons_equipment_tab()
                    self.update_armor_equipment_tab()
                    self.character_saved = True
                    self.setWindowTitle('{} - WOIN Character Assistant'.format(self.file_name))
            except IOError:
                print("Cannot open file '{}'.".format(file))

    def save(self):
        if self.file_path is not None:
            try:
                with open(self.file_path, 'wb') as file:
                    pickle.dump(self.user_character, file, pickle.HIGHEST_PROTOCOL)
                    self.character_saved = True
                    self.setWindowTitle('{} - WOIN Character Assistant'.format(self.file_name))
            except IOError:
                print("Cannot open file '{}'.".format(file))
            self.setWindowTitle('{} - WOIN Character Assistant'.format(self.file_name))
        else:
            self.save_as()

    def save_as(self):
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Character - WOIN Character Assistant",
                                                             "", "WCA Files (*.wca)",
                                                             options=options)
        if path_name:
            try:
                with open(path_name, 'wb') as file:
                    match = re.search('.*[/\\\\](.*?)\.wca', path_name)
                    self.file_path = path_name
                    self.file_name = match.group(1)

                    pickle.dump(self.user_character, file, pickle.HIGHEST_PROTOCOL)

                    self.character_saved = True
                    self.setWindowTitle('{} - WOIN Character Assistant'.format(self.file_name))
            except IOError:
                print("Cannot open file '{}'.".format(file))

    def export(self):
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export Character - WOIN Character Assistant",
                                                             "", "HTML Files (*.html)",
                                                             options=options)
        if path_name:
            try:
                with open(path_name, 'w') as file:
                    html = generate_character_sheet(self.user_character)
                    file.write(html)
            except IOError:
                print("Cannot open file '{}'.".format(file))

    def quit(self):
        if not self.character_saved:
            ret_val = self.save_changes_dialog()
            # User clicks yes to save
            if ret_val == QtWidgets.QMessageBox.Yes:
                self.save()
                # If the user cancels the save dialog, we don't want to continue
                if not self.character_saved:
                    return
            # User clicks cancel, we don't want to continue
            elif ret_val == QtWidgets.QMessageBox.Cancel:
                return
            # Otherwise, user has clicked no and we can continue
        sys.exit()

    def show_about(self):
        about_str = 'WOIN Character Assistant {}\n'.format(self.version)
        about_str += '    A character creation tool for the WOIN RPG\n'
        about_str += '    http://www.woinrpg.com/\n'
        about_str += '\nWritten by:\n'
        about_str += 'DesertDogSledder'
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle('WOIN Character Assistant')
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setText(about_str)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)

        return dialog.exec_()

    def update_overview_tab(self):
        # Info
        self.le_overview_name_val.setText(self.user_character.name)
        self.l_overview_race_val.setText(self.user_character.race['Race'].name)
        self.l_overview_homeworld_val.setText(self.user_character.homeworld['Homeworld'].name)
        self.pb_overview_trait_val.setText(self.user_character.trait['Name'])
        self.le_overview_hook_val.setText(self.user_character.hook)

        # Skills
        skill_total = self.user_character.calc_skill_total()
        skill_total_str = ''
        for skill, value in skill_total.items():
            skill_total_str += '{} - {} ({}d6)\n'.format(skill, value, character.calc_dice_pool_size(value))
        self.pte_overview_skills_val.setPlainText(skill_total_str)

        # Exploits
        all_exploits_str = ''
        for exploit in self.user_character.get_all_exploits():
            all_exploits_str += '{} - {}\n\n'.format(exploit['Name'], exploit['Desc'])

        self.pte_overview_exploits_val.setPlainText(all_exploits_str)

        # Derived Statistics
        derived_stats = self.user_character.calc_derived_stats()
        self.l_overview_health_val.setText('{}'.format(derived_stats['Health']))
        self.l_overview_initiative_val.setText('{}d6'.format(derived_stats['Initiative']))

        self.l_overview_speed_val.setText('{}'.format(derived_stats['Speed']))
        self.l_overview_climb_val.setText('{}'.format(derived_stats['Climb']))
        self.l_overview_swim_val.setText('{}'.format(derived_stats['Swim']))
        self.l_overview_zlhg_val.setText('{}/{}/{}'.format(derived_stats['Zero-G'],
                                                           derived_stats['Low-G'],
                                                           derived_stats['High-G']))
        self.l_overview_vertical_jump_val.setText("{}'({}')".format(derived_stats['Vertical Jump Standing'],
                                                                    derived_stats['Vertical Jump Running']))
        self.l_overview_horizontal_jump_val.setText("{}'({}')".format(derived_stats['Horizontal Jump Standing'],
                                                                      derived_stats['Horizontal Jump Running']))
        self.l_overview_carry_val.setText('{}'.format(derived_stats['Carry']))

        self.l_overview_melee_def_val.setText('{}'.format(derived_stats['Melee Defense']))
        self.l_overview_ranged_def_val.setText('{}'.format(derived_stats['Ranged Defense']))
        self.l_overview_mental_def_val.setText('{}'.format(derived_stats['Mental Defense']))
        self.l_overview_vital_def_val.setText('{}'.format(derived_stats['Vital Defense']))

        # Stats
        total_stats = self.user_character.calc_stat_total()

        self.l_overview_str_val.setText('{} ({}d6)'.format(total_stats['STR'],
                                                           character.calc_dice_pool_size(total_stats['STR'])))
        self.l_overview_agi_val.setText('{} ({}d6)'.format(total_stats['AGI'],
                                                           character.calc_dice_pool_size(total_stats['AGI'])))
        self.l_overview_end_val.setText('{} ({}d6)'.format(total_stats['END'],
                                                           character.calc_dice_pool_size(total_stats['END'])))
        self.l_overview_int_val.setText('{} ({}d6)'.format(total_stats['INT'],
                                                           character.calc_dice_pool_size(total_stats['INT'])))
        self.l_overview_log_val.setText('{} ({}d6)'.format(total_stats['LOG'],
                                                           character.calc_dice_pool_size(total_stats['LOG'])))
        self.l_overview_wil_val.setText('{} ({}d6)'.format(total_stats['WIL'],
                                                           character.calc_dice_pool_size(total_stats['WIL'])))
        self.l_overview_cha_val.setText('{} ({}d6)'.format(total_stats['CHA'],
                                                           character.calc_dice_pool_size(total_stats['CHA'])))
        self.l_overview_luc_val.setText('{} ({}d6)'.format(total_stats['LUC'],
                                                           character.calc_dice_pool_size(total_stats['LUC'])))
        self.l_overview_rep_val.setText('{} ({}d6)'.format(total_stats['REP'],
                                                           character.calc_dice_pool_size(total_stats['REP'])))
        self.l_overview_mag_val.setText('{} ({}d6)'.format(total_stats['MAG'],
                                                           character.calc_dice_pool_size(total_stats['MAG'])))
        self.l_overview_chi_val.setText('{} ({}d6)'.format(total_stats['CHI'],
                                                           character.calc_dice_pool_size(total_stats['CHI'])))
        self.l_overview_psi_val.setText('{} ({}d6)'.format(total_stats['PSI'],
                                                           character.calc_dice_pool_size(total_stats['PSI'])))
        self.character_saved = False
        self.setWindowTitle('*{} - WOIN Character Assistant'.format(self.file_name))

    def update_race_tab(self):
        # Race
        self.pb_race_race_val.setText(self.user_character.race['Race'].name)
        self.cb_race_size_val.setCurrentIndex(self.size_choices.index(self.user_character.race['Size'].lower()))

        # Skills
        selected_race_skills = ''
        for skill_pick in self.user_character.race['Skills']:
            selected_race_skills += '{} ({}), '.format(skill_pick['Name'], skill_pick['Rank'])
        selected_race_skills = selected_race_skills[:-2]
        if selected_race_skills == '':
            self.pte_race_skills_val.setPlainText('No skills selected')
        else:
            self.pte_race_skills_val.setPlainText(selected_race_skills)

        # Exploits
        self.lw_race_exploits_val.clear()
        for exploit in self.user_character.race['Race'].exploits:
            self.lw_race_exploits_val.addItem(str(exploit['Name']))
        self.lw_race_exploits_val.setCurrentRow(0)

        # Racial Stats
        self.l_race_str_val.setText('{:+d}'.format(self.user_character.race['Stats']['STR']))
        self.l_race_agi_val.setText('{:+d}'.format(self.user_character.race['Stats']['AGI']))
        self.l_race_end_val.setText('{:+d}'.format(self.user_character.race['Stats']['END']))
        self.l_race_int_val.setText('{:+d}'.format(self.user_character.race['Stats']['INT']))
        self.l_race_log_val.setText('{:+d}'.format(self.user_character.race['Stats']['LOG']))
        self.l_race_wil_val.setText('{:+d}'.format(self.user_character.race['Stats']['WIL']))
        self.l_race_cha_val.setText('{:+d}'.format(self.user_character.race['Stats']['CHA']))
        self.l_race_luc_val.setText('{:+d}'.format(self.user_character.race['Stats']['LUC']))
        self.l_race_rep_val.setText('{:+d}'.format(self.user_character.race['Stats']['REP']))
        self.l_race_mag_val.setText('{:+d}'.format(self.user_character.race['Stats']['MAG']))
        self.l_race_chi_val.setText('{:+d}'.format(self.user_character.race['Stats']['CHI']))
        self.l_race_psi_val.setText('{:+d}'.format(self.user_character.race['Stats']['PSI']))

    def update_homeworld_tab(self):
        self.pb_homeworld_homeworld_val.setText(self.user_character.homeworld['Homeworld'].name)

        selected_homeworld_skills = ''
        for skill_pick in self.user_character.homeworld['Skills']:
            selected_homeworld_skills += '{} ({}), '.format(skill_pick['Name'], skill_pick['Rank'])
            selected_homeworld_skills = selected_homeworld_skills[:-2]

        if selected_homeworld_skills == '':
            self.pte_homeworld_skills_val.setPlainText('No skills selected')
        else:
            self.pte_homeworld_skills_val.setPlainText(selected_homeworld_skills)

        self.l_homeworld_str_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['STR']))
        self.l_homeworld_agi_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['AGI']))
        self.l_homeworld_end_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['END']))
        self.l_homeworld_int_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['INT']))
        self.l_homeworld_log_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['LOG']))
        self.l_homeworld_wil_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['WIL']))
        self.l_homeworld_cha_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['CHA']))
        self.l_homeworld_luc_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['LUC']))
        self.l_homeworld_rep_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['REP']))
        self.l_homeworld_mag_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['MAG']))
        self.l_homeworld_chi_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['CHI']))
        self.l_homeworld_psi_val.setText('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['PSI']))

    def update_careers_tab(self):
        self.lw_careers_careers_val.clear()
        for career in self.user_character.career_track:
            self.lw_careers_careers_val.addItem(career['Career'].name)

        if self.lw_careers_careers_val.count() <= 0:
            self.l_careers_str_val.setText('-')
            self.l_careers_agi_val.setText('-')
            self.l_careers_end_val.setText('-')
            self.l_careers_int_val.setText('-')
            self.l_careers_log_val.setText('-')
            self.l_careers_wil_val.setText('-')
            self.l_careers_cha_val.setText('-')
            self.l_careers_luc_val.setText('-')
            self.l_careers_rep_val.setText('-')
            self.l_careers_mag_val.setText('-')
            self.l_careers_chi_val.setText('-')
            self.l_careers_psi_val.setText('-')
            self.on_career_select(-1)
        else:
            self.lw_careers_careers_val.setCurrentRow(0)

    def update_exploits_tab(self):
        self.lw_exploits_exploits_val.clear()
        for exploit in self.user_character.misc_exploits:
            self.lw_exploits_exploits_val.addItem(exploit['Name'])

        if len(self.user_character.misc_exploits) <= 0:
            self.pb_exploits_remove.setDisabled(True)
        else:
            self.pb_exploits_remove.setDisabled(False)

    def update_general_equipment_tab(self):
        self.tw_eq_gn_val.clear()
        twi_list = []
        for item in self.user_character.equipment['General']:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(item['Name']))
            twi_list[-1].setText(1, '{}'.format(item['Weight']))
            twi_list[-1].setText(2, '{}'.format(item['Quantity']))
            twi_list[-1].setText(3, '{}'.format(item['Quantity'] * item['Cost']))

        self.tw_eq_gn_val.addTopLevelItems(twi_list)

        if len(twi_list) == 0:
            self.pb_eq_gn_remove.setDisabled(True)
        else:
            self.pb_eq_gn_remove.setDisabled(False)

    def update_weapons_equipment_tab(self):
        self.tw_eq_wp_val.clear()
        twi_list = []
        for weapon in self.user_character.equipment['Weapons']:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(weapon['Name']))
            twi_list[-1].setText(1, '{}'.format(weapon['Damage']))
            twi_list[-1].setText(2, '{}'.format(weapon['Type']))
            twi_list[-1].setText(3, '{}'.format(weapon['Range']))
            twi_list[-1].setText(4, '{}'.format(weapon['Special']))
            twi_list[-1].setText(5, '{}'.format(weapon['Quantity']))
            twi_list[-1].setText(6, '{}'.format(weapon['Quantity'] * weapon['Cost']))
            twi_list[-1].setText(7, '{}'.format(weapon['Quantity'] * weapon['Weight']))
            if len(weapon['Ammunition']) > 0:
                ammo_list = []
                for item in weapon['Ammunition']:
                    ammo_list.append(QtWidgets.QTreeWidgetItem(twi_list[-1]))
                    ammo_list[-1].setText(0, '{}'.format(item['Name']))
                    ammo_list[-1].setText(5, '{}'.format(item['Quantity']))
                    ammo_list[-1].setText(6, '{}'.format(item['Quantity'] * item['Cost']))
                    ammo_list[-1].setText(7, '{}'.format(item['Quantity'] * 1))
            self.tw_eq_wp_val.addTopLevelItem(twi_list[-1])
            twi_list[-1].setExpanded(True)

        #self.tw_eq_wp_val.addTopLevelItems(twi_list)

        if len(twi_list) == 0:
            self.pb_eq_wp_remove.setDisabled(True)
            self.gb_eq_wp_ammo.setDisabled(True)
        else:
            self.pb_eq_wp_remove.setDisabled(False)

    def update_armor_equipment_tab(self):
        self.tw_eq_ar_val.clear()
        twi_list = []
        for armor in self.user_character.equipment['Armor']:
            twi_list.append(QtWidgets.QTreeWidgetItem(None))
            twi_list[-1].setText(0, '{}'.format(armor['Name']))
            twi_list[-1].setText(1, '{}'.format(armor['Soak']))
            twi_list[-1].setText(2, '{}'.format(armor['Defense']))
            twi_list[-1].setText(3, '{}'.format(armor['Speed']))
            twi_list[-1].setText(4, '{}'.format(armor['Type']))
            twi_list[-1].setText(5, '{}'.format(armor['Special']))
            twi_list[-1].setText(6, '{}'.format(armor['Quantity']))
            twi_list[-1].setText(7, '{}'.format(armor['Quantity'] * armor['Cost']))
            twi_list[-1].setText(8, '{}'.format(armor['Quantity'] * armor['Weight']))

        self.tw_eq_ar_val.addTopLevelItems(twi_list)

        if len(twi_list) == 0:
            self.pb_eq_ar_remove.setDisabled(True)
        else:
            self.pb_eq_ar_remove.setDisabled(False)

    ##########################
    # Overview tab functions #
    ##########################
    def set_name(self):
        self.user_character.name = self.le_overview_name_val.displayText()
        self.setWindowTitle('*{} - WOIN Character Assistant'.format(self.file_name))
        self.character_saved = False

    def set_trait(self):
        set_trait_dialog = SetTraitDialog()
        total_stats = self.user_character.calc_stat_total()

        set_trait_dialog.l_std_str_val.setText('{}'.format(total_stats['STR']))
        set_trait_dialog.l_std_agi_val.setText('{}'.format(total_stats['AGI']))
        set_trait_dialog.l_std_end_val.setText('{}'.format(total_stats['END']))
        set_trait_dialog.l_std_int_val.setText('{}'.format(total_stats['INT']))
        set_trait_dialog.l_std_log_val.setText('{}'.format(total_stats['LOG']))
        set_trait_dialog.l_std_wil_val.setText('{}'.format(total_stats['WIL']))
        set_trait_dialog.l_std_cha_val.setText('{}'.format(total_stats['CHA']))
        set_trait_dialog.l_std_luc_val.setText('{}'.format(total_stats['LUC']))
        set_trait_dialog.l_std_rep_val.setText('{}'.format(total_stats['REP']))
        set_trait_dialog.l_std_mag_val.setText('{}'.format(total_stats['MAG']))
        set_trait_dialog.l_std_chi_val.setText('{}'.format(total_stats['CHI']))
        set_trait_dialog.l_std_psi_val.setText('{}'.format(total_stats['PSI']))

        # Check to see if we've set the trait before. If so, pre-select the trait on the dialog.
        trait = set_trait_dialog.lw_std_traits.findItems(self.user_character.trait['Name'], QtCore.Qt.MatchExactly)
        if trait:
            set_trait_dialog.lw_std_traits.setCurrentItem(trait[0])
            set_trait_dialog.on_trait_select()

        # If the user accepted the dialog, set the new trait
        if set_trait_dialog.exec_():
            self.user_character.trait = copy.deepcopy(set_trait_dialog.trait_list[
                                                          set_trait_dialog.lw_std_traits.currentRow()])
            self.update_overview_tab()

    def set_hook(self):
        self.user_character.hook = self.le_overview_hook_val.displayText()
        self.character_saved = False

    def set_defense_skills(self):
        set_defense_skills_dialog = SetDefenseSkillsDialog()

        set_defense_skills_dialog.cb_sdsd_melee_val.addItem('')
        set_defense_skills_dialog.cb_sdsd_ranged_val.addItem('')
        set_defense_skills_dialog.cb_sdsd_mental_val.addItem('')
        set_defense_skills_dialog.cb_sdsd_vital_val.addItem('')

        total_skills = self.user_character.calc_skill_total()

        for skill in total_skills:
            set_defense_skills_dialog.cb_sdsd_melee_val.addItem(skill)
            set_defense_skills_dialog.cb_sdsd_ranged_val.addItem(skill)
            set_defense_skills_dialog.cb_sdsd_mental_val.addItem(skill)
            set_defense_skills_dialog.cb_sdsd_vital_val.addItem(skill)

        # Check for matches in the list so we can pre-select values
        melee = set_defense_skills_dialog.cb_sdsd_melee_val.findText(self.user_character.defense_skills['Melee'],
                                                                     QtCore.Qt.MatchExactly)
        ranged = set_defense_skills_dialog.cb_sdsd_ranged_val.findText(self.user_character.defense_skills['Ranged'],
                                                                       QtCore.Qt.MatchExactly)
        mental = set_defense_skills_dialog.cb_sdsd_mental_val.findText(self.user_character.defense_skills['Mental'],
                                                                       QtCore.Qt.MatchExactly)
        vital = set_defense_skills_dialog.cb_sdsd_vital_val.findText(self.user_character.defense_skills['Vital'],
                                                                     QtCore.Qt.MatchExactly)

        if melee:
            set_defense_skills_dialog.cb_sdsd_melee_val.setCurrentIndex(melee)
        if ranged:
            set_defense_skills_dialog.cb_sdsd_ranged_val.setCurrentIndex(ranged)
        if mental:
            set_defense_skills_dialog.cb_sdsd_mental_val.setCurrentIndex(mental)
        if vital:
            set_defense_skills_dialog.cb_sdsd_vital_val.setCurrentIndex(vital)

        if set_defense_skills_dialog.exec_():
            self.user_character.defense_skills['Melee'] = set_defense_skills_dialog.cb_sdsd_melee_val.currentText()
            self.user_character.defense_skills['Ranged'] = set_defense_skills_dialog.cb_sdsd_ranged_val.currentText()
            self.user_character.defense_skills['Mental'] = set_defense_skills_dialog.cb_sdsd_mental_val.currentText()
            self.user_character.defense_skills['Vital'] = set_defense_skills_dialog.cb_sdsd_vital_val.currentText()
            self.update_overview_tab()

    ######################
    # Race tab functions #
    ######################
    def set_race(self):
        set_race_dialog = SetRaceDialog()

        # Pre-select the dialog's source button based on current character's race source
        if self.user_character.race['Source'] == 'now':
            set_race_dialog.rb_srd_now.setChecked(True)
        elif self.user_character.race['Source'] == 'new':
            set_race_dialog.rb_srd_new.setChecked(True)
        elif self.user_character.race['Source'] == 'custom':
            set_race_dialog.rb_srd_custom.setChecked(True)
        else:
            set_race_dialog.rb_srd_old.setChecked(True)

        set_race_dialog.on_source_select(True)

        # Search the list for the current character's race so we can select it
        race = set_race_dialog.lw_srd_races_val.findItems(self.user_character.race['Race'].name, QtCore.Qt.MatchExactly)
        set_race_dialog.lw_srd_races_val.setCurrentItem(race[0])

        if set_race_dialog.exec_():
            self.user_character.race = {'Race': copy.deepcopy(set_race_dialog.race_list[
                                                                  set_race_dialog.lw_srd_races_val.currentRow()]),
                                        'Source': set_race_dialog.race_source,
                                        'Size': 'Medium',
                                        'Stats': collections.OrderedDict(STR=set_race_dialog.sb_srd_str_val.value(),
                                                                         AGI=set_race_dialog.sb_srd_agi_val.value(),
                                                                         END=set_race_dialog.sb_srd_end_val.value(),
                                                                         INT=set_race_dialog.sb_srd_int_val.value(),
                                                                         LOG=set_race_dialog.sb_srd_log_val.value(),
                                                                         WIL=set_race_dialog.sb_srd_wil_val.value(),
                                                                         CHA=set_race_dialog.sb_srd_cha_val.value(),
                                                                         LUC=set_race_dialog.sb_srd_luc_val.value(),
                                                                         REP=set_race_dialog.sb_srd_rep_val.value(),
                                                                         MAG=set_race_dialog.sb_srd_mag_val.value(),
                                                                         CHI=set_race_dialog.sb_srd_chi_val.value(),
                                                                         PSI=set_race_dialog.sb_srd_psi_val.value()),
                                        'Skills': []}
            self.update_race_tab()
            self.update_overview_tab()

    def set_size(self):
        self.user_character.race['Size'] = self.cb_race_size_val.currentText().lower()
        self.update_overview_tab()

    def set_race_skills(self):
        set_race_skills_dialog = SkillsDialog()
        available_skills_str = ''
        for race_skill in self.user_character.race['Race'].available_skills:
            available_skills_str += '{}, '.format(race_skill)
        set_race_skills_dialog.pte_sd_available_skills_val.setPlainText(available_skills_str[:-2])
        set_race_skills_dialog.skills = copy.deepcopy(self.user_character.race['Skills'])
        set_race_skills_dialog.regenerate_list()

        if set_race_skills_dialog.exec_():
            self.user_character.race['Skills'] = copy.deepcopy(set_race_skills_dialog.skills)
            self.update_overview_tab()
            self.update_race_tab()

    def show_race_exploit_desc(self, current_row):
        self.pte_race_exploits_desc.clear()
        if current_row != -1:
            self.pte_race_exploits_desc.setPlainText(self.user_character.race['Race'].exploits[current_row]['Desc'])

    ###########################
    # Homeworld tab functions #
    ###########################
    def set_homeworld(self):
        set_homeworld_dialog = SetHomeworldDialog()

        # Pre-select the dialog's source button based on current character's homeworld source
        if self.user_character.race['Source'] == 'custom':
            set_homeworld_dialog.rb_shd_custom.setChecked(True)
        else:
            set_homeworld_dialog.rb_shd_new.setChecked(True)

        set_homeworld_dialog.on_source_select(True)

        # Search the list for the current character's race so we can select it
        homeworld = set_homeworld_dialog.lw_shd_homeworlds_val.findItems(
            self.user_character.homeworld['Homeworld'].name, QtCore.Qt.MatchExactly)
        set_homeworld_dialog.lw_shd_homeworlds_val.setCurrentItem(homeworld[0])
        set_homeworld_dialog.on_homeworld_select()

        if set_homeworld_dialog.exec_():
            self.user_character.homeworld = {'Homeworld': copy.deepcopy(
                set_homeworld_dialog.homeworld_list[set_homeworld_dialog.lw_shd_homeworlds_val.currentRow()]),
                'Source': set_homeworld_dialog.homeworld_source,
                'Stats': collections.OrderedDict(STR=set_homeworld_dialog.sb_shd_str_val.value(),
                                                 AGI=set_homeworld_dialog.sb_shd_agi_val.value(),
                                                 END=set_homeworld_dialog.sb_shd_end_val.value(),
                                                 INT=set_homeworld_dialog.sb_shd_int_val.value(),
                                                 LOG=set_homeworld_dialog.sb_shd_log_val.value(),
                                                 WIL=set_homeworld_dialog.sb_shd_wil_val.value(),
                                                 CHA=set_homeworld_dialog.sb_shd_cha_val.value(),
                                                 LUC=set_homeworld_dialog.sb_shd_luc_val.value(),
                                                 REP=set_homeworld_dialog.sb_shd_rep_val.value(),
                                                 MAG=set_homeworld_dialog.sb_shd_mag_val.value(),
                                                 CHI=set_homeworld_dialog.sb_shd_chi_val.value(),
                                                 PSI=set_homeworld_dialog.sb_shd_psi_val.value()),
                'Skills': []}
            self.update_overview_tab()
            self.update_homeworld_tab()

    def set_homeworld_skills(self):
        set_homeworld_skills_dialog = SkillsDialog()
        available_skills_str = ''
        for homeworld_skill in self.user_character.homeworld['Homeworld'].available_skills:
            available_skills_str += '{}, '.format(homeworld_skill)
        set_homeworld_skills_dialog.pte_sd_available_skills_val.setPlainText(available_skills_str[:-2])
        set_homeworld_skills_dialog.skills = copy.deepcopy(self.user_character.homeworld['Skills'])
        set_homeworld_skills_dialog.regenerate_list()

        if set_homeworld_skills_dialog.exec_():
            self.user_character.homeworld['Skills'] = copy.deepcopy(set_homeworld_skills_dialog.skills)
            self.update_overview_tab()
            self.update_homeworld_tab()

    #########################
    # Careers tab functions #
    #########################
    def add_career(self):
        career_dialog = EditCareerDialog()
        
        if career_dialog.exec_():
            selected_career = career_dialog.career_list[career_dialog.lw_ecd_careers_val.currentRow()]
            self.user_character.career_track.append(
                {'Source': career_dialog.career_source,
                 'Career': copy.deepcopy(selected_career),
                 'Length': '{} {}'.format(
                     dice.roll(selected_career.career_time)['total'],
                     selected_career.career_time_unit),
                 'Stats': collections.OrderedDict(STR=career_dialog.sb_ecd_str_val.value(),
                                                  AGI=career_dialog.sb_ecd_agi_val.value(),
                                                  END=career_dialog.sb_ecd_end_val.value(),
                                                  INT=career_dialog.sb_ecd_int_val.value(),
                                                  LOG=career_dialog.sb_ecd_log_val.value(),
                                                  WIL=career_dialog.sb_ecd_wil_val.value(),
                                                  CHA=career_dialog.sb_ecd_cha_val.value(),
                                                  LUC=career_dialog.sb_ecd_luc_val.value(),
                                                  REP=career_dialog.sb_ecd_rep_val.value(),
                                                  MAG=career_dialog.sb_ecd_mag_val.value(),
                                                  CHI=career_dialog.sb_ecd_chi_val.value(),
                                                  PSI=career_dialog.sb_ecd_psi_val.value()),
                 'Skills': [],
                 'Exploit': {'Name': 'unset career exploit', 'Desc': 'unset', 'Source': 'unset'},
                 'Notes': ''})
            self.update_overview_tab()
            self.update_careers_tab()
            self.lw_careers_careers_val.setCurrentRow(self.lw_careers_careers_val.count()-1)

    def edit_career(self):
        career_dialog = EditCareerDialog()
        career_track_index = self.lw_careers_careers_val.currentRow()
        current_list_source = self.user_character.career_track[career_track_index]['Source']
        if current_list_source == 'origins':
            career_dialog.rb_ecd_origins.setChecked(True)
        elif current_list_source == 'old':
            career_dialog.rb_ecd_old.setChecked(True)
        elif current_list_source == 'now':
            career_dialog.rb_ecd_now.setChecked(True)
        elif current_list_source == 'new':
            career_dialog.rb_ecd_new.setChecked(True)
        elif current_list_source == 'martial arts':
            career_dialog.rb_ecd_ma.setChecked(True)
        elif current_list_source == 'custom':
            career_dialog.rb_ecd_custom.setChecked(True)

        career_dialog.on_source_select(True)

        # Search the list for the current character's career so we can select it
        career = career_dialog.lw_ecd_careers_val.findItems(
            self.user_character.career_track[career_track_index]['Career'].name, QtCore.Qt.MatchExactly)
        career_dialog.lw_ecd_careers_val.setCurrentItem(career[0])

        if career_dialog.exec_():
            selected_career = career_dialog.career_list[career_dialog.lw_ecd_careers_val.currentRow()]
            self.user_character.career_track[career_track_index] = \
                {'Source': career_dialog.career_source,
                 'Career': copy.deepcopy(selected_career),
                 'Length': '{} {}'.format(
                     dice.roll(selected_career.career_time)['total'],
                     selected_career.career_time_unit),
                 'Stats': collections.OrderedDict(STR=career_dialog.sb_ecd_str_val.value(),
                                                  AGI=career_dialog.sb_ecd_agi_val.value(),
                                                  END=career_dialog.sb_ecd_end_val.value(),
                                                  INT=career_dialog.sb_ecd_int_val.value(),
                                                  LOG=career_dialog.sb_ecd_log_val.value(),
                                                  WIL=career_dialog.sb_ecd_wil_val.value(),
                                                  CHA=career_dialog.sb_ecd_cha_val.value(),
                                                  LUC=career_dialog.sb_ecd_luc_val.value(),
                                                  REP=career_dialog.sb_ecd_rep_val.value(),
                                                  MAG=career_dialog.sb_ecd_mag_val.value(),
                                                  CHI=career_dialog.sb_ecd_chi_val.value(),
                                                  PSI=career_dialog.sb_ecd_psi_val.value()),
                 'Skills': [],
                 'Exploit': {'Name': 'unset career exploit', 'Desc': 'unset', 'Source': 'unset'},
                 'Notes': ''}
            self.update_overview_tab()
            self.update_careers_tab()

    def remove_career(self):
        selected_career = self.lw_careers_careers_val.currentRow()
        self.user_character.career_track.pop(selected_career)
        self.update_overview_tab()
        self.update_careers_tab()

        if selected_career < self.lw_careers_careers_val.count()-1:
            self.lw_careers_careers_val.setCurrentRow(selected_career)
        elif selected_career >= self.lw_careers_careers_val.currentRow()-1:
            self.lw_careers_careers_val.setCurrentRow(self.lw_careers_careers_val.count()-1)

    def move_career_up(self):
        selected_career = self.lw_careers_careers_val.currentRow()
        self.user_character.career_track[selected_career], \
            self.user_character.career_track[selected_career-1] = \
            self.user_character.career_track[selected_career-1], \
            self.user_character.career_track[selected_career]

        self.update_careers_tab()
        self.lw_careers_careers_val.setCurrentRow(selected_career-1)

    def move_career_down(self):
        selected_career = self.lw_careers_careers_val.currentRow()
        self.user_character.career_track[selected_career], \
            self.user_character.career_track[selected_career+1] = \
            self.user_character.career_track[selected_career+1], \
            self.user_character.career_track[selected_career]

        self.update_careers_tab()
        self.lw_careers_careers_val.setCurrentRow(selected_career+1)

    def set_career_skills(self):
        selected_career = self.lw_careers_careers_val.currentRow()
        set_career_skills_dialog = SkillsDialog()
        available_skills_str = ''
        for skill in self.user_character.career_track[selected_career]['Career'].available_skills:
            available_skills_str += '{}, '.format(skill)
        set_career_skills_dialog.pte_sd_available_skills_val.setPlainText(available_skills_str)
        set_career_skills_dialog.skills = copy.deepcopy(self.user_character.career_track[selected_career]['Skills'])
        set_career_skills_dialog.regenerate_list()

        if set_career_skills_dialog.exec_():
            self.user_character.career_track[selected_career]['Skills'] = copy.deepcopy(set_career_skills_dialog.skills)
            self.update_overview_tab()
            self.update_careers_tab()
            self.lw_careers_careers_val.setCurrentRow(selected_career)

    def set_career_exploit(self):
        selected_career = self.lw_careers_careers_val.currentRow()
        current_stats = self.user_character.calc_current_stat_total(selected_career)
        set_career_exploit_dialog = ExploitDialog(career=self.user_character.career_track[selected_career]['Career'])

        set_career_exploit_dialog.l_ed_str_val.setText('{}'.format(current_stats['STR']))
        set_career_exploit_dialog.l_ed_agi_val.setText('{}'.format(current_stats['AGI']))
        set_career_exploit_dialog.l_ed_end_val.setText('{}'.format(current_stats['END']))
        set_career_exploit_dialog.l_ed_int_val.setText('{}'.format(current_stats['INT']))
        set_career_exploit_dialog.l_ed_log_val.setText('{}'.format(current_stats['LOG']))
        set_career_exploit_dialog.l_ed_wil_val.setText('{}'.format(current_stats['WIL']))
        set_career_exploit_dialog.l_ed_cha_val.setText('{}'.format(current_stats['CHA']))
        set_career_exploit_dialog.l_ed_luc_val.setText('{}'.format(current_stats['LUC']))
        set_career_exploit_dialog.l_ed_rep_val.setText('{}'.format(current_stats['REP']))
        set_career_exploit_dialog.l_ed_mag_val.setText('{}'.format(current_stats['MAG']))
        set_career_exploit_dialog.l_ed_chi_val.setText('{}'.format(current_stats['CHI']))
        set_career_exploit_dialog.l_ed_psi_val.setText('{}'.format(current_stats['PSI']))

        if 'Source' in self.user_character.career_track[selected_career]['Exploit']:
            list_source = self.user_character.career_track[selected_career]['Exploit']['Source']
        else:
            list_source = None
        if list_source != 'unset' and list_source is not None:
            if list_source is 'universal':
                set_career_exploit_dialog.rb_ed_universal.setChecked(True)
            elif list_source is 'android':
                set_career_exploit_dialog.rb_ed_android.setChecked(True)
            elif list_source is 'career':
                set_career_exploit_dialog.rb_ed_career.setChecked(True)
            elif list_source is 'custom':
                set_career_exploit_dialog.rb_ed_custom.setChecked(True)
            # Search the list for the current character's career so we can select it
            exploit = set_career_exploit_dialog.lw_ed_exploits_val.findItems(
                self.user_character.career_track[selected_career]['Exploit']['Name'], QtCore.Qt.MatchExactly)
            if len(exploit) > 0:
                set_career_exploit_dialog.lw_ed_exploits_val.setCurrentItem(exploit[0])
        else:
            set_career_exploit_dialog.rb_ed_career.setChecked(True)

        if set_career_exploit_dialog.exec_():
            self.user_character.career_track[selected_career]['Exploit'] = copy.deepcopy(
                set_career_exploit_dialog.exploit_list[set_career_exploit_dialog.lw_ed_exploits_val.currentRow()])
            self.user_character.career_track[
                selected_career]['Exploit']['Source'] = set_career_exploit_dialog.exploit_source
            self.update_overview_tab()
            self.update_careers_tab()
            self.lw_careers_careers_val.setCurrentRow(selected_career)

    def on_career_select(self, current_row):
        if current_row != -1:
            self.pte_careers_exploit_val.setPlainText('{} - {}'.format(
                self.user_character.career_track[current_row]['Exploit']['Name'],
                self.user_character.career_track[current_row]['Exploit']['Desc']))

            selected_skills = ''
            for skill in self.user_character.career_track[current_row]['Skills']:
                selected_skills += '{} ({}), '.format(skill['Name'], skill['Rank'])
            if selected_skills == '':
                self.pte_careers_skills_val.setPlainText('No skills selected')
            else:
                self.pte_careers_skills_val.setPlainText(selected_skills[:-2])

            self.l_careers_str_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['STR']))
            self.l_careers_agi_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['AGI']))
            self.l_careers_end_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['END']))
            self.l_careers_int_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['INT']))
            self.l_careers_log_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['LOG']))
            self.l_careers_wil_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['WIL']))
            self.l_careers_cha_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['CHA']))
            self.l_careers_luc_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['LUC']))
            self.l_careers_rep_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['REP']))
            self.l_careers_mag_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['MAG']))
            self.l_careers_chi_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['CHI']))
            self.l_careers_psi_val.setText('{:+d}'.format(
                self.user_character.career_track[current_row]['Stats']['PSI']))

            if current_row == 0:
                self.pb_careers_move_up.setDisabled(True)
            else:
                self.pb_careers_move_up.setDisabled(False)

            if current_row >= self.lw_careers_careers_val.count()-1:
                self.pb_careers_move_down.setDisabled(True)
            else:
                self.pb_careers_move_down.setDisabled(False)

            self.pb_careers_edit.setDisabled(False)
            self.pb_careers_remove.setDisabled(False)
            self.pb_careers_set_exploit.setDisabled(False)
            self.pb_careers_set_skills.setDisabled(False)
        else:
            self.pte_careers_skills_val.clear()
            self.pte_careers_exploit_val.clear()
            self.pb_careers_edit.setDisabled(True)
            self.pb_careers_remove.setDisabled(True)
            self.pb_careers_move_up.setDisabled(True)
            self.pb_careers_move_down.setDisabled(True)
            self.pb_careers_set_exploit.setDisabled(True)
            self.pb_careers_set_skills.setDisabled(True)

    ##########################
    # Exploits tab functions #
    ##########################
    def add_misc_exploit(self):
        add_misc_exploit_dialog = ExploitDialog()
        total_stats = self.user_character.calc_stat_total()

        add_misc_exploit_dialog.l_ed_str_val.setText('{}'.format(total_stats['STR']))
        add_misc_exploit_dialog.l_ed_agi_val.setText('{}'.format(total_stats['AGI']))
        add_misc_exploit_dialog.l_ed_end_val.setText('{}'.format(total_stats['END']))
        add_misc_exploit_dialog.l_ed_int_val.setText('{}'.format(total_stats['INT']))
        add_misc_exploit_dialog.l_ed_log_val.setText('{}'.format(total_stats['LOG']))
        add_misc_exploit_dialog.l_ed_wil_val.setText('{}'.format(total_stats['WIL']))
        add_misc_exploit_dialog.l_ed_cha_val.setText('{}'.format(total_stats['CHA']))
        add_misc_exploit_dialog.l_ed_luc_val.setText('{}'.format(total_stats['LUC']))
        add_misc_exploit_dialog.l_ed_rep_val.setText('{}'.format(total_stats['REP']))
        add_misc_exploit_dialog.l_ed_mag_val.setText('{}'.format(total_stats['MAG']))
        add_misc_exploit_dialog.l_ed_chi_val.setText('{}'.format(total_stats['CHI']))
        add_misc_exploit_dialog.l_ed_psi_val.setText('{}'.format(total_stats['PSI']))

        if add_misc_exploit_dialog.exec_():
            new_exploit = copy.deepcopy(
                add_misc_exploit_dialog.exploit_list[add_misc_exploit_dialog.lw_ed_exploits_val.currentRow()])
            new_exploit['Source'] = add_misc_exploit_dialog.exploit_source
            self.user_character.misc_exploits.append(new_exploit)
            self.user_character.misc_exploits.sort(key=lambda x: x['Name'])
            self.update_overview_tab()
            self.update_exploits_tab()

            exploit = self.lw_exploits_exploits_val.findItems(new_exploit['Name'], QtCore.Qt.MatchExactly)
            if len(exploit) > 0:
                self.lw_exploits_exploits_val.setCurrentItem(exploit[0])

    def remove_misc_exploit(self):
        selected_exploit = self.lw_exploits_exploits_val.currentRow()
        self.user_character.misc_exploits.pop(selected_exploit)
        self.update_overview_tab()
        self.update_exploits_tab()

    def on_misc_exploit_select(self, current_row):
        self.pte_exploits_desc.clear()
        if current_row != -1:
            self.pte_exploits_desc.setPlainText(self.user_character.misc_exploits[current_row]['Desc'])

    ###########################
    # Equipment tab functions #
    ###########################
    #########################
    # General tab functions #
    #########################
    def add_general_gear(self):
        general_gear_dialog = GeneralGearDialog()
        if general_gear_dialog.exec_():
            selected_item = general_gear_dialog.tw_ggd_gear.currentItem()
            item_dict = {'Name': selected_item.text(0),
                         'Cost': int(selected_item.text(1)),
                         'Weight': selected_item.text(2),
                         'Availability': selected_item.text(3),
                         'Quantity': int(general_gear_dialog.sb_ggd_quantity_val.text()),
                         'Source': general_gear_dialog.cb_ggd_category.currentText()}
            self.user_character.equipment['General'].append(item_dict)
            self.user_character.equipment['General'].sort(key=lambda x: x['Name'])
            self.update_general_equipment_tab()
            self.update_overview_tab()

    def remove_general_gear(self):
        self.user_character.equipment['General'].pop(self.tw_eq_gn_val.currentIndex().row())
        self.update_general_equipment_tab()
        self.update_overview_tab()

    #########################
    # Weapons tab functions #
    #########################
    def add_weapon(self):
        weapon_dialog = WeaponDialog()
        if weapon_dialog.exec_():
            selected_item = weapon_dialog.tw_wd_gear.currentItem()
            item_dict = {'Name': selected_item.text(0),
                         'Damage': selected_item.text(1),
                         'Type': selected_item.text(2),
                         'Range': selected_item.text(3),
                         'Base Cost': int(selected_item.text(4)),
                         'Cost': int(weapon_dialog.item_cost),
                         'Size': selected_item.text(5),
                         'Weight': int(selected_item.text(6)),
                         'Availability': selected_item.text(7),
                         'Special': selected_item.text(8),
                         'Quantity': int(weapon_dialog.sb_wd_quantity_val.text()),
                         'Quality': weapon_dialog.cb_wd_quality_val.currentText(),
                         'Ammunition': [],
                         'Source': weapon_dialog.cb_wd_category.currentText()}
            self.user_character.equipment['Weapons'].append(item_dict)
            self.user_character.equipment['Weapons'].sort(key=lambda x: x['Name'])
            self.update_weapons_equipment_tab()
            self.update_overview_tab()

    def remove_weapon(self):
        self.user_character.equipment['Weapons'].pop(self.tw_eq_wp_val.currentIndex().row())
        self.update_weapons_equipment_tab()
        self.update_overview_tab()

    def add_ammunition(self):
        index = self.tw_eq_wp_val.currentIndex().parent().row()
        if index == -1:
            index = self.tw_eq_wp_val.currentIndex().row()

        ammo_type = self.cb_eq_wp_ammo_type_val.currentText()
        ammo_quantity = self.sb_eq_wp_magazine_val.value()
        ammo_exists = False
        if ammo_type == 'Standard':
            cost = self.user_character.equipment['Weapons'][index]['Base Cost'] // 20
        else:
            cost = 100

        for ammo in self.user_character.equipment['Weapons'][index]['Ammunition']:
            if ammo_type == ammo['Name']:
                ammo_exists = True
                ammo['Quantity'] += ammo_quantity
                break

        if not ammo_exists:
            self.user_character.equipment['Weapons'][index]['Ammunition'].append(
                {'Name': ammo_type,
                 'Quantity': ammo_quantity,
                 'Cost': cost}
            )

        self.user_character.equipment['Weapons'][index]['Ammunition'].sort(key=lambda x: x['Name'])
        self.update_weapons_equipment_tab()
        self.update_overview_tab()
        self.tw_eq_wp_val.setCurrentItem(self.tw_eq_wp_val.topLevelItem(index))

    def remove_ammunition(self):
        parent_index = self.tw_eq_wp_val.currentIndex().parent().row()
        if parent_index > -1:
            child_index = self.tw_eq_wp_val.currentIndex().row()
            self.user_character.equipment['Weapons'][parent_index]['Ammunition'].pop(child_index)
            self.update_weapons_equipment_tab()
            self.update_overview_tab()

    def on_weapon_select(self, current, previous):
        if current is not None:
            parent_index = self.tw_eq_wp_val.currentIndex().parent().row()
            if parent_index > -1:
                self.pb_eq_wp_ammo_remove.setDisabled(False)
            else:
                self.pb_eq_wp_ammo_remove.setDisabled(True)
                item_index = self.tw_eq_wp_val.currentIndex().row()
                if 'ballistic' in self.user_character.equipment['Weapons'][item_index]['Type'].lower():
                    self.gb_eq_wp_ammo.setDisabled(False)
                else:
                    self.gb_eq_wp_ammo.setDisabled(True)


    #######################
    # Armor tab functions #
    #######################
    def add_armor(self):
        armor_dialog = ArmorDialog()
        if armor_dialog.exec_():
            selected_item = armor_dialog.tw_ar_gear.currentItem()
            item_dict = {'Name': selected_item.text(0),
                         'Soak': int(selected_item.text(1)),
                         'Defense': int(selected_item.text(2)),
                         'Base Cost': int(selected_item.text(3)),
                         'Cost': int(armor_dialog.item_cost),
                         'Type': selected_item.text(4),
                         'Weight': int(selected_item.text(5)),
                         'Vulnerable': selected_item.text(6),
                         'Speed': int(selected_item.text(7)),
                         'Special': selected_item.text(8),
                         'Quantity': int(armor_dialog.sb_ar_quantity_val.text()),
                         'Quality': armor_dialog.cb_ar_quality_val.currentText(),
                         'Source': armor_dialog.cb_ar_category.currentText()}
            self.user_character.equipment['Armor'].append(item_dict)
            self.user_character.equipment['Armor'].sort(key=lambda x: x['Name'])
            self.update_armor_equipment_tab()
            self.update_overview_tab()

    def remove_armor(self):
        self.user_character.equipment['Armor'].pop(self.tw_eq_ar_val.currentIndex().row())
        self.update_armor_equipment_tab()
        self.update_overview_tab()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = WCA()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
