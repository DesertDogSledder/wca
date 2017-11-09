from lib import tui, update
import wca

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
            wca.main()
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
