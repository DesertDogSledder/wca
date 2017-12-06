# -*- coding: utf-8 -*-

import wx
import wx.xrc
from data.homeworlds import *
try:
    from custom import custom_homeworlds
    custom_homeworlds_loaded = True
except ImportError:
    custom_homeworlds_loaded = False

###########################################################################
## Class ChangeHomeworldDialog
###########################################################################

class ChangeHomeworldDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Change Homeworld", pos=wx.DefaultPosition,
                           size=wx.Size(765, 379), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_chd_main = wx.BoxSizer(wx.VERTICAL)

        self.p_chd_change_homeworld = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_chd_1 = wx.BoxSizer(wx.VERTICAL)

        bs_chd_race_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_chd_homeworld = wx.StaticBoxSizer(wx.StaticBox(self.p_chd_change_homeworld, wx.ID_ANY, u"Homeworld"),
                                              wx.HORIZONTAL)

        bs_chd_rb = wx.BoxSizer(wx.VERTICAL)

        self.rb_chd_new = wx.RadioButton(sbs_chd_homeworld.GetStaticBox(), wx.ID_ANY, u"NEW", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_chd_rb.Add(self.rb_chd_new, 0, wx.ALL, 5)

        self.rb_chd_custom = wx.RadioButton(sbs_chd_homeworld.GetStaticBox(), wx.ID_ANY, u"Custom", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bs_chd_rb.Add(self.rb_chd_custom, 0, wx.ALL, 5)

        sbs_chd_homeworld.Add(bs_chd_rb, 0, wx.EXPAND, 5)

        lb_chd_homeworld_listChoices = []
        self.lb_chd_homeworld_list = wx.ListBox(sbs_chd_homeworld.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                                wx.DefaultSize, lb_chd_homeworld_listChoices, 0)
        self.lb_chd_homeworld_list.SetMinSize(wx.Size(-1, 120))

        sbs_chd_homeworld.Add(self.lb_chd_homeworld_list, 0, wx.ALL, 5)

        bs_chd_race_desc.Add(sbs_chd_homeworld, 0, wx.EXPAND, 5)

        sbs_chd_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_chd_change_homeworld, wx.ID_ANY, u"Available Skills"),
                                           wx.VERTICAL)

        self.tc_chd_skills = wx.TextCtrl(sbs_chd_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_chd_skills.SetMinSize(wx.Size(-1, 70))

        sbs_chd_skills.Add(self.tc_chd_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_chd_race_desc.Add(sbs_chd_skills, 1, wx.EXPAND, 5)

        bs_chd_1.Add(bs_chd_race_desc, 1, wx.EXPAND, 5)

        sbs_chd_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_chd_change_homeworld, wx.ID_ANY, u"Stats"), wx.VERTICAL)

        gs_chd_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_chd_str = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_str.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_str, 0, wx.ALL, 5)

        self.st_chd_agi = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_agi.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_agi, 0, wx.ALL, 5)

        self.st_chd_end = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_end.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_end, 0, wx.ALL, 5)

        self.st_chd_int = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_int.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_int, 0, wx.ALL, 5)

        self.st_chd_log = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_log.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_log, 0, wx.ALL, 5)

        self.st_chd_wil = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_wil.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_wil, 0, wx.ALL, 5)

        self.st_chd_cha = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_cha.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_cha, 0, wx.ALL, 5)

        self.st_chd_luc = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_luc.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_luc, 0, wx.ALL, 5)

        self.st_chd_rep = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_rep.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_rep, 0, wx.ALL, 5)

        self.st_chd_mag = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_mag.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_mag, 0, wx.ALL, 5)

        self.st_chd_chi = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_chi.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_chi, 0, wx.ALL, 5)

        self.st_chd_psi = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_chd_psi.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_psi, 0, wx.ALL, 5)

        self.st_chd_str_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"str_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_str_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_str_val, 0, wx.ALL, 5)

        self.st_chd_agi_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"agi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_agi_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_agi_val, 0, wx.ALL, 5)

        self.st_chd_end_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"end_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_end_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_end_val, 0, wx.ALL, 5)

        self.st_chd_int_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"int_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_int_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_int_val, 0, wx.ALL, 5)

        self.st_chd_log_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"log_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_log_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_log_val, 0, wx.ALL, 5)

        self.st_chd_wil_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"wil_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_wil_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_wil_val, 0, wx.ALL, 5)

        self.st_chd_cha_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"cha_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_cha_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_cha_val, 0, wx.ALL, 5)

        self.st_chd_luc_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"luc_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_luc_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_luc_val, 0, wx.ALL, 5)

        self.st_chd_rep_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"rep_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_rep_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_rep_val, 0, wx.ALL, 5)

        self.st_chd_mag_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"mag_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_mag_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_mag_val, 0, wx.ALL, 5)

        self.st_chd_chi_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"chi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_chi_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_chi_val, 0, wx.ALL, 5)

        self.st_chd_psi_val = wx.StaticText(sbs_chd_stats.GetStaticBox(), wx.ID_ANY, u"psi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_chd_psi_val.Wrap(-1)
        gs_chd_stats.Add(self.st_chd_psi_val, 0, wx.ALL, 5)

        sbs_chd_stats.Add(gs_chd_stats, 0, wx.EXPAND, 5)

        bs_chd_1.Add(sbs_chd_stats, 0, wx.EXPAND, 5)

        bs_chd_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_chd_ok = wx.Button(self.p_chd_change_homeworld, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_chd_buttons.Add(self.b_chd_ok, 0, wx.ALL, 5)

        self.b_chd_cancel = wx.Button(self.p_chd_change_homeworld, wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bs_chd_buttons.Add(self.b_chd_cancel, 0, wx.ALL, 5)

        bs_chd_1.Add(bs_chd_buttons, 0, wx.ALIGN_RIGHT, 5)

        self.p_chd_change_homeworld.SetSizer(bs_chd_1)
        self.p_chd_change_homeworld.Layout()
        bs_chd_1.Fit(self.p_chd_change_homeworld)
        bs_chd_main.Add(self.p_chd_change_homeworld, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_chd_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.rb_chd_new.Bind(wx.EVT_RADIOBUTTON, self.show_homeworlds)
        self.rb_chd_custom.Bind(wx.EVT_RADIOBUTTON, self.show_homeworlds)
        self.lb_chd_homeworld_list.Bind(wx.EVT_LISTBOX, self.on_homeworld_select)
        self.b_chd_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_chd_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        if not custom_homeworlds_loaded:
            self.rb_chd_custom.Enable(False)
            self.rb_chd_custom.Hide()

    def __del__(self):
        pass

    ###################################
    # ChangeHomeworldDialog Functions #
    ###################################
    def get_homeworld_list(self):
        homeworld_list = None
        if self.rb_chd_new.GetValue():
            homeworld_list = homeworlds_new.homeworld_new_list
        elif self.rb_chd_custom.GetValue():
            homeworld_list = custom_homeworlds.custom_homeworld_list
        return homeworld_list

    def get_list_source(self):
        list_source = None
        if self.rb_chd_new.GetValue():
            list_source = 'new'
        elif self.rb_chd_custom.GetValue():
            list_source = 'custom'
        return list_source

    def show_homeworlds(self, event):
        homeworld_list = self.get_homeworld_list()
        self.lb_chd_homeworld_list.Clear()

        for homeworld in homeworld_list:
            self.lb_chd_homeworld_list.Append(homeworld.name)

    def on_homeworld_select(self, event):
        homeworld_list = self.get_homeworld_list()
        selected_homeworld = self.lb_chd_homeworld_list.GetSelection()

        skill_list = ''
        for skill in homeworld_list[selected_homeworld].available_skills:
            skill_list += '{}, '.format(skill)
        self.tc_chd_skills.SetValue(skill_list[:-2])

        self.st_chd_str_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['STR']))
        self.st_chd_agi_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['AGI']))
        self.st_chd_end_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['END']))
        self.st_chd_int_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['INT']))
        self.st_chd_log_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['LOG']))
        self.st_chd_wil_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['WIL']))
        self.st_chd_cha_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['CHA']))
        self.st_chd_luc_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['LUC']))
        self.st_chd_rep_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['REP']))
        self.st_chd_mag_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['MAG']))
        self.st_chd_chi_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['CHI']))
        self.st_chd_psi_val.SetLabel('{:+d}'.format(homeworld_list[selected_homeworld].stats['PSI']))

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)