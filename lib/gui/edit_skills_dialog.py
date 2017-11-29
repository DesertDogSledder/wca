# -*- coding: utf-8 -*-

import wx
import wx.xrc


###########################################################################
## Class EditSkillsDialog
###########################################################################

class EditSkillsDialog(wx.Dialog):
    def __init__(self, parent, available_skills=[]):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Edit Skills", pos=wx.DefaultPosition,
                           size=wx.Size(604, 433), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_esd_main = wx.BoxSizer(wx.VERTICAL)

        self.p_esd_edit_skills = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_esd_1 = wx.BoxSizer(wx.VERTICAL)

        sbs_esd_available_skills = wx.StaticBoxSizer(
            wx.StaticBox(self.p_esd_edit_skills, wx.ID_ANY, u"Available Skills"), wx.VERTICAL)

        self.tc_esd_available_skills = wx.TextCtrl(sbs_esd_available_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                   wx.DefaultPosition, wx.Size(-1, 100),
                                                   wx.TE_MULTILINE | wx.TE_READONLY)
        sbs_esd_available_skills.Add(self.tc_esd_available_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_esd_1.Add(sbs_esd_available_skills, 1, wx.EXPAND, 5)

        bs_esd_skills = wx.BoxSizer(wx.HORIZONTAL)

        b_esd_skills_list = wx.BoxSizer(wx.VERTICAL)

        lb_esd_skills_listChoices = []
        self.lb_esd_skills_list = wx.ListBox(self.p_esd_edit_skills, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             lb_esd_skills_listChoices, wx.LB_SORT)
        self.lb_esd_skills_list.SetMinSize(wx.Size(160, 150))

        b_esd_skills_list.Add(self.lb_esd_skills_list, 0, wx.ALL, 5)

        self.b_esd_remove_skill = wx.Button(self.p_esd_edit_skills, wx.ID_ANY, u"Remove Skill", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        b_esd_skills_list.Add(self.b_esd_remove_skill, 0, wx.ALL, 5)

        bs_esd_skills.Add(b_esd_skills_list, 1, wx.EXPAND, 5)

        bs_esd_add_skill = wx.BoxSizer(wx.VERTICAL)

        self.tc_esd_skill = wx.TextCtrl(self.p_esd_edit_skills, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bs_esd_add_skill.Add(self.tc_esd_skill, 0, wx.ALL, 5)

        self.b_esd_add_skill = wx.Button(self.p_esd_edit_skills, wx.ID_ANY, u"Add Skill", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_esd_add_skill.Add(self.b_esd_add_skill, 0, wx.ALL, 5)

        bs_esd_skills.Add(bs_esd_add_skill, 1, wx.EXPAND, 5)

        bs_esd_1.Add(bs_esd_skills, 1, wx.EXPAND, 5)

        bs_esd_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_esd_ok = wx.Button(self.p_esd_edit_skills, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_esd_buttons.Add(self.b_esd_ok, 0, wx.ALL, 5)

        self.b_esd_cancel = wx.Button(self.p_esd_edit_skills, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bs_esd_buttons.Add(self.b_esd_cancel, 0, wx.ALL, 5)

        bs_esd_1.Add(bs_esd_buttons, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)

        self.p_esd_edit_skills.SetSizer(bs_esd_1)
        self.p_esd_edit_skills.Layout()
        bs_esd_1.Fit(self.p_esd_edit_skills)
        bs_esd_main.Add(self.p_esd_edit_skills, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_esd_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.b_esd_remove_skill.Bind(wx.EVT_BUTTON, self.remove_skill)
        self.tc_esd_skill.Bind(wx.EVT_TEXT_ENTER, self.add_skill)
        self.b_esd_add_skill.Bind(wx.EVT_BUTTON, self.add_skill)
        self.b_esd_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_esd_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.available_skills_str = ''
        for skill in available_skills:
            self.available_skills_str += '{}, '.format(skill)
        self.tc_esd_available_skills.SetValue(self.available_skills_str[:-2])

    def __del__(self):
        pass

    ##########################################
    # Additional EditSkillsDialog init stuff #
    ##########################################
    # self.available_skills_str = ''
    # for skill in available_skills:
    #     self.available_skills_str += '{}, '.format(skill)
    # self.tc_esd_available_skills.SetValue(self.available_skills_str[:-2])

    ##############################
    # EditSkillsDialog Functions #
    ##############################
    def remove_skill(self, event):
        self.lb_esd_skills_list.Delete(self.lb_esd_skills_list.GetSelection())

    def add_skill(self, event):
        skill = self.tc_esd_skill.GetValue().lower().strip()
        if skill != '':
            self.lb_esd_skills_list.Append(skill)
        self.tc_esd_skill.Clear()

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)