# -*- coding: utf-8 -*-

import wx
import wx.xrc
from data.exploits import *

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