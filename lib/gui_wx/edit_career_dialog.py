# -*- coding: utf-8 -*-

import wx
import wx.lib.intctrl
import wx.xrc

from data.careers import *

try:
    from custom import custom_careers
    custom_careers_loaded = True
except ImportError:
    custom_careers_loaded = False


###########################################################################
## Class EditCareerDialog
###########################################################################

class EditCareerDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Edit Career", pos=wx.DefaultPosition,
                           size=wx.Size(765, 649), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_ecd_main = wx.BoxSizer(wx.VERTICAL)

        self.p_ecd_edit_career = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_ecd_1 = wx.BoxSizer(wx.VERTICAL)

        bs_ecd_career_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_ecd_careers = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Careers"), wx.HORIZONTAL)

        bs_ecd_rb = wx.BoxSizer(wx.VERTICAL)

        self.rb_ecd_origins = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"Origins", wx.DefaultPosition,
                                             wx.DefaultSize, wx.RB_GROUP)
        bs_ecd_rb.Add(self.rb_ecd_origins, 0, wx.ALL, 5)

        self.rb_ecd_old = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"OLD", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_ecd_rb.Add(self.rb_ecd_old, 0, wx.ALL, 5)

        self.rb_ecd_now = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"NOW", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_ecd_rb.Add(self.rb_ecd_now, 0, wx.ALL, 5)

        self.rb_ecd_new = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"NEW", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_ecd_rb.Add(self.rb_ecd_new, 0, wx.ALL, 5)

        self.rb_ecd_ma = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"Martial Arts", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bs_ecd_rb.Add(self.rb_ecd_ma, 0, wx.ALL, 5)

        self.rb_ecd_custom = wx.RadioButton(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, u"Custom", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bs_ecd_rb.Add(self.rb_ecd_custom, 0, wx.ALL, 5)

        sbs_ecd_careers.Add(bs_ecd_rb, 0, wx.EXPAND, 5)

        lb_ecd_career_listChoices = []
        self.lb_ecd_career_list = wx.ListBox(sbs_ecd_careers.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                             wx.DefaultSize, lb_ecd_career_listChoices, 0)
        self.lb_ecd_career_list.SetMinSize(wx.Size(-1, 120))

        sbs_ecd_careers.Add(self.lb_ecd_career_list, 0, wx.ALL, 5)

        bs_ecd_career_desc.Add(sbs_ecd_careers, 0, wx.EXPAND, 5)

        sbs_ecd_career_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Career Description"),
                                                wx.VERTICAL)

        self.tc_ecd_career_desc = wx.TextCtrl(sbs_ecd_career_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.Size(-1, 170), wx.TE_MULTILINE | wx.TE_READONLY)
        sbs_ecd_career_desc.Add(self.tc_ecd_career_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_ecd_career_desc.Add(sbs_ecd_career_desc, 1, wx.EXPAND, 5)

        bs_ecd_1.Add(bs_ecd_career_desc, 1, wx.EXPAND, 5)

        sbs_ecd_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Available Skills"),
                                           wx.VERTICAL)

        self.tc_ecd_skills = wx.TextCtrl(sbs_ecd_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_ecd_skills.SetMinSize(wx.Size(-1, 70))

        sbs_ecd_skills.Add(self.tc_ecd_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_ecd_1.Add(sbs_ecd_skills, 0, wx.EXPAND, 5)

        bs_ecd_exploits_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_ecd_exploit_names = wx.StaticBoxSizer(
            wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Available Exploits"), wx.VERTICAL)

        lb_ecd_exploit_listChoices = []
        self.lb_ecd_exploit_list = wx.ListBox(sbs_ecd_exploit_names.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                              wx.DefaultSize, lb_ecd_exploit_listChoices, 0)
        self.lb_ecd_exploit_list.SetMinSize(wx.Size(-1, 140))

        sbs_ecd_exploit_names.Add(self.lb_ecd_exploit_list, 0, wx.ALL | wx.EXPAND, 5)

        bs_ecd_exploits_desc.Add(sbs_ecd_exploit_names, 1, wx.EXPAND, 5)

        sbs_ecd_exploit_desc = wx.StaticBoxSizer(
            wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Exploit Description"), wx.VERTICAL)

        self.tc_ecd_exploit_desc = wx.TextCtrl(sbs_ecd_exploit_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_ecd_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_ecd_exploit_desc.Add(self.tc_ecd_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_ecd_exploits_desc.Add(sbs_ecd_exploit_desc, 2, wx.EXPAND, 5)

        bs_ecd_1.Add(bs_ecd_exploits_desc, 1, wx.EXPAND, 5)

        sbs_ecd_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Stats"), wx.VERTICAL)

        gs_ecd_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_ecd_str = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_str.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_str, 0, wx.ALL, 5)

        self.st_ecd_agi = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_agi.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_agi, 0, wx.ALL, 5)

        self.st_ecd_end = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_end.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_end, 0, wx.ALL, 5)

        self.st_ecd_int = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_int.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_int, 0, wx.ALL, 5)

        self.st_ecd_log = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_log.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_log, 0, wx.ALL, 5)

        self.st_ecd_wil = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_wil.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_wil, 0, wx.ALL, 5)

        self.st_ecd_cha = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_cha.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_cha, 0, wx.ALL, 5)

        self.st_ecd_luc = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_luc.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_luc, 0, wx.ALL, 5)

        self.st_ecd_rep = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_rep.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_rep, 0, wx.ALL, 5)

        self.st_ecd_mag = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_mag.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_mag, 0, wx.ALL, 5)

        self.st_ecd_chi = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_chi.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_chi, 0, wx.ALL, 5)

        self.st_ecd_psi = wx.StaticText(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_ecd_psi.Wrap(-1)
        gs_ecd_stats.Add(self.st_ecd_psi, 0, wx.ALL, 5)

        self.ic_ecd_str = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_str, 0, wx.ALL, 5)

        self.ic_ecd_agi = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_agi, 0, wx.ALL, 5)

        self.ic_ecd_end = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_end, 0, wx.ALL, 5)

        self.ic_ecd_int = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_int, 0, wx.ALL, 5)

        self.ic_ecd_log = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_log, 0, wx.ALL, 5)

        self.ic_ecd_wil = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_wil, 0, wx.ALL, 5)

        self.ic_ecd_cha = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_cha, 0, wx.ALL, 5)

        self.ic_ecd_luc = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_luc, 0, wx.ALL, 5)

        self.ic_ecd_rep = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_rep, 0, wx.ALL, 5)

        self.ic_ecd_mag = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_mag, 0, wx.ALL, 5)

        self.ic_ecd_chi = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_chi, 0, wx.ALL, 5)

        self.ic_ecd_psi = wx.lib.intctrl.IntCtrl(sbs_ecd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        gs_ecd_stats.Add(self.ic_ecd_psi, 0, wx.ALL, 5)

        sbs_ecd_stats.Add(gs_ecd_stats, 0, wx.EXPAND, 5)

        bs_ecd_1.Add(sbs_ecd_stats, 0, wx.EXPAND, 5)

        bs_ecd_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_ecd_ok = wx.Button(self.p_ecd_edit_career, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_ecd_buttons.Add(self.b_ecd_ok, 0, wx.ALL, 5)

        self.b_ecd_cancel = wx.Button(self.p_ecd_edit_career, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bs_ecd_buttons.Add(self.b_ecd_cancel, 0, wx.ALL, 5)

        bs_ecd_1.Add(bs_ecd_buttons, 0, wx.ALIGN_RIGHT, 5)

        self.p_ecd_edit_career.SetSizer(bs_ecd_1)
        self.p_ecd_edit_career.Layout()
        bs_ecd_1.Fit(self.p_ecd_edit_career)
        bs_ecd_main.Add(self.p_ecd_edit_career, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_ecd_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.rb_ecd_origins.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.rb_ecd_old.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.rb_ecd_now.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.rb_ecd_new.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.rb_ecd_ma.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.rb_ecd_custom.Bind(wx.EVT_RADIOBUTTON, self.show_careers)
        self.lb_ecd_career_list.Bind(wx.EVT_LISTBOX, self.on_career_select)
        self.lb_ecd_exploit_list.Bind(wx.EVT_LISTBOX, self.on_exploit_select)
        self.b_ecd_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_ecd_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.rb_ecd_origins.SetValue(True)
        self.show_careers(None)
        if not custom_careers_loaded:
            self.rb_ecd_custom.Enable(False)
            self.rb_ecd_custom.Hide()

    def __del__(self):
        pass

    ##########################################
    # Additional EditCareerDialog init stuff #
    ##########################################
    # self.rb_ecd_origins.SetValue(True)
    # self.show_careers(None)

    # if not custom_careers_loaded:
    #     self.rb_ecd_custom.Enable(False)
    #     self.rb_ecd_custom.Hide()

    ##############################
    # EditCareerDialog Functions #
    ##############################
    def get_career_list(self):
        career_list = None
        if self.rb_ecd_origins.GetValue():
            career_list = origins.career_woin_origin_list
        elif self.rb_ecd_old.GetValue():
            career_list = careers_old.career_old_list
        elif self.rb_ecd_now.GetValue():
            career_list = careers_now.career_now_list
        elif self.rb_ecd_new.GetValue():
            career_list = careers_new.career_new_list
        elif self.rb_ecd_ma.GetValue():
            career_list = careers_martial_arts.career_ma_list
        elif self.rb_ecd_custom.GetValue():
            career_list = custom_careers.custom_career_list
        return career_list

    def get_list_source(self):
        list_source = None
        if self.rb_ecd_origins.GetValue():
            list_source = 'origins'
        elif self.rb_ecd_old.GetValue():
            list_source = 'old'
        elif self.rb_ecd_now.GetValue():
            list_source = 'now'
        elif self.rb_ecd_new.GetValue():
            list_source = 'new'
        elif self.rb_ecd_ma.GetValue():
            list_source = 'martial arts'
        elif self.rb_ecd_custom.GetValue():
            list_source = 'custom'
        return list_source

    def show_careers(self, event):
        career_list = self.get_career_list()

        self.lb_ecd_career_list.Clear()
        self.lb_ecd_exploit_list.Clear()
        self.tc_ecd_skills.Clear()
        self.tc_ecd_exploit_desc.Clear()

        for career in career_list:
            self.lb_ecd_career_list.Append(career.name)

        self.lb_ecd_career_list.SetSelection(0)
        self.on_career_select(None)

    def on_career_select(self, event):
        career_list = self.get_career_list()
        selected_career = self.lb_ecd_career_list.GetSelection()

        self.tc_ecd_career_desc.SetValue('Prerequisites: {}\n\n{}'.format(career_list[selected_career].prereq,
                                                                          career_list[selected_career].desc))

        self.lb_ecd_exploit_list.Clear()

        skill_list = ''
        for skill in career_list[selected_career].available_skills:
            skill_list += '{}, '.format(skill)
        self.tc_ecd_skills.SetValue(skill_list[:-2])

        for exploit in career_list[selected_career].available_exploits:
            self.lb_ecd_exploit_list.Append(exploit['Name'])

        self.ic_ecd_str.SetValue(career_list[selected_career].stats['STR'])
        self.ic_ecd_agi.SetValue(career_list[selected_career].stats['AGI'])
        self.ic_ecd_end.SetValue(career_list[selected_career].stats['END'])
        self.ic_ecd_int.SetValue(career_list[selected_career].stats['INT'])
        self.ic_ecd_log.SetValue(career_list[selected_career].stats['LOG'])
        self.ic_ecd_wil.SetValue(career_list[selected_career].stats['WIL'])
        self.ic_ecd_cha.SetValue(career_list[selected_career].stats['CHA'])
        self.ic_ecd_luc.SetValue(career_list[selected_career].stats['LUC'])
        self.ic_ecd_rep.SetValue(career_list[selected_career].stats['REP'])
        self.ic_ecd_mag.SetValue(career_list[selected_career].stats['MAG'])
        self.ic_ecd_chi.SetValue(career_list[selected_career].stats['CHI'])
        self.ic_ecd_psi.SetValue(career_list[selected_career].stats['PSI'])

    def on_exploit_select(self, event):
        career_list = self.get_career_list()
        selected_career = self.lb_ecd_career_list.GetSelection()
        selected_exploit = self.lb_ecd_exploit_list.GetSelection()

        self.tc_ecd_exploit_desc.SetValue(
            career_list[selected_career].available_exploits[selected_exploit]['Desc'])

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)