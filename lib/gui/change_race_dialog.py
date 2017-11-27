# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.lib.intctrl
from data.races import *
try:
    from data.custom import custom_races
    custom_races_loaded = True
except ImportError:
    custom_races_loaded = False


###########################################################################
## Class ChangeRaceDialog
###########################################################################

class ChangeRaceDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Change Race", pos=wx.DefaultPosition,
                           size=wx.Size(765, 649), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_crd_main = wx.BoxSizer(wx.VERTICAL)

        self.p_crd_change_race = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_crd_1 = wx.BoxSizer(wx.VERTICAL)

        bs_crd_race_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_crd_race = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Race"), wx.HORIZONTAL)

        bs_crd_rb = wx.BoxSizer(wx.VERTICAL)

        self.rb_crd_old = wx.RadioButton(sbs_crd_race.GetStaticBox(), wx.ID_ANY, u"OLD", wx.DefaultPosition,
                                         wx.DefaultSize, wx.RB_GROUP)
        self.rb_crd_old.SetValue(True)
        bs_crd_rb.Add(self.rb_crd_old, 0, wx.ALL, 5)

        self.rb_crd_now = wx.RadioButton(sbs_crd_race.GetStaticBox(), wx.ID_ANY, u"NOW", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_crd_rb.Add(self.rb_crd_now, 0, wx.ALL, 5)

        self.rb_crd_new = wx.RadioButton(sbs_crd_race.GetStaticBox(), wx.ID_ANY, u"NEW", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_crd_rb.Add(self.rb_crd_new, 0, wx.ALL, 5)

        self.rb_crd_custom = wx.RadioButton(sbs_crd_race.GetStaticBox(), wx.ID_ANY, u"Custom", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bs_crd_rb.Add(self.rb_crd_custom, 0, wx.ALL, 5)

        sbs_crd_race.Add(bs_crd_rb, 0, wx.EXPAND, 5)

        lb_crd_race_listChoices = []
        self.lb_crd_race_list = wx.ListBox(sbs_crd_race.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           lb_crd_race_listChoices, 0)
        self.lb_crd_race_list.SetMinSize(wx.Size(-1, 120))

        sbs_crd_race.Add(self.lb_crd_race_list, 0, wx.ALL, 5)

        bs_crd_race_desc.Add(sbs_crd_race, 0, wx.EXPAND, 5)

        sbs_crd_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Description"), wx.VERTICAL)

        self.tc_crd_race_desc = wx.TextCtrl(sbs_crd_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_crd_race_desc.SetMinSize(wx.Size(-1, 120))

        sbs_crd_desc.Add(self.tc_crd_race_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_crd_race_desc.Add(sbs_crd_desc, 1, wx.EXPAND, 5)

        bs_crd_1.Add(bs_crd_race_desc, 1, wx.EXPAND, 5)

        sbs_crd_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Available Skills"),
                                           wx.VERTICAL)

        self.tc_crd_skills = wx.TextCtrl(sbs_crd_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_crd_skills.SetMinSize(wx.Size(-1, 70))

        sbs_crd_skills.Add(self.tc_crd_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_crd_1.Add(sbs_crd_skills, 0, wx.EXPAND, 5)

        bsb_crd_exploits_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_crd_exploit_names = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Exploits"),
                                                  wx.VERTICAL)

        lb_crd_exploit_listChoices = []
        self.lb_crd_exploit_list = wx.ListBox(sbs_crd_exploit_names.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                              wx.DefaultSize, lb_crd_exploit_listChoices, 0)
        self.lb_crd_exploit_list.SetMinSize(wx.Size(-1, 140))

        sbs_crd_exploit_names.Add(self.lb_crd_exploit_list, 0, wx.ALL | wx.EXPAND, 5)

        bsb_crd_exploits_desc.Add(sbs_crd_exploit_names, 1, wx.EXPAND, 5)

        sbs_crd_exploit_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Description"),
                                                 wx.VERTICAL)

        self.tc_crd_exploit_desc = wx.TextCtrl(sbs_crd_exploit_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_crd_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_crd_exploit_desc.Add(self.tc_crd_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bsb_crd_exploits_desc.Add(sbs_crd_exploit_desc, 2, wx.EXPAND, 5)

        bs_crd_1.Add(bsb_crd_exploits_desc, 1, wx.EXPAND, 5)

        sbs_crd_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_crd_change_race, wx.ID_ANY, u"Stats"), wx.VERTICAL)

        gs_crd_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_crd_str = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_str.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_str, 0, wx.ALL, 5)

        self.st_crd_agi = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_agi.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_agi, 0, wx.ALL, 5)

        self.st_crd_end = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_end.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_end, 0, wx.ALL, 5)

        self.st_crd_int = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_int.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_int, 0, wx.ALL, 5)

        self.st_crd_log = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_log.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_log, 0, wx.ALL, 5)

        self.st_crd_wil = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_wil.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_wil, 0, wx.ALL, 5)

        self.st_crd_cha = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_cha.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_cha, 0, wx.ALL, 5)

        self.st_crd_luc = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_luc.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_luc, 0, wx.ALL, 5)

        self.st_crd_rep = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_rep.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_rep, 0, wx.ALL, 5)

        self.st_crd_mag = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_mag.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_mag, 0, wx.ALL, 5)

        self.st_crd_chi = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_chi.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_chi, 0, wx.ALL, 5)

        self.st_crd_psi = wx.StaticText(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_crd_psi.Wrap(-1)
        gs_crd_stats.Add(self.st_crd_psi, 0, wx.ALL, 5)

        self.ic_crd_str = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_str.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_str, 0, wx.ALL, 5)

        self.ic_crd_agi = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_agi.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_agi, 0, wx.ALL, 5)

        self.ic_crd_end = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_end.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_end, 0, wx.ALL, 5)

        self.ic_crd_int = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_int.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_int, 0, wx.ALL, 5)

        self.ic_crd_log = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_log.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_log, 0, wx.ALL, 5)

        self.ic_crd_wil = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_wil.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_wil, 0, wx.ALL, 5)

        self.ic_crd_cha = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_cha.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_cha, 0, wx.ALL, 5)

        self.ic_crd_luc = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_luc.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_luc, 0, wx.ALL, 5)

        self.ic_crd_rep = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_rep.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_rep, 0, wx.ALL, 5)

        self.ic_crd_mag = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_mag.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_mag, 0, wx.ALL, 5)

        self.ic_crd_chi = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_chi.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_chi, 0, wx.ALL, 5)

        self.ic_crd_psi = wx.lib.intctrl.IntCtrl(sbs_crd_stats.GetStaticBox(), wx.ID_ANY, 0, wx.DefaultPosition,
                                                 (25, -1), 0)
        # self.ic_crd_psi.Wrap(-1)
        gs_crd_stats.Add(self.ic_crd_psi, 0, wx.ALL, 5)

        sbs_crd_stats.Add(gs_crd_stats, 0, wx.EXPAND, 5)

        bs_crd_1.Add(sbs_crd_stats, 0, wx.EXPAND, 5)

        bs_crd_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_crd_ok = wx.Button(self.p_crd_change_race, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_crd_buttons.Add(self.b_crd_ok, 0, wx.ALL, 5)

        self.b_crd_cancel = wx.Button(self.p_crd_change_race, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bs_crd_buttons.Add(self.b_crd_cancel, 0, wx.ALL, 5)

        bs_crd_1.Add(bs_crd_buttons, 0, wx.ALIGN_RIGHT, 5)

        self.p_crd_change_race.SetSizer(bs_crd_1)
        self.p_crd_change_race.Layout()
        bs_crd_1.Fit(self.p_crd_change_race)
        bs_crd_main.Add(self.p_crd_change_race, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_crd_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.rb_crd_old.Bind(wx.EVT_RADIOBUTTON, self.show_races)
        self.rb_crd_now.Bind(wx.EVT_RADIOBUTTON, self.show_races)
        self.rb_crd_new.Bind(wx.EVT_RADIOBUTTON, self.show_races)
        self.rb_crd_custom.Bind(wx.EVT_RADIOBUTTON, self.show_races)
        self.lb_crd_race_list.Bind(wx.EVT_LISTBOX, self.on_race_select)
        self.lb_crd_exploit_list.Bind(wx.EVT_LISTBOX, self.on_exploit_select)
        self.b_crd_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_crd_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.rb_crd_old.SetValue(True)
        self.show_races(None)
        if not custom_races_loaded:
            self.rb_crd_custom.Enable(False)
            self.rb_crd_custom.Hide()

    def __del__(self):
        pass

    ##########################################
    # Additional ChangeRaceDialog init stuff #
    ##########################################
    # self.rb_crd_old.SetValue(True)
    # self.show_races(None)
    # if not custom_races_loaded:
    #     self.rb_crd_custom.Enable(False)
    #     self.rb_crd_custom.Hide()

    ##############################
    # ChangeRaceDialog Functions #
    ##############################
    def get_race_list(self):
        race_list = None
        if self.rb_crd_old.GetValue():
            race_list = races_old.race_old_list
        elif self.rb_crd_now.GetValue():
            race_list = races_now.race_now_list
        elif self.rb_crd_new.GetValue():
            race_list = races_new.race_new_list
        elif self.rb_crd_custom.GetValue():
            race_list = custom_races.custom_race_list
        return race_list

    def get_list_source(self):
        list_source = None
        if self.rb_crd_old.GetValue():
            list_source = 'old'
        elif self.rb_crd_now.GetValue():
            list_source = 'now'
        elif self.rb_crd_new.GetValue():
            list_source = 'new'
        elif self.rb_crd_custom.GetValue():
            list_source = 'custom'
        return list_source

    def show_races(self, event):
        race_list = self.get_race_list()
        self.lb_crd_race_list.Clear()
        for race in race_list:
            self.lb_crd_race_list.Append(race.name)

        self.lb_crd_race_list.SetSelection(0)
        self.on_race_select(None)

    def on_race_select(self, event):
        race_list = self.get_race_list()
        selected_race = self.lb_crd_race_list.GetSelection()
        self.lb_crd_exploit_list.Clear()
        self.tc_crd_exploit_desc.Clear()

        skill_list = ''
        for skill in race_list[selected_race].available_skills:
            skill_list += '{}, '.format(skill)
        self.tc_crd_skills.SetLabel(skill_list[:-2])

        for exploit in race_list[selected_race].exploits:
            self.lb_crd_exploit_list.Append(exploit['Name'])

        self.tc_crd_race_desc.SetValue(race_list[selected_race].desc)

        self.ic_crd_str.SetValue(race_list[selected_race].stats['STR'])
        self.ic_crd_agi.SetValue(race_list[selected_race].stats['AGI'])
        self.ic_crd_end.SetValue(race_list[selected_race].stats['END'])
        self.ic_crd_int.SetValue(race_list[selected_race].stats['INT'])
        self.ic_crd_log.SetValue(race_list[selected_race].stats['LOG'])
        self.ic_crd_wil.SetValue(race_list[selected_race].stats['WIL'])
        self.ic_crd_cha.SetValue(race_list[selected_race].stats['CHA'])
        self.ic_crd_luc.SetValue(race_list[selected_race].stats['LUC'])
        self.ic_crd_rep.SetValue(race_list[selected_race].stats['REP'])
        self.ic_crd_mag.SetValue(race_list[selected_race].stats['MAG'])
        self.ic_crd_chi.SetValue(race_list[selected_race].stats['CHI'])
        self.ic_crd_psi.SetValue(race_list[selected_race].stats['PSI'])

    def on_exploit_select(self, event):
        race_list = self.get_race_list()
        selected_exploit = self.lb_crd_exploit_list.GetSelection()

        self.tc_crd_exploit_desc.SetValue(
            race_list[self.lb_crd_race_list.GetSelection()].exploits[selected_exploit]['Desc'])

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)