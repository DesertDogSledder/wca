import wx
import wx.xrc


###########################################################################
## Class SetDefenseSkillsDialog
###########################################################################

class SetDefenseSkillsDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Set Defense Skills", pos=wx.DefaultPosition,
                           size=wx.Size(699, 161), style=wx.DEFAULT_DIALOG_STYLE)

        skills_dict = parent.user_character.calc_skill_total()
        skills = []
        for skill, value in skills_dict.items():
            skills.append(skill)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bs_sdsd_main = wx.BoxSizer(wx.VERTICAL)

        bs_sdsd_def_skills = wx.BoxSizer(wx.HORIZONTAL)

        sbs_sdsd_melee = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Melee Defense"), wx.VERTICAL)

        c_sdsd_meleeChoices = skills
        self.c_sdsd_melee = wx.Choice(sbs_sdsd_melee.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      c_sdsd_meleeChoices, 0)
        self.c_sdsd_melee.SetSelection(0)
        sbs_sdsd_melee.Add(self.c_sdsd_melee, 0, wx.ALL | wx.EXPAND, 5)

        bs_sdsd_def_skills.Add(sbs_sdsd_melee, 1, wx.EXPAND, 5)

        sbs_sdsd_ranged = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Ranged Defense"), wx.VERTICAL)

        c_sdsd_rangedChoices = skills
        self.c_sdsd_ranged = wx.Choice(sbs_sdsd_ranged.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      c_sdsd_rangedChoices, 0)
        self.c_sdsd_ranged.SetSelection(0)
        sbs_sdsd_ranged.Add(self.c_sdsd_ranged, 0, wx.ALL | wx.EXPAND, 5)

        bs_sdsd_def_skills.Add(sbs_sdsd_ranged, 1, wx.EXPAND, 5)

        sbs_sdsd_mental = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Mental Defense"), wx.VERTICAL)

        c_sdsd_mentalChoices = skills
        self.c_sdsd_mental = wx.Choice(sbs_sdsd_mental.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       c_sdsd_mentalChoices, 0)
        self.c_sdsd_mental.SetSelection(0)
        sbs_sdsd_mental.Add(self.c_sdsd_mental, 0, wx.ALL | wx.EXPAND, 5)

        bs_sdsd_def_skills.Add(sbs_sdsd_mental, 1, wx.EXPAND, 5)

        sbs_sdsd_vital = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Vital Defense"), wx.VERTICAL)

        c_sdsd_vitalChoices = skills
        self.c_sdsd_vital = wx.Choice(sbs_sdsd_vital.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      c_sdsd_vitalChoices, 0)
        self.c_sdsd_vital.SetSelection(0)
        sbs_sdsd_vital.Add(self.c_sdsd_vital, 0, wx.ALL | wx.EXPAND, 5)

        bs_sdsd_def_skills.Add(sbs_sdsd_vital, 1, wx.EXPAND, 5)

        bs_sdsd_main.Add(bs_sdsd_def_skills, 1, wx.EXPAND, 5)

        bs_sdsd_buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.b_sdsd_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_sdsd_buttons.Add(self.b_sdsd_ok, 0, wx.ALL, 5)

        self.b_sdsd_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bs_sdsd_buttons.Add(self.b_sdsd_cancel, 0, wx.ALL, 5)

        bs_sdsd_main.Add(bs_sdsd_buttons, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bs_sdsd_main)
        self.Layout()

        self.Centre(wx.BOTH)

        self.b_sdsd_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.b_sdsd_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

    def __del__(self):
        pass

        ################################################
        # Additional SetDefenseSkillsDialog init stuff #
        ################################################
        # skills_dict = parent.user_character.calc_skill_total()
        # skills = []
        # for skill, value in skills_dict.items():
        #     skills.append(skill)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)
