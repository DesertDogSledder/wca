import wx.lib.intctrl
import wx.adv
import copy
import pickle
import collections

from data.careers import *
from data.exploits import *
from data.homeworlds import *
from data.races import *
from lib import dice, character

try:
    from data.custom import custom_careers
    custom_careers_loaded = True
except ImportError:
    custom_careers_loaded = False
try:
    from data.custom import custom_exploits
    custom_exploits_loaded = True
except ImportError:
    custom_exploits_loaded = False
try:
    from data.custom import custom_homeworlds
    custom_homeworlds_loaded = True
except ImportError:
    custom_homeworlds_loaded = False
try:
    from data.custom import custom_races
    custom_races_loaded = True
except ImportError:
    custom_races_loaded = False

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class WCA_Frame
###########################################################################

class WCA_Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"WOIN Character Assistant", pos=wx.DefaultPosition,
                          size=wx.Size(686, 684), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar = wx.MenuBar(0)
        self.m_file = wx.Menu()
        self.mi_file_new = wx.MenuItem(self.m_file, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_new)

        self.mi_file_open = wx.MenuItem(self.m_file, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_open)

        self.mi_file_save = wx.MenuItem(self.m_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_save)

        self.mi_file_save_as = wx.MenuItem(self.m_file, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_save_as)
        self.mi_file_save_as.Enable(False)

        self.mi_file_quit = wx.MenuItem(self.m_file, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_quit)

        self.m_menubar.Append(self.m_file, u"File")

        self.SetMenuBar(self.m_menubar)

        self.m_status_bar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        bs_main_window = wx.BoxSizer(wx.VERTICAL)

        self.nb_main = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.p_overview = wx.Panel(self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_overview_main = wx.BoxSizer(wx.VERTICAL)

        bs_overview_info_skills = wx.BoxSizer(wx.HORIZONTAL)

        sbs_overview_info = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Info"), wx.VERTICAL)

        gs_overview_info_1 = wx.GridSizer(4, 0, 0, 0)

        sbs_overview_info.Add(gs_overview_info_1, 1, 0, 5)

        gbs_overview_info_1 = wx.GridBagSizer(0, 0)
        gbs_overview_info_1.SetFlexibleDirection(wx.BOTH)
        gbs_overview_info_1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.st_overview_name = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Name", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_overview_name.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_name, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.tc_overview_name_val = wx.TextCtrl(sbs_overview_info.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gbs_overview_info_1.Add(self.tc_overview_name_val, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_race = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Race", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_overview_race.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_race, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_race_val = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"char_race",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_race_val.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_race_val, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_homeworld = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Homeworld",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_homeworld.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_homeworld, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_homeworld_val = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"char_homeworld",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_homeworld_val.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_homeworld_val, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_trait = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Trait",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_trait.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_trait, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.st_overview_trait_val = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"char_trait",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_trait_val.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_trait_val, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.b_overview_change_trait = wx.Button(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Change Trait",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        gbs_overview_info_1.Add(self.b_overview_change_trait, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        sbs_overview_info.Add(gbs_overview_info_1, 1, wx.EXPAND, 5)

        bs_overview_info_skills.Add(sbs_overview_info, 0, wx.EXPAND, 5)

        sbs_overview_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Skills"), wx.VERTICAL)

        self.tc_overview_skills = wx.TextCtrl(sbs_overview_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_overview_skills.SetMinSize(wx.Size(-1, 130))

        sbs_overview_skills.Add(self.tc_overview_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_overview_info_skills.Add(sbs_overview_skills, 1, wx.EXPAND, 5)

        bs_overview_main.Add(bs_overview_info_skills, 0, wx.EXPAND, 5)

        sbs_overview_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Exploits"), wx.VERTICAL)

        self.tc_overview_exploits = wx.TextCtrl(sbs_overview_exploits.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_overview_exploits.SetMinSize(wx.Size(-1, 100))

        sbs_overview_exploits.Add(self.tc_overview_exploits, 0, wx.ALL | wx.EXPAND, 5)

        bs_overview_main.Add(sbs_overview_exploits, 2, wx.EXPAND, 5)

        sbs_overview_derived_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Derived Stats"),
                                                       wx.VERTICAL)

        self.tc_overview_derived_stats = wx.TextCtrl(sbs_overview_derived_stats.GetStaticBox(), wx.ID_ANY,
                                                     wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_overview_derived_stats.SetMinSize(wx.Size(-1, 100))

        sbs_overview_derived_stats.Add(self.tc_overview_derived_stats, 0, wx.ALL | wx.EXPAND, 5)

        bs_overview_main.Add(sbs_overview_derived_stats, 1, wx.EXPAND, 5)

        sbs_overview_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Total Stats"), wx.VERTICAL)

        gs_overview_stats_1 = wx.GridSizer(0, 12, 0, 0)

        self.st_total_str = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_str.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_str, 0, wx.ALL, 5)

        self.st_total_agi = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_agi.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_agi, 0, wx.ALL, 5)

        self.st_total_end = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_end.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_end, 0, wx.ALL, 5)

        self.st_total_int = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_int.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_int, 0, wx.ALL, 5)

        self.st_total_log = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_log.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_log, 0, wx.ALL, 5)

        self.st_total_wil = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_wil.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_wil, 0, wx.ALL, 5)

        self.st_total_cha = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_cha.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_cha, 0, wx.ALL, 5)

        self.st_total_luc = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_luc.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_luc, 0, wx.ALL, 5)

        self.st_total_rep = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_rep.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_rep, 0, wx.ALL, 5)

        self.st_total_mag = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_mag.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_mag, 0, wx.ALL, 5)

        self.st_total_chi = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_chi.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_chi, 0, wx.ALL, 5)

        self.st_total_psi = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.st_total_psi.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_psi, 0, wx.ALL, 5)

        self.st_total_str_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"str_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_str_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_str_val, 0, wx.ALL, 5)

        self.st_total_agi_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"agi_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_agi_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_agi_val, 0, wx.ALL, 5)

        self.st_total_end_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"end_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_end_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_end_val, 0, wx.ALL, 5)

        self.st_total_int_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"int_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_int_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_int_val, 0, wx.ALL, 5)

        self.st_total_log_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"log_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_log_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_log_val, 0, wx.ALL, 5)

        self.st_total_wil_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"wil_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_wil_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_wil_val, 0, wx.ALL, 5)

        self.st_total_cha_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"cha_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_cha_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_cha_val, 0, wx.ALL, 5)

        self.st_total_luc_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"luc_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_luc_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_luc_val, 0, wx.ALL, 5)

        self.st_total_rep_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"rep_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_rep_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_rep_val, 0, wx.ALL, 5)

        self.st_total_mag_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"mag_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_mag_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_mag_val, 0, wx.ALL, 5)

        self.st_total_chi_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"chi_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_chi_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_chi_val, 0, wx.ALL, 5)

        self.st_total_psi_val = wx.StaticText(sbs_overview_stats.GetStaticBox(), wx.ID_ANY, u"psi_val",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_total_psi_val.Wrap(-1)
        gs_overview_stats_1.Add(self.st_total_psi_val, 0, wx.ALL, 5)

        sbs_overview_stats.Add(gs_overview_stats_1, 1, wx.EXPAND, 5)

        bs_overview_main.Add(sbs_overview_stats, 0, wx.EXPAND, 5)

        self.p_overview.SetSizer(bs_overview_main)
        self.p_overview.Layout()
        bs_overview_main.Fit(self.p_overview)
        self.nb_main.AddPage(self.p_overview, u"Overview", True)
        self.p_race = wx.Panel(self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_race = wx.BoxSizer(wx.VERTICAL)

        sbs_race_race = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Race"), wx.VERTICAL)

        self.st_race_race_val = wx.StaticText(sbs_race_race.GetStaticBox(), wx.ID_ANY, u"char_race", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_race_race_val.Wrap(-1)
        sbs_race_race.Add(self.st_race_race_val, 0, wx.ALL, 5)

        self.b_race_edit = wx.Button(sbs_race_race.GetStaticBox(), wx.ID_ANY, u"Change Race", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbs_race_race.Add(self.b_race_edit, 0, wx.ALL, 5)

        bs_race.Add(sbs_race_race, 0, wx.EXPAND, 5)

        sbs_race_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Selected Skills"), wx.VERTICAL)

        self.tc_race_skills = wx.TextCtrl(sbs_race_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_race_skills.SetMinSize(wx.Size(-1, 80))

        sbs_race_skills.Add(self.tc_race_skills, 0, wx.ALL | wx.EXPAND, 5)

        self.b_race_skills_edit = wx.Button(sbs_race_skills.GetStaticBox(), wx.ID_ANY, u"Edit Skills",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_race_skills.Add(self.b_race_skills_edit, 0, wx.ALL, 5)

        bs_race.Add(sbs_race_skills, 1, wx.EXPAND, 5)

        bs_race_exploits_and_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_race_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Exploits"), wx.VERTICAL)

        lb_race_exploits_listChoices = []
        self.lb_race_exploits_list = wx.ListBox(sbs_race_exploits.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                                wx.DefaultSize, lb_race_exploits_listChoices, 0)
        self.lb_race_exploits_list.SetMinSize(wx.Size(-1, 140))

        sbs_race_exploits.Add(self.lb_race_exploits_list, 0, wx.ALL | wx.EXPAND, 5)

        bs_race_exploits_and_desc.Add(sbs_race_exploits, 1, wx.EXPAND, 5)

        sbs_race_exploits_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Description"), wx.VERTICAL)

        self.tc_race_exploit_desc = wx.TextCtrl(sbs_race_exploits_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_race_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_race_exploits_desc.Add(self.tc_race_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_race_exploits_and_desc.Add(sbs_race_exploits_desc, 2, wx.EXPAND, 5)

        bs_race.Add(bs_race_exploits_and_desc, 1, wx.EXPAND, 5)

        sbs_race_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Racial Stats"), wx.VERTICAL)

        gs_race_stats_1 = wx.GridSizer(0, 12, 0, 0)

        self.st_race_str = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_str.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_str, 0, wx.ALL, 5)

        self.st_race_agi = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_agi.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_agi, 0, wx.ALL, 5)

        self.st_race_end = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_end.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_end, 0, wx.ALL, 5)

        self.st_race_int = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_int.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_int, 0, wx.ALL, 5)

        self.st_race_log = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_log.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_log, 0, wx.ALL, 5)

        self.st_race_wil = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_wil.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_wil, 0, wx.ALL, 5)

        self.st_race_cha = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_cha.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_cha, 0, wx.ALL, 5)

        self.st_race_luc = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_luc.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_luc, 0, wx.ALL, 5)

        self.st_race_rep = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_rep.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_rep, 0, wx.ALL, 5)

        self.st_race_mag = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_mag.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_mag, 0, wx.ALL, 5)

        self.st_race_chi = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_chi.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_chi, 0, wx.ALL, 5)

        self.st_race_psi = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.st_race_psi.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_psi, 0, wx.ALL, 5)

        self.st_race_str_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"str_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_str_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_str_val, 0, wx.ALL, 5)

        self.st_race_agi_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"agi_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_agi_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_agi_val, 0, wx.ALL, 5)

        self.st_race_end_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"end_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_end_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_end_val, 0, wx.ALL, 5)

        self.st_race_int_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"int_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_int_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_int_val, 0, wx.ALL, 5)

        self.st_race_log_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"log_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_log_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_log_val, 0, wx.ALL, 5)

        self.st_race_wil_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"wil_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_wil_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_wil_val, 0, wx.ALL, 5)

        self.st_race_cha_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"cha_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_cha_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_cha_val, 0, wx.ALL, 5)

        self.st_race_luc_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"luc_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_luc_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_luc_val, 0, wx.ALL, 5)

        self.st_race_rep_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"rep_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_rep_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_rep_val, 0, wx.ALL, 5)

        self.st_race_mag_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"mag_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_mag_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_mag_val, 0, wx.ALL, 5)

        self.st_race_chi_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"chi_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_chi_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_chi_val, 0, wx.ALL, 5)

        self.st_race_psi_val = wx.StaticText(sbs_race_stats.GetStaticBox(), wx.ID_ANY, u"psi_val", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.st_race_psi_val.Wrap(-1)
        gs_race_stats_1.Add(self.st_race_psi_val, 0, wx.ALL, 5)

        sbs_race_stats.Add(gs_race_stats_1, 1, wx.EXPAND, 5)

        bs_race.Add(sbs_race_stats, 0, wx.EXPAND, 5)

        self.p_race.SetSizer(bs_race)
        self.p_race.Layout()
        bs_race.Fit(self.p_race)
        self.nb_main.AddPage(self.p_race, u"Race", False)
        self.p_homeworld = wx.Panel(self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_homeworld_main = wx.BoxSizer(wx.VERTICAL)

        sbs_homeworld_homeworld = wx.StaticBoxSizer(wx.StaticBox(self.p_homeworld, wx.ID_ANY, u"Homeworld"),
                                                    wx.VERTICAL)

        self.st_homeworld_homeworld_val = wx.StaticText(sbs_homeworld_homeworld.GetStaticBox(), wx.ID_ANY,
                                                        u"homeworld_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_homeworld_val.Wrap(-1)
        sbs_homeworld_homeworld.Add(self.st_homeworld_homeworld_val, 0, wx.ALL, 5)

        self.b_homeworld_edit = wx.Button(sbs_homeworld_homeworld.GetStaticBox(), wx.ID_ANY, u"Change Homeworld",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_homeworld_homeworld.Add(self.b_homeworld_edit, 0, wx.ALL, 5)

        bs_homeworld_main.Add(sbs_homeworld_homeworld, 0, wx.EXPAND, 5)

        sbs_homeworld_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_homeworld, wx.ID_ANY, u"Selected Skills"),
                                                 wx.VERTICAL)

        self.tc_homeworld_skills = wx.TextCtrl(sbs_homeworld_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_homeworld_skills.SetMinSize(wx.Size(-1, 80))

        sbs_homeworld_skills.Add(self.tc_homeworld_skills, 0, wx.ALL | wx.EXPAND, 5)

        self.b_homeworld_skills_edit = wx.Button(sbs_homeworld_skills.GetStaticBox(), wx.ID_ANY, u"Edit Skills",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_homeworld_skills.Add(self.b_homeworld_skills_edit, 0, wx.ALL, 5)

        bs_homeworld_main.Add(sbs_homeworld_skills, 1, wx.EXPAND, 5)

        sbs_homeworld_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_homeworld, wx.ID_ANY, u"Homeworld Stats"),
                                                wx.VERTICAL)

        gs_homeworld_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_homeworld_str = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_str.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_str, 0, wx.ALL, 5)

        self.st_homeworld_agi = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_agi.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_agi, 0, wx.ALL, 5)

        self.st_homeworld_end = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_end.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_end, 0, wx.ALL, 5)

        self.st_homeworld_int = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_int.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_int, 0, wx.ALL, 5)

        self.st_homeworld_log = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_log.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_log, 0, wx.ALL, 5)

        self.st_homeworld_wil = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_wil.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_wil, 0, wx.ALL, 5)

        self.st_homeworld_cha = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_cha.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_cha, 0, wx.ALL, 5)

        self.st_homeworld_luc = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_luc.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_luc, 0, wx.ALL, 5)

        self.st_homeworld_rep = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_rep.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_rep, 0, wx.ALL, 5)

        self.st_homeworld_mag = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_mag.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_mag, 0, wx.ALL, 5)

        self.st_homeworld_chi = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_chi.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_chi, 0, wx.ALL, 5)

        self.st_homeworld_psi = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_homeworld_psi.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_psi, 0, wx.ALL, 5)

        self.st_homeworld_str_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"str_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_str_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_str_val, 0, wx.ALL, 5)

        self.st_homeworld_agi_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"agi_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_agi_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_agi_val, 0, wx.ALL, 5)

        self.st_homeworld_end_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"end_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_end_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_end_val, 0, wx.ALL, 5)

        self.st_homeworld_int_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"int_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_int_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_int_val, 0, wx.ALL, 5)

        self.st_homeworld_log_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"log_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_log_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_log_val, 0, wx.ALL, 5)

        self.st_homeworld_wil_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"wil_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_wil_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_wil_val, 0, wx.ALL, 5)

        self.st_homeworld_cha_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"cha_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_cha_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_cha_val, 0, wx.ALL, 5)

        self.st_homeworld_luc_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"luc_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_luc_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_luc_val, 0, wx.ALL, 5)

        self.st_homeworld_rep_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"rep_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_rep_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_rep_val, 0, wx.ALL, 5)

        self.st_homeworld_mag_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"mag_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_mag_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_mag_val, 0, wx.ALL, 5)

        self.st_homeworld_chi_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"chi_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_chi_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_chi_val, 0, wx.ALL, 5)

        self.st_homeworld_psi_val = wx.StaticText(sbs_homeworld_stats.GetStaticBox(), wx.ID_ANY, u"psi_val",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_homeworld_psi_val.Wrap(-1)
        gs_homeworld_stats.Add(self.st_homeworld_psi_val, 0, wx.ALL, 5)

        sbs_homeworld_stats.Add(gs_homeworld_stats, 1, wx.EXPAND, 5)

        bs_homeworld_main.Add(sbs_homeworld_stats, 0, wx.EXPAND, 5)

        self.p_homeworld.SetSizer(bs_homeworld_main)
        self.p_homeworld.Layout()
        bs_homeworld_main.Fit(self.p_homeworld)
        self.nb_main.AddPage(self.p_homeworld, u"Homeworld", False)
        self.p_careers = wx.Panel(self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_careers_main = wx.BoxSizer(wx.VERTICAL)

        bs_careers_and_skills = wx.BoxSizer(wx.HORIZONTAL)

        sbs_careers_careers = wx.StaticBoxSizer(wx.StaticBox(self.p_careers, wx.ID_ANY, u"Careers"), wx.HORIZONTAL)

        lb_careers_listChoices = []
        self.lb_careers_list = wx.ListBox(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, lb_careers_listChoices, wx.LB_NEEDED_SB)
        self.lb_careers_list.SetMinSize(wx.Size(-1, 200))

        sbs_careers_careers.Add(self.lb_careers_list, 0, wx.ALL, 5)

        bs_careers_up_down = wx.BoxSizer(wx.VERTICAL)

        self.b_career_add = wx.Button(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, u"Add", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bs_careers_up_down.Add(self.b_career_add, 0, wx.ALL, 5)

        self.b_career_edit = wx.Button(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, u"Edit", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bs_careers_up_down.Add(self.b_career_edit, 0, wx.ALL, 5)

        self.b_career_remove = wx.Button(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, u"Remove", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bs_careers_up_down.Add(self.b_career_remove, 0, wx.ALL, 5)

        self.b_career_mv_up = wx.Button(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, u"Move Up", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bs_careers_up_down.Add(self.b_career_mv_up, 0, wx.ALL, 5)

        self.b_career_mv_down = wx.Button(sbs_careers_careers.GetStaticBox(), wx.ID_ANY, u"Move Down",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bs_careers_up_down.Add(self.b_career_mv_down, 0, wx.ALL, 5)

        sbs_careers_careers.Add(bs_careers_up_down, 0, wx.ALIGN_BOTTOM, 5)

        bs_careers_and_skills.Add(sbs_careers_careers, 1, wx.EXPAND, 5)

        sbs_careers_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_careers, wx.ID_ANY, u"Skills"), wx.VERTICAL)

        self.tc_careers_skills = wx.TextCtrl(sbs_careers_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_careers_skills.SetMinSize(wx.Size(-1, 120))

        sbs_careers_skills.Add(self.tc_careers_skills, 0, wx.ALL | wx.EXPAND, 5)

        self.b_careers_edit_skills = wx.Button(sbs_careers_skills.GetStaticBox(), wx.ID_ANY, u"Edit Skills",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_careers_skills.Add(self.b_careers_edit_skills, 0, wx.ALL, 5)

        bs_careers_and_skills.Add(sbs_careers_skills, 2, wx.EXPAND, 5)

        bs_careers_main.Add(bs_careers_and_skills, 1, wx.EXPAND, 5)

        sbs_careers_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_careers, wx.ID_ANY, u"Exploit"), wx.VERTICAL)

        self.tc_careers_exploit_and_desc = wx.TextCtrl(sbs_careers_exploits.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize,
                                                       wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_careers_exploit_and_desc.SetMinSize(wx.Size(-1, 80))

        sbs_careers_exploits.Add(self.tc_careers_exploit_and_desc, 0, wx.ALL | wx.EXPAND, 5)

        self.b_careers_edit_exploits = wx.Button(sbs_careers_exploits.GetStaticBox(), wx.ID_ANY, u"Edit Career Exploit",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_careers_exploits.Add(self.b_careers_edit_exploits, 0, wx.ALL, 5)

        bs_careers_main.Add(sbs_careers_exploits, 1, wx.EXPAND, 5)

        sbs_careers_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_careers, wx.ID_ANY, u"Career Stats"), wx.VERTICAL)

        gs_careers_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_career_str = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_str.Wrap(-1)
        gs_careers_stats.Add(self.st_career_str, 0, wx.ALL, 5)

        self.st_career_agi = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_agi.Wrap(-1)
        gs_careers_stats.Add(self.st_career_agi, 0, wx.ALL, 5)

        self.st_career_end = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_end.Wrap(-1)
        gs_careers_stats.Add(self.st_career_end, 0, wx.ALL, 5)

        self.st_career_end = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_end.Wrap(-1)
        gs_careers_stats.Add(self.st_career_end, 0, wx.ALL, 5)

        self.st_career_log = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_log.Wrap(-1)
        gs_careers_stats.Add(self.st_career_log, 0, wx.ALL, 5)

        self.st_career_wil = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_wil.Wrap(-1)
        gs_careers_stats.Add(self.st_career_wil, 0, wx.ALL, 5)

        self.st_career_cha = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_cha.Wrap(-1)
        gs_careers_stats.Add(self.st_career_cha, 0, wx.ALL, 5)

        self.st_career_luc = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_luc.Wrap(-1)
        gs_careers_stats.Add(self.st_career_luc, 0, wx.ALL, 5)

        self.st_career_rep = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_rep.Wrap(-1)
        gs_careers_stats.Add(self.st_career_rep, 0, wx.ALL, 5)

        self.st_career_mag = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_mag.Wrap(-1)
        gs_careers_stats.Add(self.st_career_mag, 0, wx.ALL, 5)

        self.st_career_chi = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_chi.Wrap(-1)
        gs_careers_stats.Add(self.st_career_chi, 0, wx.ALL, 5)

        self.st_career_psi = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_career_psi.Wrap(-1)
        gs_careers_stats.Add(self.st_career_psi, 0, wx.ALL, 5)

        self.st_career_str_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"str_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_str_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_str_val, 0, wx.ALL, 5)

        self.st_career_agi_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"agi_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_agi_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_agi_val, 0, wx.ALL, 5)

        self.st_career_end_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"end_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_end_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_end_val, 0, wx.ALL, 5)

        self.st_career_int_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"int_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_int_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_int_val, 0, wx.ALL, 5)

        self.st_career_log_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"log_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_log_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_log_val, 0, wx.ALL, 5)

        self.st_career_wil_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"wil_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_wil_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_wil_val, 0, wx.ALL, 5)

        self.st_career_cha_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"cha_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_cha_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_cha_val, 0, wx.ALL, 5)

        self.st_career_luc_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"luc_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_luc_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_luc_val, 0, wx.ALL, 5)

        self.st_career_rep_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"rep_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_rep_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_rep_val, 0, wx.ALL, 5)

        self.st_career_mag_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"mag_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_mag_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_mag_val, 0, wx.ALL, 5)

        self.st_career_chi_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"chi_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_chi_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_chi_val, 0, wx.ALL, 5)

        self.st_career_psi_val = wx.StaticText(sbs_careers_stats.GetStaticBox(), wx.ID_ANY, u"psi_val",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_career_psi_val.Wrap(-1)
        gs_careers_stats.Add(self.st_career_psi_val, 0, wx.ALL, 5)

        sbs_careers_stats.Add(gs_careers_stats, 1, wx.EXPAND, 5)

        bs_careers_main.Add(sbs_careers_stats, 0, wx.EXPAND, 5)

        self.p_careers.SetSizer(bs_careers_main)
        self.p_careers.Layout()
        bs_careers_main.Fit(self.p_careers)
        self.nb_main.AddPage(self.p_careers, u"Careers", False)
        self.p_exploits = wx.Panel(self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_exploits_main = wx.BoxSizer(wx.HORIZONTAL)

        sbs_exploits_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_exploits, wx.ID_ANY, u"Exploits"), wx.VERTICAL)

        gbs_exploits_list = wx.GridBagSizer(0, 0)
        gbs_exploits_list.SetFlexibleDirection(wx.BOTH)
        gbs_exploits_list.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        lb_exploits_listChoices = []
        self.lb_exploits_list = wx.ListBox(sbs_exploits_exploits.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, lb_exploits_listChoices, 0)
        self.lb_exploits_list.SetMinSize(wx.Size(-1, 200))

        gbs_exploits_list.Add(self.lb_exploits_list, wx.GBPosition(0, 0), wx.GBSpan(1, 2), wx.ALL, 5)

        self.b_exploits_add = wx.Button(sbs_exploits_exploits.GetStaticBox(), wx.ID_ANY, u"Add...", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbs_exploits_list.Add(self.b_exploits_add, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.b_exploits_remove = wx.Button(sbs_exploits_exploits.GetStaticBox(), wx.ID_ANY, u"Remove",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        gbs_exploits_list.Add(self.b_exploits_remove, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        sbs_exploits_exploits.Add(gbs_exploits_list, 1, wx.EXPAND, 5)

        bs_exploits_main.Add(sbs_exploits_exploits, 0, wx.EXPAND, 5)

        sbs_exploits_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_exploits, wx.ID_ANY, u"Description"), wx.VERTICAL)

        self.tc_exploits_desc = wx.TextCtrl(sbs_exploits_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY | wx.TE_WORDWRAP)
        self.tc_exploits_desc.SetMinSize(wx.Size(-1, 400))

        sbs_exploits_desc.Add(self.tc_exploits_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_exploits_main.Add(sbs_exploits_desc, 1, wx.EXPAND, 5)

        self.p_exploits.SetSizer(bs_exploits_main)
        self.p_exploits.Layout()
        bs_exploits_main.Fit(self.p_exploits)
        self.nb_main.AddPage(self.p_exploits, u"Exploits", False)

        bs_main_window.Add(self.nb_main, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_main_window)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.new_character, id=self.mi_file_new.GetId())
        self.Bind(wx.EVT_MENU, self.open_file, id=self.mi_file_open.GetId())
        self.Bind(wx.EVT_MENU, self.save_as_file, id=self.mi_file_save_as.GetId())
        self.Bind(wx.EVT_MENU, self.quit_wca, id=self.mi_file_quit.GetId())
        self.tc_overview_name_val.Bind(wx.EVT_TEXT, self.set_character_name)
        self.b_overview_change_trait.Bind(wx.EVT_BUTTON, self.change_trait)
        self.b_race_edit.Bind(wx.EVT_BUTTON, self.change_race)
        self.b_race_skills_edit.Bind(wx.EVT_BUTTON, self.edit_race_skills)
        self.lb_race_exploits_list.Bind(wx.EVT_LISTBOX, self.show_race_exploit_desc)
        self.b_homeworld_edit.Bind(wx.EVT_BUTTON, self.change_homeworld)
        self.b_homeworld_skills_edit.Bind(wx.EVT_BUTTON, self.edit_homeworld_skills)
        self.lb_careers_list.Bind(wx.EVT_LISTBOX, self.on_career_select)
        self.b_career_add.Bind(wx.EVT_BUTTON, self.add_career)
        self.b_career_edit.Bind(wx.EVT_BUTTON, self.edit_career)
        self.b_career_remove.Bind(wx.EVT_BUTTON, self.remove_career)
        self.b_career_mv_up.Bind(wx.EVT_BUTTON, self.move_career_up)
        self.b_career_mv_down.Bind(wx.EVT_BUTTON, self.move_career_down)
        self.b_careers_edit_skills.Bind(wx.EVT_BUTTON, self.edit_career_skills)
        self.b_careers_edit_exploits.Bind(wx.EVT_BUTTON, self.set_career_exploit)
        self.lb_exploits_list.Bind(wx.EVT_LISTBOX, self.on_misc_exploit_select)
        self.b_exploits_add.Bind(wx.EVT_BUTTON, self.add_misc_exploit)
        self.b_exploits_remove.Bind(wx.EVT_BUTTON, self.remove_misc_exploit)

        self.nb_main.Hide()

    def __del__(self):
        pass

    ##################################
    # Additional WCAFrame init stuff #
    ##################################
    # self.nb_main.Hide()

    ######################
    # WCAFrame Functions #
    ######################

    ##################
    # Menu functions #
    ##################
    def new_character(self, event):
        self.nb_main.Show()
        self.user_character = character.Character(race={'Race': copy.deepcopy(races_new.race_new_human),
                                                        'Source': 'new',
                                                        'Stats': copy.deepcopy(races_new.race_new_human.stats)},
                                                  homeworld={'Homeworld': copy.deepcopy(homeworlds_new.homeworld_none),
                                                             'Source': 'new'},
                                                  age_descriptor='young')
        self.mi_file_save.Enable(True)
        self.mi_file_save_as.Enable(True)

        # Update
        self.update_overview_tab(None)
        self.update_race_tab(None)
        self.update_homeworld_tab(None)
        self.update_career_tab(None)
        self.update_exploits_tab(None)
        self.on_career_select(None)
        self.on_misc_exploit_select(None)

    def open_file(self, event):
        # if self.character_not_saved:
        #     if wx.MessageBox("Current character has not been saved! Proceed?", "Please confirm",
        #                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
        #         return

        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open Character file", wildcard="WCA files (*.wca)|*.wca",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = file_dialog.GetPath()
            try:
                with open(pathname, 'rb') as file:
                    self.user_character = pickle.load(file)
            except IOError:
                wx.LogError("Cannot open file '{}'.".format(file))
        self.mi_file_save.Enable(True)
        self.mi_file_save_as.Enable(True)
        self.nb_main.Show()
        # Update
        self.update_overview_tab(None)
        self.update_race_tab(None)
        self.update_homeworld_tab(None)
        self.update_career_tab(None)
        self.update_exploits_tab(None)
        self.on_career_select(None)
        self.on_misc_exploit_select(None)

    def save_as_file(self, event):
        with wx.FileDialog(self, "Save WCA file", wildcard="WCA files (*.wca)|*.wca",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = file_dialog.GetPath()
            try:
                with open(pathname, 'wb') as file:
                    pickle.dump(self.user_character, file, pickle.HIGHEST_PROTOCOL)
            except IOError:
                wx.LogError("Cannot save current data in file '{}}'.".format(pathname))

    def quit_wca(self, event):
        self.Close()

    #########################
    # Tab refresh functions #
    #########################
    def update_overview_tab(self, event):
        total_stats = self.user_character.calc_stat_total()

        self.tc_overview_name_val.SetValue(self.user_character.name)
        self.st_overview_homeworld_val.SetLabel(self.user_character.homeworld['Homeworld'].name)
        self.st_overview_race_val.SetLabel(self.user_character.race['Race'].name)
        self.st_overview_trait_val.SetLabel(self.user_character.trait['Name'])

        skill_total = self.user_character.calc_skill_total()
        skill_total_str = ''
        for skill, value in skill_total.items():
            skill_total_str += '{} - {} ({}d6)\n'.format(skill, value, character.calc_dice_pool_size(value))
        self.tc_overview_skills.SetValue(skill_total_str)

        self.st_total_str_val.SetLabel(str(total_stats['STR']))
        self.st_total_agi_val.SetLabel(str(total_stats['AGI']))
        self.st_total_end_val.SetLabel(str(total_stats['END']))
        self.st_total_int_val.SetLabel(str(total_stats['INT']))
        self.st_total_log_val.SetLabel(str(total_stats['LOG']))
        self.st_total_wil_val.SetLabel(str(total_stats['WIL']))
        self.st_total_cha_val.SetLabel(str(total_stats['CHA']))
        self.st_total_luc_val.SetLabel(str(total_stats['LUC']))
        self.st_total_rep_val.SetLabel(str(total_stats['REP']))
        self.st_total_mag_val.SetLabel(str(total_stats['MAG']))
        self.st_total_chi_val.SetLabel(str(total_stats['CHI']))
        self.st_total_psi_val.SetLabel(str(total_stats['PSI']))

        all_exploits_str = ''
        for exploit in self.user_character.get_all_exploits():
            all_exploits_str += '{} - {}\n\n'.format(exploit['Name'], exploit['Desc'])

        self.tc_overview_exploits.SetValue(all_exploits_str)

        derived_stats_str = ''
        for key, value in self.user_character.calc_derived_stats().items():
            derived_stats_str += '{} - {}\n'.format(key, value)

        self.tc_overview_derived_stats.SetValue(derived_stats_str)

    def update_race_tab(self, event):
        self.st_race_race_val.SetLabel(self.user_character.race['Race'].name)

        selected_race_skills = ''
        for skill_pick in self.user_character.race_skill_choices:
            selected_race_skills += '{}, '.format(skill_pick)
        selected_race_skills = selected_race_skills[:-2]
        if selected_race_skills == '':
            self.tc_race_skills.SetValue('No skills selected')
        else:
            self.tc_race_skills.SetValue(selected_race_skills)

        self.lb_race_exploits_list.Clear()
        for exploit in self.user_character.race['Race'].exploits:
            self.lb_race_exploits_list.Append(exploit['Name'])

        self.st_race_str_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['STR']))
        self.st_race_agi_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['AGI']))
        self.st_race_end_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['END']))
        self.st_race_int_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['INT']))
        self.st_race_log_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['LOG']))
        self.st_race_wil_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['WIL']))
        self.st_race_cha_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['CHA']))
        self.st_race_luc_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['LUC']))
        self.st_race_rep_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['REP']))
        self.st_race_mag_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['MAG']))
        self.st_race_chi_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['CHI']))
        self.st_race_psi_val.SetLabel('{:+d}'.format(self.user_character.race['Stats']['PSI']))

    def update_homeworld_tab(self, event):
        self.st_homeworld_homeworld_val.SetLabel(self.user_character.homeworld['Homeworld'].name)

        selected_homeworld_skills = ''
        for skill_pick in self.user_character.homeworld_skill_choices:
            selected_homeworld_skills += '{}, '.format(skill_pick)
            selected_homeworld_skills = selected_homeworld_skills[:-2]

        if selected_homeworld_skills == '':
            self.tc_homeworld_skills.SetLabel('No skills selected')
        else:
            self.tc_homeworld_skills.SetLabel(selected_homeworld_skills)

        self.st_homeworld_str_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['STR']))
        self.st_homeworld_agi_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['AGI']))
        self.st_homeworld_end_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['END']))
        self.st_homeworld_int_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['INT']))
        self.st_homeworld_log_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['LOG']))
        self.st_homeworld_wil_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['WIL']))
        self.st_homeworld_cha_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['CHA']))
        self.st_homeworld_luc_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['LUC']))
        self.st_homeworld_rep_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['REP']))
        self.st_homeworld_mag_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['MAG']))
        self.st_homeworld_chi_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['CHI']))
        self.st_homeworld_psi_val.SetLabel('{:+d}'.format(self.user_character.homeworld['Homeworld'].stats['PSI']))

    def update_career_tab(self, event):
        self.lb_careers_list.Clear()
        for career in self.user_character.career_track:
            self.lb_careers_list.Append(career['Career'].name)

        if self.lb_careers_list.GetCount() <= 0:
            self.st_career_str_val.SetLabel('-')
            self.st_career_agi_val.SetLabel('-')
            self.st_career_end_val.SetLabel('-')
            self.st_career_int_val.SetLabel('-')
            self.st_career_log_val.SetLabel('-')
            self.st_career_wil_val.SetLabel('-')
            self.st_career_cha_val.SetLabel('-')
            self.st_career_luc_val.SetLabel('-')
            self.st_career_rep_val.SetLabel('-')
            self.st_career_mag_val.SetLabel('-')
            self.st_career_chi_val.SetLabel('-')
            self.st_career_psi_val.SetLabel('-')

    def update_exploits_tab(self, event):
        self.lb_exploits_list.Clear()
        for exploit in self.user_character.misc_exploits:
            self.lb_exploits_list.Append(exploit['Name'])

    ##########################
    # Overview tab functions #
    ##########################
    def set_character_name(self, event):
        self.user_character.name = event.GetString()

    def change_trait(self, event):
        set_trait_dialog = SetTraitDialog(self)
        index = 0
        while index < set_trait_dialog.lb_std_exploit_list.GetCount():
            if self.user_character.trait['Name'] in set_trait_dialog.lb_std_exploit_list.GetString(index):
                set_trait_dialog.lb_std_exploit_list.SetSelection(index)
                set_trait_dialog.on_trait_select(None)
                break
            index += 1

        results = set_trait_dialog.ShowModal()
        if results == wx.ID_OK:
            selected_trait = set_trait_dialog.lb_std_exploit_list.GetSelection()
            self.user_character.trait = copy.deepcopy(set_trait_dialog.trait_list[selected_trait])
            self.update_overview_tab(None)

    ######################
    # Race tab functions #
    ######################
    def change_race(self, event):
        race_dialog = ChangeRaceDialog(self)
        current_list_source = self.user_character.race['Source']
        if current_list_source == 'old':
            race_dialog.rb_crd_old.SetValue(True)
        elif current_list_source == 'now':
            race_dialog.rb_crd_now.SetValue(True)
        elif current_list_source == 'new':
            race_dialog.rb_crd_new.SetValue(True)
        elif current_list_source == 'custom':
            race_dialog.rb_crd_custom.SetValue(True)

        race_dialog.show_races(None)
        index = 0
        while index < race_dialog.lb_crd_race_list.GetCount():
            if self.user_character.race['Race'].name == race_dialog.lb_crd_race_list.GetString(index):
                race_dialog.lb_crd_race_list.SetSelection(index)
            index += 1

        race_dialog.on_race_select(None)

        results = race_dialog.ShowModal()
        if results == wx.ID_OK:
            race_list = race_dialog.get_race_list()
            self.user_character.race = {'Race': race_list[race_dialog.lb_crd_race_list.GetSelection()],
                                        'Stats': collections.OrderedDict(STR=race_dialog.ic_crd_str.GetValue(),
                                                                         AGI=race_dialog.ic_crd_agi.GetValue(),
                                                                         END=race_dialog.ic_crd_end.GetValue(),
                                                                         INT=race_dialog.ic_crd_int.GetValue(),
                                                                         LOG=race_dialog.ic_crd_log.GetValue(),
                                                                         WIL=race_dialog.ic_crd_wil.GetValue(),
                                                                         CHA=race_dialog.ic_crd_cha.GetValue(),
                                                                         LUC=race_dialog.ic_crd_luc.GetValue(),
                                                                         REP=race_dialog.ic_crd_rep.GetValue(),
                                                                         MAG=race_dialog.ic_crd_mag.GetValue(),
                                                                         CHI=race_dialog.ic_crd_chi.GetValue(),
                                                                         PSI=race_dialog.ic_crd_psi.GetValue()),
                                        'Source': race_dialog.get_list_source()}
            self.update_race_tab(None)
            self.update_overview_tab(None)

    def edit_race_skills(self, event):
        race_skills_dialog = EditSkillsDialog(self)
        for skill in self.user_character.race_skill_choices:
            race_skills_dialog.lb_esd_skills_list.Append(skill)
        results = race_skills_dialog.ShowModal()
        if results == wx.ID_OK:
            self.user_character.race_skill_choices = copy.deepcopy(race_skills_dialog.lb_esd_skills_list.GetItems())
            self.update_race_tab(None)
            self.update_overview_tab(None)

    def show_race_exploit_desc(self, event):
        selected_exploit = self.lb_race_exploits_list.GetSelection()
        self.tc_race_exploit_desc.SetValue(self.user_character.race['Race'].exploits[selected_exploit]['Desc'])

    ###########################
    # Homeworld tab functions #
    ###########################
    def change_homeworld(self, event):
        homeworld_dialog = ChangeHomeworldDialog(self)
        current_list_source = self.user_character.homeworld['Source']
        if current_list_source == 'new':
            homeworld_dialog.rb_chd_new.SetValue(True)
        elif current_list_source == 'custom':
            homeworld_dialog.rb_chd_custom.SetValue(True)

        homeworld_dialog.show_homeworlds(None)

        index = 0
        while index < homeworld_dialog.lb_chd_homeworld_list.GetCount():
            if (self.user_character.homeworld['Homeworld'].name ==
                    homeworld_dialog.lb_chd_homeworld_list.GetString(index)):
                homeworld_dialog.lb_chd_homeworld_list.SetSelection(index)
            index += 1
        homeworld_dialog.on_homeworld_select(None)

        results = homeworld_dialog.ShowModal()
        if results == wx.ID_OK:
            homeworld_list = homeworld_dialog.get_homeworld_list()
            self.user_character.homeworld = {'Homeworld': copy.deepcopy(
                homeworld_list[homeworld_dialog.lb_chd_homeworld_list.GetSelection()]),
                                             'Source': homeworld_dialog.get_list_source()}
            self.update_homeworld_tab(None)
            self.update_overview_tab(None)

    def edit_homeworld_skills(self, event):
        homeworld_skills_dialog = EditSkillsDialog(self)
        for skill in self.user_character.homeworld_skill_choices:
            homeworld_skills_dialog.lb_esd_skills_list.Append(skill)
        results = homeworld_skills_dialog.ShowModal()
        if results == wx.ID_OK:
            self.user_character.homeworld_skill_choices = copy.deepcopy(
                homeworld_skills_dialog.lb_esd_skills_list.GetItems())
            self.update_homeworld_tab(None)
            self.update_overview_tab(None)

    ########################
    # Career tab functions #
    ########################
    def add_career(self, event):
        career_dialog = EditCareerDialog(self)
        results = career_dialog.ShowModal()
        if results == wx.ID_OK:
            selected_career = career_dialog.lb_ecd_career_list.GetSelection()
            career_list = career_dialog.get_career_list()
            list_source = career_dialog.get_list_source()
            self.user_character.career_track.append(
                {'Source': list_source,
                 'Career': copy.deepcopy(career_list[selected_career]),
                 'Length': '{} {}'.format(
                     dice.roll(career_list[selected_career].career_time)['total'],
                     career_list[selected_career].career_time_unit),
                 'Stats': collections.OrderedDict(STR=career_dialog.ic_ecd_str.GetValue(),
                                                  AGI=career_dialog.ic_ecd_agi.GetValue(),
                                                  END=career_dialog.ic_ecd_end.GetValue(),
                                                  INT=career_dialog.ic_ecd_int.GetValue(),
                                                  LOG=career_dialog.ic_ecd_log.GetValue(),
                                                  WIL=career_dialog.ic_ecd_wil.GetValue(),
                                                  CHA=career_dialog.ic_ecd_cha.GetValue(),
                                                  LUC=career_dialog.ic_ecd_luc.GetValue(),
                                                  REP=career_dialog.ic_ecd_rep.GetValue(),
                                                  MAG=career_dialog.ic_ecd_mag.GetValue(),
                                                  CHI=career_dialog.ic_ecd_chi.GetValue(),
                                                  PSI=career_dialog.ic_ecd_psi.GetValue()),
                 'Skills': [],
                 'Exploit': {'Name': 'unset career exploit', 'Desc': 'unset', 'Source': 'unset'},
                 'Notes': ''})


            # Update page
            self.update_career_tab(None)
            self.update_overview_tab(None)
            self.lb_careers_list.SetSelection(self.lb_careers_list.GetCount()-1)
            self.on_career_select(None)

    def edit_career(self, event):
        career_track_index = self.lb_careers_list.GetSelection()
        career_dialog = EditCareerDialog(self)
        current_list_source = self.user_character.career_track[career_track_index]['Source']
        if current_list_source == 'origins':
            career_dialog.rb_ecd_origins.SetValue(True)
        elif current_list_source == 'old':
            career_dialog.rb_ecd_old.SetValue(True)
        elif current_list_source == 'now':
            career_dialog.rb_ecd_now.SetValue(True)
        elif current_list_source == 'new':
            career_dialog.rb_ecd_new.SetValue(True)
        elif current_list_source == 'martial arts':
            career_dialog.rb_ecd_ma.SetValue(True)
        elif current_list_source == 'custom':
            career_dialog.rb_ecd_custom.SetValue(True)

        career_dialog.show_careers(None)
        index = 0
        while index < career_dialog.lb_ecd_career_list.GetCount():
            if self.user_character.career_track[career_track_index]['Career'].name in \
                    career_dialog.lb_ecd_career_list.GetString(index):
                career_dialog.lb_ecd_career_list.SetSelection(index)
                career_dialog.on_career_select(None)
                break
            index += 1

        results = career_dialog.ShowModal()
        if results == wx.ID_OK:
            selected_career = career_dialog.lb_ecd_career_list.GetSelection()
            career_list = career_dialog.get_career_list()
            list_source = career_dialog.get_list_source()
            self.user_character.career_track[career_track_index] = \
                {'Source': list_source,
                 'Career': copy.deepcopy(career_list[selected_career]),
                 'Length': '{} {}'.format(
                     dice.roll(career_list[selected_career].career_time)['total'],
                     career_list[selected_career].career_time_unit),
                 'Stats': collections.OrderedDict(STR=career_dialog.ic_ecd_str.GetValue(),
                                                  AGI=career_dialog.ic_ecd_agi.GetValue(),
                                                  END=career_dialog.ic_ecd_end.GetValue(),
                                                  INT=career_dialog.ic_ecd_int.GetValue(),
                                                  LOG=career_dialog.ic_ecd_log.GetValue(),
                                                  WIL=career_dialog.ic_ecd_wil.GetValue(),
                                                  CHA=career_dialog.ic_ecd_cha.GetValue(),
                                                  LUC=career_dialog.ic_ecd_luc.GetValue(),
                                                  REP=career_dialog.ic_ecd_rep.GetValue(),
                                                  MAG=career_dialog.ic_ecd_mag.GetValue(),
                                                  CHI=career_dialog.ic_ecd_chi.GetValue(),
                                                  PSI=career_dialog.ic_ecd_psi.GetValue()),
                 'Skills': [],
                 'Exploit': {'Name': 'unset career exploit', 'Desc': 'unset'},
                 'Notes': ''}

            # Update page
            self.update_career_tab(None)
            self.update_overview_tab(None)
            self.lb_careers_list.SetSelection(career_track_index)
            self.on_career_select(None)

    def remove_career(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        self.user_character.career_track.pop(selected_career)
        self.update_career_tab(None)
        self.update_overview_tab(None)

        if selected_career < self.lb_careers_list.GetCount()-1:
            self.lb_careers_list.SetSelection(selected_career)
        elif selected_career >= self.lb_careers_list.GetCount()-1:
            self.lb_careers_list.SetSelection(self.lb_careers_list.GetCount()-1)

        # Update page
        self.on_career_select(None)

    def set_career_exploit(self, event):
        career_track_index = self.lb_careers_list.GetSelection()
        set_career_exploit = AddExploitDialog(self, self.user_character.career_track[career_track_index]['Career'],
                                              u"Set Career Exploit")
        list_source = self.user_character.career_track[career_track_index]['Exploit']['Source']
        if list_source != 'unset' and list_source is not None:
            if list_source is 'universal':
                set_career_exploit.rb_aed_universal.SetValue(True)
            elif list_source is 'android':
                set_career_exploit.rb_aed_android.SetValue(True)
            elif list_source is 'career':
                set_career_exploit.rb_aed_career.SetValue(True)
            elif list_source is 'custom':
                set_career_exploit.rb_aed_custom.SetValue(True)

            set_career_exploit.show_exploits(None)
            index = 0
            while index < set_career_exploit.lb_aed_exploit_list.GetCount():
                if (self.user_character.career_track[career_track_index]['Exploit']['Name'] in
                        set_career_exploit.lb_aed_exploit_list.GetString(index)):
                    set_career_exploit.lb_aed_exploit_list.SetSelection(index)
                    break
                index += 1
            set_career_exploit.on_exploit_select(None)

        results = set_career_exploit.ShowModal()
        if results == wx.ID_OK:
            exploit_list = set_career_exploit.get_exploit_list()
            selected_exploit = set_career_exploit.lb_aed_exploit_list.GetSelection()
            self.user_character.career_track[career_track_index]['Exploit']['Name'] = \
                exploit_list[selected_exploit]['Name']
            self.user_character.career_track[career_track_index]['Exploit']['Desc'] = \
                exploit_list[selected_exploit]['Desc']
            self.user_character.career_track[career_track_index]['Exploit']['Source'] = \
                set_career_exploit.get_list_source()

            self.lb_careers_list.SetSelection(career_track_index)
            self.update_career_tab(None)
            self.update_overview_tab(None)
            self.on_career_select(None)

    def edit_career_skills(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        career_skills_dialog = EditSkillsDialog(self)
        for skill in self.user_character.career_track[selected_career]['Skills']:
            career_skills_dialog.lb_esd_skills_list.Append(skill)
        results = career_skills_dialog.ShowModal()
        if results == wx.ID_OK:
            self.user_character.career_track[selected_career]['Skills'] = copy.deepcopy(
                career_skills_dialog.lb_esd_skills_list.GetItems())

        # Update page
        self.update_career_tab(None)
        self.update_overview_tab(None)
        self.lb_careers_list.SetSelection(selected_career)
        self.on_career_select(None)

    def on_career_select(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        # career_exploits = ''
        # for exploit in self.user_character.career_track[event.GetSelection()]['Exploit']:
        #     career_exploits += '{}\n'.format(exploit)
        # self.st_career_selected_exploits.SetLabel(career_exploits)
        if selected_career != -1:
            self.tc_careers_exploit_and_desc.SetValue('{} - {}'.format(
                self.user_character.career_track[selected_career]['Exploit']['Name'],
                self.user_character.career_track[selected_career]['Exploit']['Desc']))

            career_skills = ''
            for skill in self.user_character.career_track[selected_career]['Skills']:
                career_skills += '{}, '.format(skill)
            if career_skills != '':
                self.tc_careers_skills.SetValue(career_skills[:-2])
            else:
                self.tc_careers_skills.SetValue('No skills selected')

            # disable move up/down buttons if at the top/bottom of the list
            if selected_career == 0:
                self.b_career_mv_up.Enable(False)
            else:
                self.b_career_mv_up.Enable(True)

            if selected_career >= (self.lb_careers_list.GetCount() - 1):
                self.b_career_mv_down.Enable(False)
            else:
                self.b_career_mv_down.Enable(True)

            self.b_career_edit.Enable(True)
            self.b_career_remove.Enable(True)
            self.b_careers_edit_skills.Enable(True)
            self.b_careers_edit_exploits.Enable(True)

            self.st_career_str_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['STR']))
            self.st_career_agi_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['AGI']))
            self.st_career_end_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['END']))
            self.st_career_int_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['INT']))
            self.st_career_log_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['LOG']))
            self.st_career_wil_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['WIL']))
            self.st_career_cha_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['CHA']))
            self.st_career_luc_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['LUC']))
            self.st_career_rep_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['REP']))
            self.st_career_mag_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['MAG']))
            self.st_career_chi_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['CHI']))
            self.st_career_psi_val.SetLabel('{:+d}'.format(
                self.user_character.career_track[selected_career]['Stats']['PSI']))
        else:
            self.tc_careers_skills.Clear()
            self.tc_careers_exploit_and_desc.Clear()
            self.b_career_edit.Enable(False)
            self.b_career_remove.Enable(False)
            self.b_career_mv_up.Enable(False)
            self.b_career_mv_down.Enable(False)
            self.b_careers_edit_skills.Enable(False)
            self.b_careers_edit_exploits.Enable(False)

    def move_career_up(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        self.user_character.career_track[selected_career], \
            self.user_character.career_track[selected_career-1] = \
            self.user_character.career_track[selected_career-1], \
            self.user_character.career_track[selected_career]

        self.update_career_tab(None)
        self.lb_careers_list.SetSelection(selected_career-1)
        self.on_career_select(None)

    def move_career_down(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        self.user_character.career_track[selected_career], \
            self.user_character.career_track[selected_career+1] = \
            self.user_character.career_track[selected_career+1], \
            self.user_character.career_track[selected_career]

        self.update_career_tab(None)
        self.lb_careers_list.SetSelection(selected_career+1)
        self.on_career_select(None)

    #########################
    # Exploit tab functions #
    #########################
    def on_misc_exploit_select(self, event):
        selected_exploit = self.lb_exploits_list.GetSelection()
        if selected_exploit != -1:
            self.tc_exploits_desc.SetValue(self.user_character.misc_exploits[selected_exploit]['Desc'])
            self.b_exploits_remove.Enable(True)
        else:
            self.tc_exploits_desc.Clear()
            self.b_exploits_remove.Enable(False)

    def add_misc_exploit(self, event):
        misc_exploit_dialog = AddExploitDialog(self, title='Add Misc Exploit')
        results = misc_exploit_dialog.ShowModal()
        if results == wx.ID_OK:
            exploit_list = misc_exploit_dialog.get_exploit_list()
            selected_exploit = misc_exploit_dialog.lb_aed_exploit_list.GetSelection()
            self.user_character.misc_exploits.append(copy.deepcopy(exploit_list[selected_exploit]))
            self.user_character.misc_exploits.sort(key=lambda x: x['Name'])

            # Update
            self.update_exploits_tab(None)
            self.update_overview_tab(None)
            self.lb_exploits_list.SetSelection(self.lb_exploits_list.GetCount()-1)
            self.on_misc_exploit_select(None)

    def remove_misc_exploit(self, event):
        selected_exploit = self.lb_exploits_list.GetSelection()
        self.user_character.misc_exploits.pop(selected_exploit)
        self.update_exploits_tab(None)
        self.update_overview_tab(None)

        if selected_exploit < self.lb_exploits_list.GetCount()-1:
            self.lb_exploits_list.SetSelection(selected_exploit)
        elif selected_exploit >= self.lb_exploits_list.GetCount()-1:
            self.lb_exploits_list.SetSelection(self.lb_exploits_list.GetCount()-1)

        self.on_misc_exploit_select(None)


###########################################################################
## Class SetTraitDialog
###########################################################################

class SetTraitDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Set Trait", pos=wx.DefaultPosition,
                           size=wx.Size(765, 706), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_std_main = wx.BoxSizer(wx.VERTICAL)

        self.p_std_set_trait = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_std_1 = wx.BoxSizer(wx.VERTICAL)

        bs_std_exploit_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_std_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_std_set_trait, wx.ID_ANY, u"Traits"), wx.HORIZONTAL)

        lb_std_exploit_listChoices = []
        self.lb_std_exploit_list = wx.ListBox(sbs_std_exploits.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                              wx.DefaultSize, lb_std_exploit_listChoices, 0)
        self.lb_std_exploit_list.SetMinSize(wx.Size(-1, 120))

        sbs_std_exploits.Add(self.lb_std_exploit_list, 0, wx.ALL, 5)

        bs_std_exploit_desc.Add(sbs_std_exploits, 0, wx.EXPAND, 5)

        sbs_std_exploit_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_std_set_trait, wx.ID_ANY, u"Description"),
                                                 wx.VERTICAL)

        self.tc_std_exploit_desc = wx.TextCtrl(sbs_std_exploit_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_std_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_std_exploit_desc.Add(self.tc_std_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_std_exploit_desc.Add(sbs_std_exploit_desc, 2, wx.EXPAND, 5)

        bs_std_1.Add(bs_std_exploit_desc, 1, wx.EXPAND, 5)

        sbs_std_trait_table = wx.StaticBoxSizer(wx.StaticBox(self.p_std_set_trait, wx.ID_ANY, u"Attribute-Trait Table"),
                                                wx.VERTICAL)

        fgs_std_trait_table = wx.FlexGridSizer(0, 3, 0, 50)
        fgs_std_trait_table.AddGrowableCol(0)
        fgs_std_trait_table.SetFlexibleDirection(wx.BOTH)
        fgs_std_trait_table.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.st_std_tt_header_attr = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Attribute",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_header_attr.Wrap(-1)
        self.st_std_tt_header_attr.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        fgs_std_trait_table.Add(self.st_std_tt_header_attr, 0, wx.ALL, 5)

        self.st_std_tt_header_attr_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                        u"Highest Attribute", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_header_attr_high.Wrap(-1)
        self.st_std_tt_header_attr_high.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        fgs_std_trait_table.Add(self.st_std_tt_header_attr_high, 0, wx.ALL, 5)

        self.st_std_tt_header_attr_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                       u"Lowest Attribute", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_header_attr_low.Wrap(-1)
        self.st_std_tt_header_attr_low.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        fgs_std_trait_table.Add(self.st_std_tt_header_attr_low, 0, wx.ALL, 5)

        self.st_std_tt_str = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_std_tt_str.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_str, 0, wx.ALL, 5)

        self.st_std_tt_str_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                u"Massive, Athletic, Brawny", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_str_high.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_str_high, 0, wx.ALL, 5)

        self.st_std_tt_str_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Feeble, Tottering",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_str_low.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_str_low, 0, wx.ALL, 5)

        self.st_std_tt_agi = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_std_tt_agi.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_agi, 0, wx.ALL, 5)

        self.st_std_tt_agi_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                u"Nimble, Deadeye, Ambidextrous", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_agi_high.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_agi_high, 0, wx.ALL, 5)

        self.st_std_tt_agi_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Clumsy, Lame",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_agi_low.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_agi_low, 0, wx.ALL, 5)

        self.st_std_tt_end = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_std_tt_end.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_end, 0, wx.ALL, 5)

        self.st_std_tt_end_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                u"Rugged, Tough-as-nails", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_end_high.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_end_high, 0, wx.ALL, 5)

        self.st_std_tt_end_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                               u"Coughing, Asthmatic/anemic", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_std_tt_end_low.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_end_low, 0, wx.ALL, 5)

        self.st_std_tt_int = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.st_std_tt_int.Wrap(-1)
        fgs_std_trait_table.Add(self.st_std_tt_int, 0, wx.ALL, 5)

        self.std_std_tt_int_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Empathic, Alert",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_int_high.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_int_high, 0, wx.ALL, 5)

        self.std_std_tt_int_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Naive, Distracted",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_int_low.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_int_low, 0, wx.ALL, 5)

        self.std_std_tt_log = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.std_std_tt_log.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_log, 0, wx.ALL, 5)

        self.std_std_tt_log_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Brilliant, Erudite",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_log_high.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_log_high, 0, wx.ALL, 5)

        self.std_std_tt_log_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Illiterate, Forgetful",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_log_low.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_log_low, 0, wx.ALL, 5)

        self.std_std_tt_wil = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.std_std_tt_wil.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_wil, 0, wx.ALL, 5)

        self.std_std_tt_wil_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"Stoic, Unflappable",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_wil_high.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_wil_high, 0, wx.ALL, 5)

        self.std_std_tt_wil_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                u"Alcoholic, Reckless, Spendthrift", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.std_std_tt_wil_low.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_wil_low, 0, wx.ALL, 5)

        self.std_std_tt_cha = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.std_std_tt_cha.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_cha, 0, wx.ALL, 5)

        self.std_std_tt_cha_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                 u"Commanding, Inspiring, Suave, Persuasive", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.std_std_tt_cha_high.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_cha_high, 0, wx.ALL, 5)

        self.std_std_tt_cha_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                u"Unwashed, Disfigured, Obnoxious", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.std_std_tt_cha_low.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_cha_low, 0, wx.ALL, 5)

        self.std_std_tt_rep = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.std_std_tt_rep.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_rep, 0, wx.ALL, 5)

        self.std_std_tt_rep_high = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY,
                                                 u"Well-known, Egotistical", wx.DefaultPosition, wx.DefaultSize, 0)
        self.std_std_tt_rep_high.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_rep_high, 0, wx.ALL, 5)

        self.std_std_tt_rep_low = wx.StaticText(sbs_std_trait_table.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.std_std_tt_rep_low.Wrap(-1)
        fgs_std_trait_table.Add(self.std_std_tt_rep_low, 0, wx.ALL, 5)

        sbs_std_trait_table.Add(fgs_std_trait_table, 1, wx.EXPAND, 5)

        bs_std_1.Add(sbs_std_trait_table, 1, wx.EXPAND, 5)

        sbs_std_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_std_set_trait, wx.ID_ANY, u"Total Stats"), wx.VERTICAL)

        gs_std_stats = wx.GridSizer(0, 12, 0, 0)

        self.st_std_str = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"STR", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_str.Wrap(-1)
        gs_std_stats.Add(self.st_std_str, 0, wx.ALL, 5)

        self.st_std_agi = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"AGI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_agi.Wrap(-1)
        gs_std_stats.Add(self.st_std_agi, 0, wx.ALL, 5)

        self.st_std_end = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"END", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_end.Wrap(-1)
        gs_std_stats.Add(self.st_std_end, 0, wx.ALL, 5)

        self.st_std_int = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"INT", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_int.Wrap(-1)
        gs_std_stats.Add(self.st_std_int, 0, wx.ALL, 5)

        self.st_std_log = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"LOG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_log.Wrap(-1)
        gs_std_stats.Add(self.st_std_log, 0, wx.ALL, 5)

        self.st_std_wil = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"WIL", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_wil.Wrap(-1)
        gs_std_stats.Add(self.st_std_wil, 0, wx.ALL, 5)

        self.st_std_cha = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"CHA", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_cha.Wrap(-1)
        gs_std_stats.Add(self.st_std_cha, 0, wx.ALL, 5)

        self.st_std_luc = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"LUC", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_luc.Wrap(-1)
        gs_std_stats.Add(self.st_std_luc, 0, wx.ALL, 5)

        self.st_std_rep = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"REP", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_rep.Wrap(-1)
        gs_std_stats.Add(self.st_std_rep, 0, wx.ALL, 5)

        self.st_std_mag = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"MAG", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_mag.Wrap(-1)
        gs_std_stats.Add(self.st_std_mag, 0, wx.ALL, 5)

        self.st_std_chi = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"CHI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_chi.Wrap(-1)
        gs_std_stats.Add(self.st_std_chi, 0, wx.ALL, 5)

        self.st_std_psi = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"PSI", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.st_std_psi.Wrap(-1)
        gs_std_stats.Add(self.st_std_psi, 0, wx.ALL, 5)

        self.st_std_str_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"str_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_str_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_str_val, 0, wx.ALL, 5)

        self.st_std_agi_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"agi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_agi_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_agi_val, 0, wx.ALL, 5)

        self.st_std_end_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"end_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_end_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_end_val, 0, wx.ALL, 5)

        self.st_std_int_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"int_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_int_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_int_val, 0, wx.ALL, 5)

        self.st_std_log_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"log_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_log_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_log_val, 0, wx.ALL, 5)

        self.st_std_wil_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"wil_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_wil_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_wil_val, 0, wx.ALL, 5)

        self.st_std_cha_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"cha_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_cha_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_cha_val, 0, wx.ALL, 5)

        self.st_std_luc_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"luc_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_luc_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_luc_val, 0, wx.ALL, 5)

        self.st_std_rep_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"rep_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_rep_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_rep_val, 0, wx.ALL, 5)

        self.st_std_mag_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"mag_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_mag_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_mag_val, 0, wx.ALL, 5)

        self.st_std_chi_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"chi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_chi_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_chi_val, 0, wx.ALL, 5)

        self.st_std_psi_val = wx.StaticText(sbs_std_stats.GetStaticBox(), wx.ID_ANY, u"psi_val", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.st_std_psi_val.Wrap(-1)
        gs_std_stats.Add(self.st_std_psi_val, 0, wx.ALL, 5)

        sbs_std_stats.Add(gs_std_stats, 0, wx.EXPAND, 5)

        bs_std_1.Add(sbs_std_stats, 0, wx.EXPAND, 5)

        bs_std_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_std_ok = wx.Button(self.p_std_set_trait, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_std_buttons.Add(self.b_std_ok, 0, wx.ALL, 5)

        self.b_std_cancel = wx.Button(self.p_std_set_trait, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_std_buttons.Add(self.b_std_cancel, 0, wx.ALL, 5)

        bs_std_1.Add(bs_std_buttons, 0, wx.ALIGN_RIGHT, 5)

        self.p_std_set_trait.SetSizer(bs_std_1)
        self.p_std_set_trait.Layout()
        bs_std_1.Fit(self.p_std_set_trait)
        bs_std_main.Add(self.p_std_set_trait, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_std_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.lb_std_exploit_list.Bind(wx.EVT_LISTBOX, self.on_trait_select)
        self.b_std_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_std_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.trait_list = exploits_traits.exploit_traits_list
        for trait in self.trait_list:
            self.lb_std_exploit_list.Append(trait['Name'])

        self.total_stats = parent.user_character.calc_stat_total()

        self.st_std_str_val.SetLabel(str(self.total_stats['STR']))
        self.st_std_agi_val.SetLabel(str(self.total_stats['AGI']))
        self.st_std_end_val.SetLabel(str(self.total_stats['END']))
        self.st_std_int_val.SetLabel(str(self.total_stats['INT']))
        self.st_std_log_val.SetLabel(str(self.total_stats['LOG']))
        self.st_std_wil_val.SetLabel(str(self.total_stats['WIL']))
        self.st_std_cha_val.SetLabel(str(self.total_stats['CHA']))
        self.st_std_luc_val.SetLabel(str(self.total_stats['LUC']))
        self.st_std_rep_val.SetLabel(str(self.total_stats['REP']))
        self.st_std_mag_val.SetLabel(str(self.total_stats['MAG']))
        self.st_std_chi_val.SetLabel(str(self.total_stats['CHI']))
        self.st_std_psi_val.SetLabel(str(self.total_stats['PSI']))

        self.lb_std_exploit_list.SetSelection(0)
        self.on_trait_select(None)

    def __del__(self):
        pass

    ########################################
    # Additional SetTraitDialog init stuff #
    ########################################
    # self.trait_list = exploits_traits.exploit_traits_list
    # for trait in self.trait_list:
    #     self.lb_std_exploit_list.Append(trait['Name'])
    #
    # self.total_stats = parent.user_character.calc_stat_total()
    #
    # self.st_std_str_val.SetLabel(str(self.total_stats['STR']))
    # self.st_std_agi_val.SetLabel(str(self.total_stats['AGI']))
    # self.st_std_end_val.SetLabel(str(self.total_stats['END']))
    # self.st_std_int_val.SetLabel(str(self.total_stats['INT']))
    # self.st_std_log_val.SetLabel(str(self.total_stats['LOG']))
    # self.st_std_wil_val.SetLabel(str(self.total_stats['WIL']))
    # self.st_std_cha_val.SetLabel(str(self.total_stats['CHA']))
    # self.st_std_luc_val.SetLabel(str(self.total_stats['LUC']))
    # self.st_std_rep_val.SetLabel(str(self.total_stats['REP']))
    # self.st_std_mag_val.SetLabel(str(self.total_stats['MAG']))
    # self.st_std_chi_val.SetLabel(str(self.total_stats['CHI']))
    # self.st_std_psi_val.SetLabel(str(self.total_stats['PSI']))
    #
    # self.lb_std_exploit_list.SetSelection(0)
    # self.on_trait_select(None)

    def on_trait_select(self, event):
        self.tc_std_exploit_desc.SetValue(self.trait_list[self.lb_std_exploit_list.GetSelection()]['Desc'])

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)


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


###########################################################################
## Class EditSkillsDialog
###########################################################################

class EditSkillsDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Edit Skills", pos=wx.DefaultPosition,
                           size=wx.Size(428, 318), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_esd_main = wx.BoxSizer(wx.VERTICAL)

        self.p_esd_edit_skills = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_esd_1 = wx.BoxSizer(wx.VERTICAL)

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

    def __del__(self):
        pass

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

        bs_ecd_1.Add(bs_ecd_career_desc, 1, wx.EXPAND, 5)

        sbs_ecd_skills = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Available Skills"),
                                           wx.VERTICAL)

        self.tc_ecd_skills = wx.TextCtrl(sbs_ecd_skills.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_ecd_skills.SetMinSize(wx.Size(-1, 70))

        sbs_ecd_skills.Add(self.tc_ecd_skills, 0, wx.ALL | wx.EXPAND, 5)

        bs_ecd_1.Add(sbs_ecd_skills, 0, wx.EXPAND, 5)

        bsb_ecd_exploits_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_ecd_exploit_names = wx.StaticBoxSizer(
            wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Available Exploits"), wx.VERTICAL)

        lb_ecd_exploit_listChoices = []
        self.lb_ecd_exploit_list = wx.ListBox(sbs_ecd_exploit_names.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                              wx.DefaultSize, lb_ecd_exploit_listChoices, 0)
        self.lb_ecd_exploit_list.SetMinSize(wx.Size(-1, 140))

        sbs_ecd_exploit_names.Add(self.lb_ecd_exploit_list, 0, wx.ALL | wx.EXPAND, 5)

        bsb_ecd_exploits_desc.Add(sbs_ecd_exploit_names, 1, wx.EXPAND, 5)

        sbs_ecd_exploit_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_ecd_edit_career, wx.ID_ANY, u"Description"),
                                                 wx.VERTICAL)

        self.tc_ecd_exploit_desc = wx.TextCtrl(sbs_ecd_exploit_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_ecd_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_ecd_exploit_desc.Add(self.tc_ecd_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bsb_ecd_exploits_desc.Add(sbs_ecd_exploit_desc, 2, wx.EXPAND, 5)

        bs_ecd_1.Add(bsb_ecd_exploits_desc, 1, wx.EXPAND, 5)

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

    def __del__(self):
        pass

    ##########################################
    # Additional EditCareerDialog init stuff #
    ##########################################
    # self.rb_ecd_origins.SetValue(True)
    # self.show_careers(None)

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


###########################################################################
## Class AddExploitDialog
###########################################################################

class AddExploitDialog(wx.Dialog):
    def __init__(self, parent, career=None, title=u"Add Exploit"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(765, 313), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_aed_main = wx.BoxSizer(wx.VERTICAL)

        self.p_aed_edit_exploits = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_aed_1 = wx.BoxSizer(wx.VERTICAL)

        bs_aed_exploit_desc = wx.BoxSizer(wx.HORIZONTAL)

        sbs_aed_exploits = wx.StaticBoxSizer(wx.StaticBox(self.p_aed_edit_exploits, wx.ID_ANY, u"Exploits"),
                                             wx.HORIZONTAL)

        bs_aed_rb = wx.BoxSizer(wx.VERTICAL)

        self.rb_aed_universal = wx.RadioButton(sbs_aed_exploits.GetStaticBox(), wx.ID_ANY, u"Universal",
                                               wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        bs_aed_rb.Add(self.rb_aed_universal, 0, wx.ALL, 5)

        self.rb_aed_career = wx.RadioButton(sbs_aed_exploits.GetStaticBox(), wx.ID_ANY, u"Career", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bs_aed_rb.Add(self.rb_aed_career, 0, wx.ALL, 5)

        self.rb_aed_android = wx.RadioButton(sbs_aed_exploits.GetStaticBox(), wx.ID_ANY, u"Android", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bs_aed_rb.Add(self.rb_aed_android, 0, wx.ALL, 5)

        self.rb_aed_custom = wx.RadioButton(sbs_aed_exploits.GetStaticBox(), wx.ID_ANY, u"Custom", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bs_aed_rb.Add(self.rb_aed_custom, 0, wx.ALL, 5)

        sbs_aed_exploits.Add(bs_aed_rb, 0, wx.EXPAND, 5)

        bs_aed_exploits_list_and_rb = wx.BoxSizer(wx.HORIZONTAL)

        lb_aed_exploit_listChoices = []
        self.lb_aed_exploit_list = wx.ListBox(sbs_aed_exploits.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                              wx.DefaultSize, lb_aed_exploit_listChoices, 0)
        self.lb_aed_exploit_list.SetMinSize(wx.Size(-1, 120))

        bs_aed_exploits_list_and_rb.Add(self.lb_aed_exploit_list, 0, wx.ALL, 5)

        sbs_aed_exploits.Add(bs_aed_exploits_list_and_rb, 0, wx.EXPAND, 5)

        bs_aed_exploit_desc.Add(sbs_aed_exploits, 0, wx.EXPAND, 5)

        sbs_aed_exploit_desc = wx.StaticBoxSizer(wx.StaticBox(self.p_aed_edit_exploits, wx.ID_ANY, u"Description"),
                                                 wx.VERTICAL)

        self.tc_aed_exploit_desc = wx.TextCtrl(sbs_aed_exploit_desc.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.tc_aed_exploit_desc.SetMinSize(wx.Size(-1, 140))

        sbs_aed_exploit_desc.Add(self.tc_aed_exploit_desc, 0, wx.ALL | wx.EXPAND, 5)

        bs_aed_exploit_desc.Add(sbs_aed_exploit_desc, 2, wx.EXPAND, 5)

        bs_aed_1.Add(bs_aed_exploit_desc, 1, wx.EXPAND, 5)

        bs_aed_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_aed_ok = wx.Button(self.p_aed_edit_exploits, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_aed_buttons.Add(self.b_aed_ok, 0, wx.ALL, 5)

        self.b_aed_cancel = wx.Button(self.p_aed_edit_exploits, wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bs_aed_buttons.Add(self.b_aed_cancel, 0, wx.ALL, 5)

        bs_aed_1.Add(bs_aed_buttons, 0, wx.ALIGN_RIGHT, 5)

        self.p_aed_edit_exploits.SetSizer(bs_aed_1)
        self.p_aed_edit_exploits.Layout()
        bs_aed_1.Fit(self.p_aed_edit_exploits)
        bs_aed_main.Add(self.p_aed_edit_exploits, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_aed_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.rb_aed_universal.Bind(wx.EVT_RADIOBUTTON, self.show_exploits)
        self.rb_aed_career.Bind(wx.EVT_RADIOBUTTON, self.show_exploits)
        self.rb_aed_android.Bind(wx.EVT_RADIOBUTTON, self.show_exploits)
        self.rb_aed_custom.Bind(wx.EVT_RADIOBUTTON, self.show_exploits)
        self.lb_aed_exploit_list.Bind(wx.EVT_LISTBOX, self.on_exploit_select)
        self.b_aed_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_aed_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        if career is None:
            self.rb_aed_career.Enable(False)
            self.rb_aed_career.Hide()
        if not custom_exploits_loaded:
            self.rb_aed_custom.Enable(False)
            self.rb_aed_custom.Hide()

        self.show_exploits(None)
        self.on_exploit_select(None)

    def __del__(self):
        pass

    ###########################################
    # Additional AddExploitsDialog init stuff #
    ###########################################
    # if career is None:
    #     self.rb_aed_career.Enable(False)
    #     self.rb_aed_career.Hide()
    # if not custom_exploits_loaded:
    #     self.rb_aed_custom.Enable(False)
    #     self.rb_aed_custom.Hide()
    #
    # self.show_exploits(None)
    # self.on_exploit_select(None)

    ###############################
    # AddExploitsDialog Functions #
    ###############################
    def get_exploit_list(self):
        exploit_list = None
        if self.rb_aed_universal.GetValue():
            exploit_list = exploits_universal.exploit_universal_list
        elif self.rb_aed_android.GetValue():
            exploit_list = exploits_android.exploit_android_list
        elif self.rb_aed_career.GetValue():
            exploit_list = self.career.available_exploits
        elif self.rb_aed_custom.GetValue():
            exploit_list = custom_exploits.custom_exploit_list
        return exploit_list

    def get_list_source(self):
        list_source = None
        if self.rb_aed_universal.GetValue():
            list_source = 'universal'
        elif self.rb_aed_android.GetValue():
            list_source = 'android'
        elif self.rb_aed_career.GetValue():
            list_source = 'career'
        elif self.rb_aed_custom.GetValue():
            list_source = 'custom'
        return list_source

    def show_exploits(self, event):
        exploit_list = self.get_exploit_list()
        self.lb_aed_exploit_list.Clear()

        for exploit in exploit_list:
            self.lb_aed_exploit_list.Append(exploit['Name'])

        self.lb_aed_exploit_list.SetSelection(0)
        self.on_exploit_select(None)

    def on_exploit_select(self, event):
        exploit_list = self.get_exploit_list()
        selected_exploit = self.lb_aed_exploit_list.GetSelection()
        self.tc_aed_exploit_desc.SetValue(exploit_list[selected_exploit]['Desc'])

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)


def main():
    ######################
    # Launch application #
    ######################
    app = wx.App()
    main_window = WCA_Frame(None)
    main_window.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
