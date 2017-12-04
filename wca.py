from lib.gui.wca_frame import WCA_Frame
import wx

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
