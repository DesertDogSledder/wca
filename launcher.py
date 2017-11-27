from lib import tui, update
try:
    import wca_gui_wx
except ImportError:
    message = ('Failed to launch WCA GUI. Do you have wxPython installed? Try typing\n'
               '    pip install -U wxPython\n'
               'or visit https://wxpython.org/pages/downloads/ for more information on how to install '
               'wxPython')
    print(message)
    tui.wait()
banner = ('=================================\n'
          'WOIN Character Assistant Launcher\n'
          '=================================\n')


def main():
    while True:
        tui.clear_screen()
        print(banner)

        print('Main menu:\n')
        print('1. Launch WCA')
        print('2. Update WCA')
        print('3. Repair WCA')

        print('\n0. Exit\n')

        selection = tui.user_selection()

        if selection == '1':
            wca_gui_wx.main()
            break
        elif selection == '2':
            update.update_wca()
            tui.wait()
        elif selection == '3':
            update.repair_wca()
            tui.wait()
        elif selection == '0':
            break


if __name__ == '__main__':
    main()
