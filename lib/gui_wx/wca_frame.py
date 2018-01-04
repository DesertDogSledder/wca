import collections
import copy
import pickle
import re

import wx
import wx.xrc

from data.homeworlds import *
from data.races import *
from lib import dice, character
from lib.gui_wx.add_exploit_dialog import AddExploitDialog
from lib.gui_wx.change_homeworld_dialog import ChangeHomeworldDialog
from lib.gui_wx.change_race_dialog import ChangeRaceDialog
from lib.gui_wx.edit_career_dialog import EditCareerDialog
from lib.gui_wx.edit_skills_dialog import EditSkillsDialog
from lib.gui_wx.set_defense_skills_dialog import SetDefenseSkillsDialog
from lib.gui_wx.set_trait_dialog import SetTraitDialog


###########################################################################
## Class WCA_Frame
###########################################################################

class WCA_Frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"WOIN Character Assistant", pos=wx.DefaultPosition,
                          size=wx.Size(660, 780), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar = wx.MenuBar(0)
        self.m_file = wx.Menu()
        self.mi_file_new = wx.MenuItem(self.m_file, wx.ID_ANY, u"New" + u"\t" + u"Ctrl+N", wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_new)

        self.mi_file_open = wx.MenuItem(self.m_file, wx.ID_ANY, u"Open..." + u"\t" + u"Ctrl+O", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_open)

        self.mi_file_save = wx.MenuItem(self.m_file, wx.ID_ANY, u"Save" + u"\t" + u"Ctrl+S", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_save)
        self.mi_file_save.Enable(False)

        self.mi_file_save_as = wx.MenuItem(self.m_file, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_save_as)
        self.mi_file_save_as.Enable(False)

        self.m_file.AppendSeparator()

        self.mi_file_export = wx.MenuItem(self.m_file, wx.ID_ANY, u"Export...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_export)
        self.mi_file_export.Enable(False)

        self.m_file.AppendSeparator()

        self.mi_file_quit = wx.MenuItem(self.m_file, wx.ID_ANY, u"Quit" + u"\t" + u"Alt+F4", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.m_file.Append(self.mi_file_quit)

        self.m_menubar.Append(self.m_file, u"File")

        self.m_help = wx.Menu()
        self.mi_help_about = wx.MenuItem(self.m_help, wx.ID_ANY, u"About..." + u"\t" + u"F1", wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.m_help.Append(self.mi_help_about)

        self.m_menubar.Append(self.m_help, u"Help")

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

        self.st_overview_hook = wx.StaticText(sbs_overview_info.GetStaticBox(), wx.ID_ANY, u"Hook", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_overview_hook.Wrap(-1)
        gbs_overview_info_1.Add(self.st_overview_hook, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.tc_overview_hook_val = wx.TextCtrl(sbs_overview_info.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        gbs_overview_info_1.Add(self.tc_overview_hook_val, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

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

        bs_overview_main.Add(sbs_overview_exploits, 0, wx.EXPAND, 5)

        sbs_overview_derived_stats = wx.StaticBoxSizer(wx.StaticBox(self.p_overview, wx.ID_ANY, u"Derived Stats"),
                                                       wx.VERTICAL)

        fgs_overview_derived_stats = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_overview_derived_stats.AddGrowableCol(0)
        fgs_overview_derived_stats.AddGrowableCol(1)
        fgs_overview_derived_stats.SetFlexibleDirection(wx.VERTICAL)
        fgs_overview_derived_stats.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        sbs_overview_ds_health = wx.StaticBoxSizer(
            wx.StaticBox(sbs_overview_derived_stats.GetStaticBox(), wx.ID_ANY, u"Health"), wx.VERTICAL)

        self.st_overview_ds_health_val = wx.StaticText(sbs_overview_ds_health.GetStaticBox(), wx.ID_ANY, u"ds_health",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_health_val.Wrap(-1)
        sbs_overview_ds_health.Add(self.st_overview_ds_health_val, 0, wx.ALL, 5)

        fgs_overview_derived_stats.Add(sbs_overview_ds_health, 1, wx.EXPAND, 5)

        sbs_overview_ds_intiative = wx.StaticBoxSizer(
            wx.StaticBox(sbs_overview_derived_stats.GetStaticBox(), wx.ID_ANY, u"Initiative"), wx.VERTICAL)

        self.st_overview_ds_initiative_val = wx.StaticText(sbs_overview_ds_intiative.GetStaticBox(), wx.ID_ANY,
                                                           u"ds_init", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_initiative_val.Wrap(-1)
        sbs_overview_ds_intiative.Add(self.st_overview_ds_initiative_val, 0, wx.ALL, 5)

        fgs_overview_derived_stats.Add(sbs_overview_ds_intiative, 1, wx.EXPAND, 5)

        sbs_overview_ds_movement = wx.StaticBoxSizer(
            wx.StaticBox(sbs_overview_derived_stats.GetStaticBox(), wx.ID_ANY, u"Movement"), wx.VERTICAL)

        bs_overview_ds_movement = wx.BoxSizer(wx.HORIZONTAL)

        fgs_overview_ds_movement_1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_overview_ds_movement_1.AddGrowableCol(1)
        fgs_overview_ds_movement_1.SetFlexibleDirection(wx.BOTH)
        fgs_overview_ds_movement_1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.st_overview_ds_speed = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Speed",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_speed.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_speed, 0, wx.ALL, 5)

        self.st_overview_ds_speed_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"speed_val",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_speed_val.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_speed_val, 0, wx.ALL, 5)

        self.st_overview_ds_climb = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Climb",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_climb.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_climb, 0, wx.ALL, 5)

        self.st_overview_ds_climb_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"climb_val",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_climb_val.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_climb_val, 0, wx.ALL, 5)

        self.st_overview_ds_swim = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Swim",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_swim.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_swim, 0, wx.ALL, 5)

        self.st_overview_ds_swim_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"swim_val",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_swim_val.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_swim_val, 0, wx.ALL, 5)

        self.st_overview_ds_vertical_jump = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                          u"Ver. Jump", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_vertical_jump.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_vertical_jump, 0, wx.ALL, 5)

        self.st_overview_ds_vertical_jump_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                              u"v_jump_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_vertical_jump_val.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_vertical_jump_val, 0, wx.ALL, 5)

        self.st_overview_ds_carry = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Carry",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_carry.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_carry, 0, wx.ALL, 5)

        self.st_overview_ds_carry_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"carry_val",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_carry_val.Wrap(-1)
        fgs_overview_ds_movement_1.Add(self.st_overview_ds_carry_val, 0, wx.ALL, 5)

        bs_overview_ds_movement.Add(fgs_overview_ds_movement_1, 1, wx.EXPAND, 5)

        fgs_overview_ds_movement_2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_overview_ds_movement_2.SetFlexibleDirection(wx.BOTH)
        fgs_overview_ds_movement_2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.st_overview_ds_zero_g = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Zero-G",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_zero_g.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_zero_g, 0, wx.ALL, 5)

        self.st_overview_ds_zero_g_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                       u"zero_g_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_zero_g_val.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_zero_g_val, 0, wx.ALL, 5)

        self.st_overview_ds_low_g = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"Low-G",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_low_g.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_low_g, 0, wx.ALL, 5)

        self.st_overview_ds_low_g_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"low_g_val",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_low_g_val.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_low_g_val, 0, wx.ALL, 5)

        self.st_overview_ds_high_g = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY, u"High-G",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_high_g.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_high_g, 0, wx.ALL, 5)

        self.st_overview_ds_high_g_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                       u"high_g_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_high_g_val.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_high_g_val, 0, wx.ALL, 5)

        self.st_overview_ds_horizonal_jump = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                           u"Hor. Jump", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_horizonal_jump.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_horizonal_jump, 0, wx.ALL, 5)

        self.st_overview_ds_horizontal_jump_val = wx.StaticText(sbs_overview_ds_movement.GetStaticBox(), wx.ID_ANY,
                                                                u"h_jump_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_horizontal_jump_val.Wrap(-1)
        fgs_overview_ds_movement_2.Add(self.st_overview_ds_horizontal_jump_val, 0, wx.ALL, 5)

        bs_overview_ds_movement.Add(fgs_overview_ds_movement_2, 1, wx.EXPAND, 5)

        sbs_overview_ds_movement.Add(bs_overview_ds_movement, 1, wx.EXPAND, 5)

        fgs_overview_derived_stats.Add(sbs_overview_ds_movement, 1, wx.EXPAND, 5)

        sbs_overview_ds_defense = wx.StaticBoxSizer(
            wx.StaticBox(sbs_overview_derived_stats.GetStaticBox(), wx.ID_ANY, u"Defense"), wx.VERTICAL)

        fgs_overview_ds_defense_1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_overview_ds_defense_1.SetFlexibleDirection(wx.BOTH)
        fgs_overview_ds_defense_1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.st_overview_ds_defense_melee = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY, u"Melee",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_melee.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_melee, 0, wx.ALL, 5)

        self.st_overview_ds_defense_melee_val = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY,
                                                              u"melee_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_melee_val.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_melee_val, 0, wx.ALL, 5)

        self.st_overview_ds_defense_ranged = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY, u"Ranged",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_ranged.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_ranged, 0, wx.ALL, 5)

        self.st_overview_ds_defense_ranged_val = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY,
                                                               u"ranged_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_ranged_val.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_ranged_val, 0, wx.ALL, 5)

        self.st_overview_ds_defense_mental = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY, u"Mental",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_mental.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_mental, 0, wx.ALL, 5)

        self.st_overview_ds_defense_mental_val = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY,
                                                               u"mental_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_mental_val.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_mental_val, 0, wx.ALL, 5)

        self.st_overview_ds_defense_vital = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY, u"Vital",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_vital.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_vital, 0, wx.ALL, 5)

        self.st_overview_ds_defense_vital_val = wx.StaticText(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY,
                                                              u"vital_val", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_overview_ds_defense_vital_val.Wrap(-1)
        fgs_overview_ds_defense_1.Add(self.st_overview_ds_defense_vital_val, 0, wx.ALL, 5)

        sbs_overview_ds_defense.Add(fgs_overview_ds_defense_1, 1, wx.EXPAND, 5)

        self.b_overview_ds_set_def_skills = wx.Button(sbs_overview_ds_defense.GetStaticBox(), wx.ID_ANY,
                                                      u"Set Defense Skills", wx.DefaultPosition, wx.DefaultSize, 0)
        sbs_overview_ds_defense.Add(self.b_overview_ds_set_def_skills, 0, wx.ALL, 5)

        fgs_overview_derived_stats.Add(sbs_overview_ds_defense, 1, wx.EXPAND, 5)

        sbs_overview_derived_stats.Add(fgs_overview_derived_stats, 1, wx.EXPAND, 5)

        bs_overview_main.Add(sbs_overview_derived_stats, 0, wx.EXPAND, 5)

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

        bs_race_race_size = wx.BoxSizer(wx.HORIZONTAL)

        sbs_race_race = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Race"), wx.VERTICAL)

        self.st_race_race_val = wx.StaticText(sbs_race_race.GetStaticBox(), wx.ID_ANY, u"char_race", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.st_race_race_val.Wrap(-1)
        sbs_race_race.Add(self.st_race_race_val, 0, wx.ALL, 5)

        self.b_race_edit = wx.Button(sbs_race_race.GetStaticBox(), wx.ID_ANY, u"Change Race", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbs_race_race.Add(self.b_race_edit, 0, wx.ALL, 5)

        bs_race_race_size.Add(sbs_race_race, 1, wx.EXPAND, 5)

        sbs_race_size = wx.StaticBoxSizer(wx.StaticBox(self.p_race, wx.ID_ANY, u"Size"), wx.VERTICAL)

        c_race_sizeChoices = [u"Tiny", u"Small", u"Medium", u"Large", u"Enormous", u"Gigantic", u"Colossal", u"Titanic"]
        self.c_race_size = wx.Choice(sbs_race_size.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     c_race_sizeChoices, 0)
        self.c_race_size.SetSelection(2)
        sbs_race_size.Add(self.c_race_size, 0, wx.ALL, 5)

        bs_race_race_size.Add(sbs_race_size, 1, wx.EXPAND, 5)

        bs_race.Add(bs_race_race_size, 0, wx.EXPAND, 5)

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
        self.Bind(wx.EVT_CLOSE, self.quit_wca)
        self.Bind(wx.EVT_MENU, self.new_character, id=self.mi_file_new.GetId())
        self.Bind(wx.EVT_MENU, self.open_file, id=self.mi_file_open.GetId())
        self.Bind(wx.EVT_MENU, self.save_file, id=self.mi_file_save.GetId())
        self.Bind(wx.EVT_MENU, self.save_as_file, id=self.mi_file_save_as.GetId())
        self.Bind(wx.EVT_MENU, self.export_file, id=self.mi_file_export.GetId())
        self.Bind(wx.EVT_MENU, self.quit_wca, id=self.mi_file_quit.GetId())
        self.Bind(wx.EVT_MENU, self.show_about, id=self.mi_help_about.GetId())
        self.tc_overview_name_val.Bind(wx.EVT_TEXT, self.set_character_name)
        self.tc_overview_name_val.Bind(wx.EVT_TEXT_ENTER, self.set_character_name)
        self.b_overview_change_trait.Bind(wx.EVT_BUTTON, self.change_trait)
        self.tc_overview_hook_val.Bind(wx.EVT_TEXT, self.set_character_hook)
        self.tc_overview_hook_val.Bind(wx.EVT_TEXT_ENTER, self.set_character_hook)
        self.b_overview_ds_set_def_skills.Bind(wx.EVT_BUTTON, self.set_defense_skills)
        self.b_race_edit.Bind(wx.EVT_BUTTON, self.change_race)
        self.c_race_size.Bind(wx.EVT_CHOICE, self.set_race_size)
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
        self.character_not_saved = False
        self.file_name = 'untitled'
        self.path_name = None
        self.version = 'v0.20.3'

    def __del__(self):
        pass

    ##################################
    # Additional WCAFrame init stuff #
    ##################################
    # self.nb_main.Hide()
    # self.character_not_saved = False
    # self.file_name = 'untitled'
    # self.path_name = None
    # self.version = 'v0.0.0'

    ######################
    # WCAFrame Functions #
    ######################

    ##################
    # Menu functions #
    ##################
    def new_character(self, event):
        if self.character_not_saved:
            prompt_response = wx.MessageBox("There are unsaved changes.  Would you like to save before quitting?",
                                            "WOIN Character Assistant",
                                            wx.ICON_QUESTION | wx.YES_NO | wx.CANCEL, self)
            if prompt_response == wx.YES:
                self.save_as_file(None)
            elif prompt_response == wx.CANCEL:
                return

        self.nb_main.Show()
        self.user_character = character.Character(race={'Race': copy.deepcopy(races_new.race_new_human),
                                                        'Source': 'new',
                                                        'Skills': [],
                                                        'Size': 'medium',
                                                        'Stats': copy.deepcopy(races_new.race_new_human.stats)},
                                                  homeworld={'Homeworld': copy.deepcopy(homeworlds_new.homeworld_none),
                                                             'Source': 'new',
                                                             'Skills': []},
                                                  age_descriptor='young')
        self.mi_file_save.Enable(True)
        self.mi_file_save_as.Enable(True)
        self.mi_file_export.Enable(True)

        # Update
        self.update_overview_tab(None)
        self.update_race_tab(None)
        self.update_homeworld_tab(None)
        self.update_career_tab(None)
        self.update_exploits_tab(None)
        self.on_career_select(None)
        self.on_misc_exploit_select(None)

        self.file_name = 'untitled'
        self.file_path = None
        self.character_not_saved = False
        self.SetTitle('{} - WOIN Character Assistant'.format(self.file_name))

    def open_file(self, event):
        if self.character_not_saved:
            prompt_response = wx.MessageBox("There are unsaved changes.  Would you like to save before quitting?",
                                            "WOIN Character Assistant",
                                            wx.ICON_QUESTION | wx.YES_NO | wx.CANCEL, self)
            if prompt_response == wx.YES:
                self.save_as_file(None)
            elif prompt_response == wx.CANCEL:
                return

        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open Character file", wildcard="WCA files (*.wca)|*.wca",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            path_name = file_dialog.GetPath()
            try:
                with open(path_name, 'rb') as file:
                    match = re.search('.*[/\\\\](.*?)\.wca', path_name)
                    self.file_path = path_name
                    self.file_name = match.group(1)
                    self.user_character = pickle.load(file)
            except IOError:
                wx.LogError("Cannot open file '{}'.".format(file))
        self.mi_file_save.Enable(True)
        self.mi_file_save_as.Enable(True)
        self.mi_file_export.Enable(True)
        self.nb_main.Show()
        # Update
        self.update_overview_tab(None)
        self.update_race_tab(None)
        self.update_homeworld_tab(None)
        self.update_career_tab(None)
        self.update_exploits_tab(None)
        self.on_career_select(None)
        self.on_misc_exploit_select(None)
        self.character_not_saved = False
        self.SetTitle('{} - WOIN Character Assistant'.format(self.file_name))

    def save_file(self, event):
        if self.file_path is not None:
            try:
                with open(self.file_path, 'wb') as file:
                    pickle.dump(self.user_character, file, pickle.HIGHEST_PROTOCOL)
                self.character_not_saved = False
                self.SetTitle('{} - WOIN Character Assistant'.format(self.file_name))
            except IOError:
                wx.LogError("Cannot save current data in file '{}}'.".format(self.file_path))
        else:
            self.save_as_file(None)

    def save_as_file(self, event):
        with wx.FileDialog(self, "Save WCA file", wildcard="WCA files (*.wca)|*.wca",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            path_name = file_dialog.GetPath()
            try:
                with open(path_name, 'wb') as file:
                    pickle.dump(self.user_character, file, pickle.HIGHEST_PROTOCOL)
                match = re.search('.*[/\\\\](.*?)\.wca', path_name)
                self.file_path = path_name
                self.file_name = match.group(1)
                self.character_not_saved = False
                self.SetTitle('{} - WOIN Character Assistant'.format(self.file_name))
            except IOError:
                wx.LogError("Cannot save current data in file '{}}'.".format(path_name))

    def export_file(self, event):
        with wx.FileDialog(self, "Export character text file", wildcard="Text files (*.txt)|*.txt",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            path_name = file_dialog.GetPath()
            try:
                with open(path_name, 'w') as file:
                    file.write(str(self.user_character))
            except IOError:
                wx.LogError("Cannot save current data in file '{}}'.".format(path_name))

    def quit_wca(self, event):
        if self.character_not_saved:
            prompt_response = wx.MessageBox("There are unsaved changes.  Would you like to save before quitting?",
                                            "WOIN Character Assistant",
                                            wx.ICON_QUESTION | wx.YES_NO | wx.CANCEL, self)
            if prompt_response == wx.YES:
                self.save_as_file(None)
            elif prompt_response == wx.CANCEL:
                if event.CanVeto():
                    event.Veto()
                return
        self.Destroy()

    def show_about(self, event):
        about_str = 'WOIN Character Assistant {}\n'.format(self.version)
        about_str += '    A character creation tool for the WOIN RPG\n'
        about_str += '    http://www.woinrpg.com/\n'
        about_str += '\nWritten by:\n'
        about_str += 'DesertDogSledder'
        wx.MessageBox(about_str, 'WOIN Character Assistant', wx.ICON_INFORMATION | wx.OK)

    #########################
    # Tab refresh functions #
    #########################
    def update_overview_tab(self, event):
        total_stats = self.user_character.calc_stat_total()

        self.tc_overview_name_val.SetValue(self.user_character.name)
        self.st_overview_homeworld_val.SetLabel(self.user_character.homeworld['Homeworld'].name)
        self.st_overview_race_val.SetLabel(self.user_character.race['Race'].name)
        self.st_overview_trait_val.SetLabel(self.user_character.trait['Name'])
        self.tc_overview_hook_val.SetValue(self.user_character.hook)

        skill_total = self.user_character.calc_skill_total()
        skill_total_str = ''
        for skill, value in skill_total.items():
            skill_total_str += '{} - {} ({}d6)\n'.format(skill, value, character.calc_dice_pool_size(value))
        self.tc_overview_skills.SetValue(skill_total_str)

        self.st_total_str_val.SetLabel('{} ({}d6)'.format(total_stats['STR'],
                                                          character.calc_dice_pool_size(total_stats['STR'])))
        self.st_total_agi_val.SetLabel('{} ({}d6)'.format(total_stats['AGI'],
                                                          character.calc_dice_pool_size(total_stats['AGI'])))
        self.st_total_end_val.SetLabel('{} ({}d6)'.format(total_stats['END'],
                                                          character.calc_dice_pool_size(total_stats['END'])))
        self.st_total_int_val.SetLabel('{} ({}d6)'.format(total_stats['INT'],
                                                          character.calc_dice_pool_size(total_stats['INT'])))
        self.st_total_log_val.SetLabel('{} ({}d6)'.format(total_stats['LOG'],
                                                          character.calc_dice_pool_size(total_stats['LOG'])))
        self.st_total_wil_val.SetLabel('{} ({}d6)'.format(total_stats['WIL'],
                                                          character.calc_dice_pool_size(total_stats['WIL'])))
        self.st_total_cha_val.SetLabel('{} ({}d6)'.format(total_stats['CHA'],
                                                          character.calc_dice_pool_size(total_stats['CHA'])))
        self.st_total_luc_val.SetLabel('{} ({}d6)'.format(total_stats['LUC'],
                                                          character.calc_dice_pool_size(total_stats['LUC'])))
        self.st_total_rep_val.SetLabel('{} ({}d6)'.format(total_stats['REP'],
                                                          character.calc_dice_pool_size(total_stats['REP'])))
        self.st_total_mag_val.SetLabel('{} ({}d6)'.format(total_stats['MAG'],
                                                          character.calc_dice_pool_size(total_stats['MAG'])))
        self.st_total_chi_val.SetLabel('{} ({}d6)'.format(total_stats['CHI'],
                                                          character.calc_dice_pool_size(total_stats['CHI'])))
        self.st_total_psi_val.SetLabel('{} ({}d6)'.format(total_stats['PSI'],
                                                          character.calc_dice_pool_size(total_stats['PSI'])))

        all_exploits_str = ''
        for exploit in self.user_character.get_all_exploits():
            all_exploits_str += '{} - {}\n\n'.format(exploit['Name'], exploit['Desc'])

        self.tc_overview_exploits.SetValue(all_exploits_str)

        derived_stats = self.user_character.calc_derived_stats()

        self.st_overview_ds_health_val.SetLabel(derived_stats['Health'])
        self.st_overview_ds_initiative_val.SetLabel('{}d6'.format(derived_stats['Initiative']))

        self.st_overview_ds_speed_val.SetLabel(str(derived_stats['Speed']))
        self.st_overview_ds_climb_val.SetLabel(str(derived_stats['Climb']))
        self.st_overview_ds_swim_val.SetLabel(str(derived_stats['Swim']))
        self.st_overview_ds_zero_g_val.SetLabel(str(derived_stats['Zero-G']))
        self.st_overview_ds_low_g_val.SetLabel(str(derived_stats['Low-G']))
        self.st_overview_ds_high_g_val.SetLabel(str(derived_stats['High-G']))
        self.st_overview_ds_carry_val.SetLabel(str(derived_stats['Carry']))
        self.st_overview_ds_vertical_jump_val.SetLabel('{}\'/{}\''.format(derived_stats['Vertical Jump Running'],
                                                                          derived_stats['Vertical Jump Standing']))
        self.st_overview_ds_horizontal_jump_val.SetLabel('{}\'/{}\''.format(derived_stats['Horizontal Jump Running'],
                                                                            derived_stats['Horizontal Jump Standing']))

        self.st_overview_ds_defense_melee_val.SetLabel(str(derived_stats['Melee Defense']))
        self.st_overview_ds_defense_ranged_val.SetLabel(str(derived_stats['Ranged Defense']))
        self.st_overview_ds_defense_mental_val.SetLabel(str(derived_stats['Mental Defense']))
        self.st_overview_ds_defense_vital_val.SetLabel(str(derived_stats['Vital Defense']))

        self.character_not_saved = True
        self.SetTitle('*{} - WOIN Character Assistant'.format(self.file_name))

    def update_race_tab(self, event):
        self.st_race_race_val.SetLabel(self.user_character.race['Race'].name)
        size_choices = ['tiny', 'small', 'medium', 'large', 'enormous', 'gigantic', 'colossal']

        self.c_race_size.SetSelection(size_choices.index(self.user_character.race['Size'].lower()))

        selected_race_skills = ''
        for skill_pick in self.user_character.race['Skills']:
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
        for skill_pick in self.user_character.homeworld['Skills']:
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
        self.character_not_saved = True
        self.SetTitle('*{} - WOIN Character Assistant'.format(self.file_name))

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

    def set_character_hook(self, event):
        self.user_character.hook = event.GetString()
        self.character_not_saved = True
        self.SetTitle('*{} - WOIN Character Assistant'.format(self.file_name))

    def set_defense_skills(self, event):
        set_defense_skills_dialog = SetDefenseSkillsDialog(self)
        melee_index = set_defense_skills_dialog.c_sdsd_melee.FindString(
            self.user_character.defense_skills['Melee'])
        if melee_index != wx.NOT_FOUND:
            set_defense_skills_dialog.c_sdsd_melee.SetSelection(melee_index)

        ranged_index = set_defense_skills_dialog.c_sdsd_melee.FindString(
            self.user_character.defense_skills['Ranged'])
        if ranged_index != wx.NOT_FOUND:
            set_defense_skills_dialog.c_sdsd_ranged.SetSelection(ranged_index)

        mental_index = set_defense_skills_dialog.c_sdsd_melee.FindString(
            self.user_character.defense_skills['Mental'])
        if mental_index != wx.NOT_FOUND:
            set_defense_skills_dialog.c_sdsd_mental.SetSelection(mental_index)

        vital_index = set_defense_skills_dialog.c_sdsd_melee.FindString(
            self.user_character.defense_skills['Vital'])
        if vital_index != wx.NOT_FOUND:
            set_defense_skills_dialog.c_sdsd_vital.SetSelection(vital_index)

        results = set_defense_skills_dialog.ShowModal()

        if results == wx.ID_OK:
            melee_selection = set_defense_skills_dialog.c_sdsd_melee.GetSelection()
            ranged_selection = set_defense_skills_dialog.c_sdsd_ranged.GetSelection()
            mental_selection = set_defense_skills_dialog.c_sdsd_mental.GetSelection()
            vital_selection = set_defense_skills_dialog.c_sdsd_vital.GetSelection()
            self.user_character.defense_skills['Melee'] = set_defense_skills_dialog.c_sdsd_melee.GetString(
                melee_selection)
            self.user_character.defense_skills['Ranged'] = set_defense_skills_dialog.c_sdsd_ranged.GetString(
                ranged_selection)
            self.user_character.defense_skills['Mental'] = set_defense_skills_dialog.c_sdsd_mental.GetString(
                mental_selection)
            self.user_character.defense_skills['Vital'] = set_defense_skills_dialog.c_sdsd_vital.GetString(
                vital_selection)

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
                                        'Skills': [],
                                        'Size': 'Medium',
                                        'Source': race_dialog.get_list_source()}
            self.update_race_tab(None)
            self.update_overview_tab(None)

    def set_race_size(self, event):
        size_selection = self.c_race_size.GetSelection()
        self.user_character.race['Size'] = self.c_race_size.GetString(size_selection).lower()
        self.update_overview_tab(None)

    def edit_race_skills(self, event):
        race_skills_dialog = EditSkillsDialog(self, self.user_character.race['Race'].available_skills)
        for skill in self.user_character.race['Skills']:
            race_skills_dialog.lb_esd_skills_list.Append(skill)
        results = race_skills_dialog.ShowModal()
        if results == wx.ID_OK:
            self.user_character.race['Skills'] = copy.deepcopy(race_skills_dialog.lb_esd_skills_list.GetItems())
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
                                             'Skills': [],
                                             'Source': homeworld_dialog.get_list_source()}
            self.update_homeworld_tab(None)
            self.update_overview_tab(None)

    def edit_homeworld_skills(self, event):
        homeworld_skills_dialog = EditSkillsDialog(self, self.user_character.homeworld['Homeworld'].available_skills)
        for skill in self.user_character.homeworld['Skills']:
            homeworld_skills_dialog.lb_esd_skills_list.Append(skill)
        results = homeworld_skills_dialog.ShowModal()
        if results == wx.ID_OK:
            self.user_character.homeworld['Skills'] = copy.deepcopy(
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
        set_career_exploit = AddExploitDialog(self, career_track_index, u"Set Career Exploit")
        if 'Source' in self.user_character.career_track[career_track_index]['Exploit']:
            list_source = self.user_character.career_track[career_track_index]['Exploit']['Source']
        else:
            list_source = None
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
            self.update_career_tab(None)
            self.update_overview_tab(None)
            self.lb_careers_list.SetSelection(career_track_index)
            self.on_career_select(None)

    def edit_career_skills(self, event):
        selected_career = self.lb_careers_list.GetSelection()
        career_skills_dialog = EditSkillsDialog(self, self.user_character.career_track[
            selected_career]['Career'].available_skills)
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