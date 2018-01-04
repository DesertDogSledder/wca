from PyQt5 import QtWidgets

from lib.gui_qt.skills_dialog_ui import Ui_SkillsDialog


class SkillsDialog(QtWidgets.QDialog, Ui_SkillsDialog):
    def __init__(self, parent=None):
        super(SkillsDialog, self).__init__(parent)
        self.setupUi(self)

        self.pb_sd_add_skill.clicked.connect(self.add_skill)
        self.pb_sd_remove_rank.clicked.connect(self.remove_rank)
        self.pb_sd_delete_skill.clicked.connect(self.delete_skill)

        self.skills = []

    def add_skill(self):
        skill_to_add = self.le_sd_skill_val.text().lower().strip()

        if skill_to_add != '':
            skill_exists = False
            # If the skill exists, just increment that skill by the number of ranks
            for skill in self.skills:
                if skill_to_add == skill['Name']:
                    skill['Rank'] += self.sb_sd_ranks_val.value()
                    skill_exists = True

            # Otherwise, add it to the list
            if not skill_exists:
                self.skills.append({'Name': skill_to_add, 'Rank': self.sb_sd_ranks_val.value()})
                self.lw_sd_current_skills_val.addItem('{} ({})'.format(skill_to_add, self.sb_sd_ranks_val.value()))

            self.le_sd_skill_val.clear()
            self.sb_sd_ranks_val.setValue(1)
            self.regenerate_list()

    def remove_rank(self):
        index = self.lw_sd_current_skills_val.currentRow()
        if self.skills[index]['Rank'] <= 1:
            self.skills.pop(index)
            popped = True
        else:
            self.skills[index]['Rank'] -= 1
            popped = False

        self.regenerate_list()
        if self.lw_sd_current_skills_val.count() > 0:
            if popped:
                if index > 0:
                    self.lw_sd_current_skills_val.setCurrentRow(index-1)
                else:
                    self.lw_sd_current_skills_val.setCurrentRow(0)
            else:
                self.lw_sd_current_skills_val.setCurrentRow(index)

    def delete_skill(self):
        index = self.lw_sd_current_skills_val.currentRow()
        self.skills.pop(index)
        self.regenerate_list()
        if self.lw_sd_current_skills_val.count() > 0:
            if index > 0:
                self.lw_sd_current_skills_val.setCurrentRow(index-1)
            else:
                self.lw_sd_current_skills_val.setCurrentRow(0)

    def regenerate_list(self):
        self.lw_sd_current_skills_val.clear()
        self.skills.sort(key=lambda x: x['Name'])
        for skill in self.skills:
            self.lw_sd_current_skills_val.addItem('{} ({})'.format(skill['Name'], skill['Rank']))
