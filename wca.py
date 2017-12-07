from lib.gui.wca_frame import WCA_Frame
import wx
import logging
import sys


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))
    exception_info_str = 'Uncaught exception:\n\n{}\n\nSee \'error.log\' for details.'.format(
        logging.Formatter().formatException(ei=(exc_type, exc_value, exc_traceback)))
    wx.MessageBox(exception_info_str, 'WOIN Character Assistant', wx.ICON_ERROR | wx.OK)


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        filename='error.log', level=logging.ERROR)
    sys.excepthook = handle_exception

    ######################
    # Launch application #
    ######################
    app = wx.App()
    main_window = WCA_Frame(None)
    main_window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
