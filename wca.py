#!/usr/bin/python
# coding=utf-8

# WOIN Character Assistant
# Built using the WOIN Rules Reference Document available at http://www.woinrpg.com/introduction/
# User interface adapted from https://github.com/Cog-Creators/Red-DiscordBot

import copy
import pickle
import shutil
import textwrap
from os import listdir
from os.path import isfile, join

from data.careers import *
from data.exploits import *
from data.homeworlds import *
from data.races import *
from lib import dice, character, tui

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

user_character = None

banner = ('========================\n'
          'WOIN Character Assistant\n'
          '========================\n')


#################
# WCA functions #
#################
def new_character():
    global user_character
    if user_character is not None:
        print('Character exists.  Overwrite?')
        if not tui.select_yes_no():
            return

    user_character = character.Character(race=copy.deepcopy(races_new.race_new_human),
                                         homeworld=copy.deepcopy(homeworlds_new.homeworld_none),
                                         age_descriptor='young')

    print('New character initialized.  Use the \'Edit Character\' menu to start making changes!')
    tui.wait()


def edit_character():
    global user_character
    menu_name = 'Edit Character'
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('1. Name ({})'.format(user_character.name))
        print('2. Race ({})'.format(user_character.race.name))
        print('3. Hook ({})'.format(user_character.hook))
        print('4. Homeworld ({})'.format(user_character.homeworld.name))
        print('5. Careers')
        print('6. Trait ({})'.format(user_character.trait['Name']))
        print('7. Misc exploits')
        print('8. Age descriptor ({})'.format(user_character.age_descriptor))
        print('\n0. Back')

        selection = tui.user_selection()

        if selection == '1':
            edit_name(menu_name)
        elif selection == '2':
            edit_race(menu_name)
        elif selection == '3':
            edit_hook(menu_name)
        elif selection == '4':
            edit_homeworld(menu_name)
        elif selection == '5':
            edit_careers(menu_name)
        elif selection == '6':
            edit_trait(menu_name)
        elif selection == '7':
            edit_misc_exploits(menu_name)
        elif selection == '8':
            edit_age_descriptor(menu_name)
        elif selection == '0':
            break


def edit_name(parent_menu):
    global user_character
    menu_name = '{} >> Name'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Name: {}\n'.format(user_character.name))

        print('Enter new name')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection()

        if selection != '':
            user_character.name = selection
            break
        else:
            break


def edit_race(parent_menu):
    global user_character
    menu_name = '{} >> Race'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Race: {}\n'.format(user_character.race.name))

        print('1. Select race')
        print('2. Select racial skills')
        print('3. Edit racial stats')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            set_race_main(menu_name)
        elif selection == '2':
            edit_race_skills(menu_name)
        elif selection == '3':
            edit_race_stats(menu_name)
        elif selection == '0':
            break


def set_race_main(parent_menu):
    global user_character
    menu_name = '{} >> Select Race'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Race: {}\n'.format(user_character.race.name))

        print('1. OLD races')
        print('2. NOW races')
        print('3. NEW races')
        if custom_races_loaded:
            print('4. Custom races')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            set_race_sub(menu_name, 'OLD Races', races_old.race_old_list)
        elif selection == '2':
            set_race_sub(menu_name, 'NOW Races', races_now.race_now_list)
        elif selection == '3':
            set_race_sub(menu_name, 'NEW Races', races_new.race_new_list)
        elif selection == '4' and custom_races_loaded:
            set_race_sub(menu_name, 'Custom Races', custom_races.custom_race_list)
        elif selection == '0':
            break


def set_race_sub(parent_menu, sub_menu_name, race_list):
    global user_character
    menu_name = '{} >> {}'.format(parent_menu, sub_menu_name)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Race: {}\n'.format(user_character.race.name))

        width = terminal_size[0]
        count = 1
        for race in race_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, race.name, width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, race.name))
            count += 1
        tui.tidy_line(count)

        print('\n0. Back\n')
        selection = tui.user_selection()

        if selection == '0':
            break
        try:
            num_selection = int(selection)
            tui.clear_screen()
            print(race_list[num_selection-1])
            print('\nSelect this race?')
            if tui.select_yes_no():
                user_character.race = copy.deepcopy(race_list[num_selection-1])
                user_character.race_stats = copy.deepcopy(user_character.race.stats)
                break
            else:
                break
        except ValueError:
            pass


def edit_race_skills(parent_menu):
    global user_character
    menu_name = '{} >> Select Racial Skills'.format(parent_menu)
    info = 'Characters typically take three different skills from the race\'s skill choices.'
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        for line in textwrap.wrap(info, width):
            print(line)

        count = 1
        print('\nAvailable racial skills ({}):'.format(user_character.race.name))
        for skill in user_character.race.available_skills:
            if not count % 3 == 0:
                print('{:{width}}'.format(skill, width=width//4), end='')
            else:
                print('{}'.format(skill))
            count += 1
        tui.tidy_line(count)

        selected_skills = ''
        for skill_pick in user_character.race_skill_choices:
            selected_skills += '{}, '.format(skill_pick)
        selected_skills = selected_skills[:-2]

        if len(selected_skills) != 0:
            print('\nCurrent selected skills: {}\n'.format(selected_skills))
        else:
            print('\nCurrent selected skills: (None)\n')

        print('Enter a skill name to add')
        print('Enter existing skill name to remove')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection().lower()

        if selection == '':
            break

        if selection not in user_character.race_skill_choices:
            user_character.race_skill_choices.append(selection)
            user_character.race_skill_choices.sort()
        else:
            user_character.race_skill_choices.remove(selection)


def edit_race_stats(parent_menu):
    global user_character
    menu_name = '{} >> Stats'.format(parent_menu)
    info = 'This menu is useful for changing the stat bonuses granted by a race (for example, the Human \'Varied\' ' \
           'exploit).'
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        for line in textwrap.wrap(info, width):
            print(line)

        print('\nCurrent stats:')
        count = 1
        for stat, value in user_character.race_stats.items():
            if not count % 3 == 0:
                print('{}: {:<{width}}'.format(stat, value, width=width//4), end='')
            else:
                print('{}: {}'.format(stat, value))
            count += 1
        tui.tidy_line(count)

        print('\nPick stat to edit')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection().upper()[:3]

        if selection == '':
            break
        elif selection in user_character.race_stats:
            try:
                print('Enter new value')
                print('Leave blank to abort and return to previous menu')
                selection_2 = tui.user_selection()
                if selection_2 == '':
                    break
                user_character.race_stats[selection] = int(selection_2)
            except ValueError:
                print('Invalid value.')


def edit_homeworld(parent_menu):
    global user_character
    menu_name = '{} >> Homeworld'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Homeworld: {}\n'.format(user_character.homeworld.name))

        print('1. Select homeworld')
        print('2. Select homeworld skills')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            set_homeworld_main(menu_name)
        elif selection == '2':
            edit_homeworld_skills(menu_name)
        elif selection == '0':
            break


def set_homeworld_main(parent_menu):
    global user_character
    menu_name = '{} >> Set Homeworld'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Homeworld: {}\n'.format(user_character.homeworld.name))

        print('1. NEW homeworlds')
        if custom_homeworlds_loaded:
            print('2. Custom homeworlds')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            set_homeworld_sub(menu_name, 'NEW homeworlds', homeworlds_new.homeworld_new_list)
        elif selection == '2' and custom_homeworlds_loaded:
            set_homeworld_sub(menu_name, 'Custom homeworlds',custom_homeworlds.custom_homeworld_list)
        elif selection == '0':
            break


def set_homeworld_sub(parent_menu, sub_menu_name, homeworld_list):
    global user_character
    menu_name = '{} >> {}'.format(parent_menu, sub_menu_name)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current Homeworld: {}\n'.format(user_character.homeworld.name))

        width = terminal_size[0]
        count = 1
        for homeworld in homeworld_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, homeworld.name, width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, homeworld.name))
            count += 1
        tui.tidy_line(count)
        print('\n0. Back\n')
        selection = tui.user_selection()

        if selection == '0':
            break
        try:
            num_selection = int(selection)
            tui.clear_screen()
            print(homeworld_list[num_selection-1])
            print('\nSelect this homeworld?')
            if tui.select_yes_no():
                user_character.homeworld = copy.deepcopy(homeworld_list[num_selection-1])
                break
            else:
                break
        except ValueError:
            pass


def edit_homeworld_skills(parent_menu):
    global user_character
    menu_name = '{} >> Select Homeworld Skills'.format(parent_menu)
    info = 'Characters typically take one skill from the homeworld\'s skill choices.'
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        for line in textwrap.wrap(info, width):
            print(line)

        count = 1
        print('\nAvailable homeworld skills:\n')
        for skill in user_character.homeworld.available_skills:
            if not count % 3 == 0:
                print('{:{width}}'.format(skill, width=width//4), end='')
            else:
                print('{}'.format(skill))
            count += 1
        tui.tidy_line(count)

        selected_skills = ''
        for skill_pick in user_character.homeworld_skill_choices:
            selected_skills += '{}, '.format(skill_pick)
        selected_skills = selected_skills[:-2]

        if len(selected_skills) != 0:
            print('\nCurrent selected skills: {}\n'.format(selected_skills))
        else:
            print('\nCurrent selected skills: (None)\n')

        print('Enter a skill name to add')
        print('Enter existing skill name to remove')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection().lower()

        if selection == '':
            break

        if selection not in user_character.homeworld_skill_choices:
            user_character.homeworld_skill_choices.append(selection)
            user_character.homeworld_skill_choices.sort()
        else:
            user_character.homeworld_skill_choices.remove(selection)


def edit_hook(parent_menu):
    global user_character
    menu_name = '{} >> Edit Hook'.format(parent_menu)
    tui.clear_screen()
    print(banner)
    print('{}\n'.format(menu_name))
    print('Hook: {}\n'.format(user_character.hook))

    print('Enter new hook')
    print('Leave blank to abort and return to previous menu')

    selection = tui.user_selection()

    if selection != '':
        user_character.hook = selection


def edit_careers(parent_menu):
    global user_character
    menu_name = '{} >> Careers'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        career_track = ''
        count = 1
        for career in user_character.career_track:
            career_track += '[{}] {}, '.format(count, career['Career'].name)
            count += 1
        career_track = career_track[:-2]

        if career_track != '':
            print('Current career track: {}\n'.format(career_track))
        else:
            print('Current career track: (None)\n')

        print('1. Add career')
        print('2. Change career order')
        print('3. Edit career details')
        print('4. Remove career')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            add_career_main(menu_name)
        elif selection == '2':
            change_career_order(menu_name)
        elif selection == '3':
            edit_career_details_main(menu_name)
        elif selection == '4':
            remove_career(menu_name)
        elif selection == '0':
            break


def add_career_main(parent_menu):
    global user_character
    menu_name = '{} >> Add Careers'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('1. Origins')
        print('2. OLD careers')
        print('3. NOW careers')
        print('4. NEW careers')
        print('5. Martial arts careers')
        if custom_careers_loaded:
            print('6. Custom careers')
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            add_career_sub(menu_name, 'Origins', origins.career_woin_origin_list)
            break
        elif selection == '2':
            add_career_sub(menu_name, 'OLD Careers', careers_old.career_old_list)
            break
        elif selection == '3':
            add_career_sub(menu_name, 'NOW Careers', careers_now.career_now_list)
            break
        elif selection == '4':
            add_career_sub(menu_name, 'NEW Careers', careers_new.career_new_list)
            break
        elif selection == '5':
            add_career_sub(menu_name, 'Martial Arts Careers', careers_martial_arts.career_ma_list)
            break
        elif selection == '6' and custom_careers_loaded:
            add_career_sub(menu_name, 'Custom Careers', custom_careers.custom_career_list)
            break
        elif selection == '0':
            break


def add_career_sub(parent_menu, sub_menu_name, career_list):
    global user_character
    menu_name = '{} >> {}'.format(parent_menu, sub_menu_name)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        width = terminal_size[0]
        count = 1
        for career in career_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, career.name, width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, career.name))
            count += 1
        tui.tidy_line(count)

        print('\n0. Back\n')
        selection = tui.user_selection()

        if selection == '0':
            break
        if selection == '0':
            break
        try:
            num_selection = int(selection)
            tui.clear_screen()
            print(career_list[num_selection-1])
            print('\nSelect this career?')
            if tui.select_yes_no():
                user_character.career_track.append({'Career': copy.deepcopy(career_list[num_selection-1]),
                                                    'Length': '{} {}'.format(
                                                        dice.roll(career_list[num_selection - 1].career_time)['total'],
                                                        career_list[num_selection-1].career_time_unit),
                                                    'Stats': copy.deepcopy(career_list[num_selection-1].stats),
                                                    'Skills': [],
                                                    'Exploit': {'Name': 'unset career exploit', 'Desc': 'unset'},
                                                    'Notes': ''})
                break
            else:
                break
        except ValueError:
            pass


def change_career_order(parent_menu):
    global user_character
    menu_name = '{} >> Change Career Order'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        count = 1
        for career in user_character.career_track:
            print('{}. {}'.format(count, career['Career'].name))
            count += 1

        print('\n0. Back\n')

        print('Select first career number to swap (0 to abort):')
        selection = tui.user_selection()

        if selection == '0':
            break

        print('Select second career number to swap (0 to abort):')
        selection_2 = tui.user_selection()

        if selection_2 == '0':
            break

        try:
            user_character.career_track[int(selection)-1], user_character.career_track[int(selection_2)-1] = \
                user_character.career_track[int(selection_2)-1], user_character.career_track[int(selection)-1]
        except IndexError:
            print('\nInvalid selections.\n')
            tui.wait()
        except ValueError:
            print('\nInvalid selections.\n')
            tui.wait()


def edit_career_details_main(parent_menu):
    global user_character
    menu_name = '{} >> Edit Career Details'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        count = 1

        for career in user_character.career_track:
            print('{}. {}'.format(count, career['Career'].name))
            count += 1
        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '0':
            break

        try:
            num_selection = int(selection)
            edit_career_details_sub(menu_name, num_selection-1)
        except ValueError:
            pass
        except IndexError:
            pass


def edit_career_details_sub(parent_menu, index):
    global user_character
    menu_name = '{} >> [{}] {}'.format(parent_menu, index+1, user_character.career_track[index]['Career'].name)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        print('1. Select skills')
        print('2. Select exploit')
        print('3. Change stats (Career attribute exchange)')
        print('4. Edit notes')

        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            edit_career_details_skills(menu_name, index)
        elif selection == '2':
            edit_career_details_exploits_main(menu_name, index)
        elif selection == '3':
            edit_career_details_stats(menu_name, index)
        elif selection == '4':
            edit_career_details_notes(menu_name, index)
        elif selection == '0':
            break


def edit_career_details_skills(parent_menu, index):
    global user_character
    menu_name = '{} >> Skills'.format(parent_menu)
    info = 'Characters typically take two different skills per career grade. You are permitted to select one' \
           ' defensive skill in lieu of the career\'s skill choices.'
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        
        for line in textwrap.wrap(info, width):
            print(line)

        count = 1
        print('\nAvailable career skills:')
        for skill in user_character.career_track[index]['Career'].available_skills:
            if not count % 3 == 0:
                print('{:{width}}'.format(skill, width=width//4), end='')
            else:
                print('{}'.format(skill))
            count += 1
        tui.tidy_line(count)

        selected_skills = ''
        for skill_pick in user_character.career_track[index]['Skills']:
            selected_skills += '{}, '.format(skill_pick)
        selected_skills = selected_skills[:-2]

        if len(selected_skills) != 0:
            print('\nCurrent selected skills: {}\n'.format(selected_skills))
        else:
            print('\nCurrent selected skills: (None)\n')

        print('Enter a skill name to add')
        print('Enter existing skill name to remove')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection().lower()

        if selection == '':
            break

        if selection not in user_character.career_track[index]['Skills']:
            user_character.career_track[index]['Skills'].append(selection)
            user_character.career_track[index]['Skills'].sort()
        else:
            user_character.career_track[index]['Skills'].remove(selection)


def edit_career_details_exploits_main(parent_menu, index):
    global user_character
    menu_name = '{} >> Exploits'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        if user_character.career_track[index]['Exploit'] != {}:
            print('Current exploit: {}\n'.format(user_character.career_track[index]['Exploit']['Name']))
        else:
            print('Current exploit: (None)\n')

        print('1. Career exploits')
        print('2. Universal exploits')
        if custom_exploits_loaded:
            print('3. Custom exploits')

        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            edit_career_details_exploits_sub(menu_name, 'Career Exploits', index,
                                             user_character.career_track[index]['Career'].available_exploits)
        elif selection == '2':
            edit_career_details_exploits_sub(menu_name, 'Universal Exploits', index,
                                             exploits_universal.exploit_universal_list)
        elif selection == '3' and custom_exploits_loaded:
            edit_career_details_exploits_sub(menu_name, 'Custom Exploits', index,
                                             custom_exploits.custom_exploit_list)
        elif selection == '0':
            break


def edit_career_details_exploits_sub(parent_menu, sub_menu_name, index, exploit_list):
    global user_character
    menu_name = '{} >> {}'.format(parent_menu, sub_menu_name)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        width = terminal_size[0]
        count = 1
        for exploit in exploit_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, exploit['Name'], width=width//3), end='')
            else:
                print('{:2}. {}'.format(count, exploit['Name']))
            count += 1
        tui.tidy_line(count)

        print('\n0. Back\n')
        selection = tui.user_selection()

        if selection == '0':
            break
        try:
            num_selection = int(selection)
            tui.clear_screen()
            print('{} - {}'.format(exploit_list[num_selection-1]['Name'], exploit_list[num_selection-1]['Desc']))
            print('\nSelect this exploit?')
            if tui.select_yes_no():
                user_character.career_track[index]['Exploit'] = copy.deepcopy(exploit_list[num_selection-1])
                break
            else:
                break
        except ValueError:
            pass


def edit_career_details_stats(parent_menu, index):
    global user_character
    menu_name = '{} >> Stats'.format(parent_menu)
    info = 'Some races noted for a particular attribute have an ability which allows them to ' \
           'optionally exchange one of these four attribute increases for a different one, as ' \
           'long as it doesn\'t result in a duplicate attribute advancement.'
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        for line in textwrap.wrap(info, width):
            print(line)

        print('\nCurrent stats:')
        count = 1
        for stat, value in user_character.career_track[index]['Stats'].items():
            if not count % 3 == 0:
                print('{}: {:<{width}}'.format(stat, value, width=width//4), end='')
            else:
                print('{}: {}'.format(stat, value))
            count += 1
        tui.tidy_line(count)

        print('\nPick stat to edit')
        print('Leave blank to abort and return to previous menu')
        selection = tui.user_selection().upper()[:3]

        if selection == '':
            break
        elif selection in user_character.career_track[index]['Stats']:
            try:
                print('Enter new value')
                print('Leave blank to abort and return to previous menu')
                selection_2 = tui.user_selection()
                if selection_2 == '':
                    break
                user_character.career_track[index]['Stats'][selection] = int(selection_2)
            except ValueError:
                print('Invalid value.')


def edit_career_details_notes(parent_menu, index):
    global user_character
    menu_name = '{} >> Edit Notes'.format(parent_menu)
    terminal_size = shutil.get_terminal_size()
    width = terminal_size[0]
    tui.clear_screen()
    print(banner)
    print('{}\n'.format(menu_name))

    for line in textwrap.wrap('Edit notes for this particular career grade here.  This is useful for making note '
                              'of important information related to the career grade.  For example, you might note '
                              'the skill focus for your character\'s College career here.', width):
        print(line)

    print('\nCurrent notes:\n')
    for line in textwrap.wrap(user_character.career_track[index]['Notes'], width):
        print(line)

    print('\nEnter new note (0 to abort):')
    selection = tui.user_selection()
    if selection != '0':
        user_character.career_track[index]['Notes'] = selection


def remove_career(parent_menu):
    global user_character
    menu_name = '{} >> Remove Career'.format(parent_menu)
    while True:
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        count = 1
        for career in user_character.career_track:
            print('{}. {}'.format(count, career['Career'].name))
            count += 1

        print('\n0. Back\n')

        print('Select career to remove')
        selection = tui.user_selection()

        if selection == '0':
            break

        try:
            num_selection = int(selection)
            print('Career: {}'.format(user_character.career_track[num_selection-1]['Career'].name))
            print('Length: {}'.format(user_character.career_track[num_selection-1]['Length']))
            print('Stats: ', end='')
            for stat, value in user_character.career_track[num_selection-1]['Stats'].items():
                if value < 0 or value > 0:
                    print('{}: {}  '.format(stat, value), end='')
            print('\nSkills: {}'.format(user_character.career_track[num_selection-1]['Skills']))

            if user_character.career_track[num_selection-1]['Exploit'] != dict():
                print('Exploit: {}'.format(user_character.career_track[num_selection-1]['Exploit']['Name']))
            else:
                print('Exploit: none selected')

            print('\nRemove this career from the character?')
            if tui.select_yes_no():
                user_character.career_track.pop(num_selection-1)
            break
        except ValueError:
            pass
        except IndexError:
            pass


def edit_trait(parent_menu):
    global user_character
    menu_name = '{} >> Trait'.format(parent_menu)
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))
        print('Current trait: {}'.format(user_character.trait['Name']))
        print('Current stats:')
        count = 1
        for stat, value in user_character.calc_stat_total().items():
            if not count % 3 == 0:
                print('{}: {:<{width}}'.format(stat, value, width=width//4), end='')
            else:
                print('{}: {}'.format(stat, value))
            count += 1
        tui.tidy_line(count)

        print()
        count = 1
        for exploit in exploits_traits.exploit_traits_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, exploit['Name'], width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, exploit['Name']))
            count += 1

        tui.tidy_line(count)

        print('\n0. Back')

        selection = tui.user_selection()

        if selection == '0':
            break

        try:
            num_selection = int(selection)

            print('{} - {}'.format(exploits_traits.exploit_traits_list[num_selection-1]['Name'],
                                   exploits_traits.exploit_traits_list[num_selection-1]['Desc']))

            print('Select this trait?')
            if tui.select_yes_no():
                user_character.trait = copy.deepcopy(exploits_traits.exploit_traits_list[num_selection-1])
                break
        except IndexError:
            pass
        except ValueError:
            pass


def edit_misc_exploits(parent_menu):
    global user_character
    menu_name = '{} >> Misc Exploits'.format(parent_menu)
    while True:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        if len(user_character.misc_exploits) != 0:
            print('Current misc exploits:')
            count = 1
            for exploit in user_character.misc_exploits:
                if not count % 3 == 0:
                    print('{:{width}}'.format(exploit['Name'], width=width//4), end='')
                else:
                    print('{}'.format(exploit['Name']))
                count += 1
            tui.tidy_line(count)
        else:
            print('Current misc exploits: (None)')

        print('\n1. Add exploits')
        print('2. Remove exploits')

        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            add_misc_exploits_main(menu_name)
        elif selection == '2':
            remove_misc_exploits(menu_name)
        elif selection == '0':
            break


def add_misc_exploits_main(parent_menu):
    global user_character
    menu_name = '{} >> Add'.format(parent_menu)
    while True:
        print(banner)
        print('{}\n'.format(menu_name))

        print('1. Universal exploits')
        print('2. Android exploits')
        if custom_exploits_loaded:
            print('3. Custom exploits')

        print('\n0. Back\n')

        selection = tui.user_selection()

        if selection == '1':
            add_misc_exploits_sub(menu_name, 'Universal Exploits', exploits_universal.exploit_universal_list)
            break
        elif selection == '2':
            add_misc_exploits_sub(menu_name, 'Android Exploits', exploits_android.exploit_android_list)
            break
        elif selection == '3' and custom_exploits_loaded:
            add_misc_exploits_sub(menu_name, 'Custom Exploits', custom_exploits.custom_exploit_list)
            break
        elif selection == '0':
            break


def add_misc_exploits_sub(parent_menu, sub_menu_name, exploit_list):
    global user_character
    menu_name = '{} >> {}'.format(parent_menu, sub_menu_name)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        width = terminal_size[0]
        count = 1
        for exploit in exploit_list:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, exploit['Name'], width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, exploit['Name']))
            count += 1
        tui.tidy_line(count)

        print('\n0. Back\n')
        selection = tui.user_selection()

        if selection == '0':
            break
        try:
            num_selection = int(selection)
            tui.clear_screen()
            print('{} - {}'.format(exploit_list[num_selection-1]['Name'], exploit_list[num_selection-1]['Desc']))
            print('\nSelect this exploit?')
            if tui.select_yes_no() and exploit_list[num_selection-1] not in user_character.misc_exploits:
                user_character.misc_exploits.append(copy.deepcopy(exploit_list[num_selection-1]))
                user_character.misc_exploits.sort(key=lambda x: x['Name'])
                break
            else:
                break
        except ValueError:
            pass


def remove_misc_exploits(parent_menu):
    global user_character
    menu_name = '{} >> Remove'.format(parent_menu)
    while True:
        terminal_size = shutil.get_terminal_size()
        tui.clear_screen()
        print(banner)
        print('{}\n'.format(menu_name))

        width = terminal_size[0] // 3
        count = 1
        for exploit in user_character.misc_exploits:
            if not count % 3 == 0:
                print('{:2}. {:{width}}'.format(count, exploit['Name'], width=width//4), end='')
            else:
                print('{:2}. {}'.format(count, exploit['Name']))
            count += 1
        tui.tidy_line(count)

        print('\n0. Back')

        print('Select exploit to remove')
        selection = tui.user_selection()

        if selection == '0':
            break

        try:
            num_selection = int(selection)
            print('{} - {}'.format(user_character.misc_exploits[num_selection-1]['Name'],
                                   user_character.misc_exploits[num_selection-1]['Desc']))
            print('Remove this exploit?')
            if tui.select_yes_no():
                user_character.misc_exploits.pop(num_selection-1)
        except ValueError:
            pass
        except IndexError:
            pass


def edit_age_descriptor(parent_menu):
    global user_character
    menu_name = '{} >> Edit Age Descriptor'.format(parent_menu)
    info = "Your age is determined by the total of your character's years in each career and is based on their " \
           "species.\nExamples: 'young', 'adult', 'old', 'immortal', 'mechanical'"
    terminal_size = shutil.get_terminal_size()
    width = terminal_size[0]
    tui.clear_screen()
    print(banner)
    print('{}\n'.format(menu_name))
    for line in textwrap.wrap(info, width):
        print(line)
    print('\nCurrent age descriptor: {}\n'.format(user_character.age_descriptor))

    print('Enter new age descriptor')
    print('Leave blank to abort and return to previous menu')

    selection = tui.user_selection()

    if selection != '':
        user_character.age_descriptor = selection


def load_character():
    global user_character
    menu_name = 'Load Character'
    tui.clear_screen()
    print(banner)
    print('{}\n'.format(menu_name))
    if user_character is not None:
        print('Character exists.  Overwrite?')
        if not tui.select_yes_no():
            return

    character_files = [f for f in listdir('./characters') if isfile(join('./characters', f)) and '.wca' in f]
    print('Available character files:\n')
    for file in character_files:
        print(file[:-4])

    print('\nEnter character file name to load')
    print('Leave blank to abort and return to previous menu')
    selection = tui.user_selection()

    if selection == '':
        return

    try:
        with open('characters/{}.wca'.format(selection), 'rb') as f:
            user_character = pickle.load(f)
            print('Successfully loaded \"{}\".'.format(selection))
            tui.wait()
    except FileNotFoundError:
        print('File not found.')
        tui.wait()
    except pickle.UnpicklingError:
        print('Malformed file.')
        tui.wait()
    except EOFError:
        print('Malformed file.')
        tui.wait()


def save_character():
    global user_character
    menu_name = 'Save Character'
    tui.clear_screen()
    print(banner)
    print('{}\n'.format(menu_name))

    print('Enter desired file name')
    print('Leave blank to abort and return to previous menu')
    selection = tui.user_selection()

    if selection == '':
        return

    character_files = [f for f in listdir('./characters') if isfile(join('./characters', f)) and '.wca' in f]
    if '{}.wca'.format(selection) in character_files:
        print('File \"{}\" exists.  Overwrite?'.format(selection))
        if not tui.select_yes_no():
            return
    with open('characters/{}.wca'.format(selection), 'wb') as f:
        pickle.dump(user_character, f, pickle.HIGHEST_PROTOCOL)


#############
# WCA main! #
#############
def main():
    global user_character
    while True:
        tui.clear_screen()
        print(banner)

        print('Main menu:\n')
        print('1. New character')
        print('2. Load character')
        if user_character is not None:
            print('3. Edit character')
            print('4. View character')
            print('5. Save character')
        print('\n0. Exit\n')

        selection = tui.user_selection()

        if selection == '1':
            new_character()
        elif selection == '2':
            load_character()
        elif selection == '3' and user_character is not None:
            edit_character()
        elif selection == '4' and user_character is not None:
            print(user_character)
            tui.wait()
        elif selection == '5' and user_character is not None:
            save_character()
        elif selection == '0':
            if user_character is not None:
                print('Unsaved changes will be lost. Are you sure you want to exit?')
                if tui.select_yes_no():
                    break
            else:
                break
    tui.clear_screen()


if __name__ == '__main__':
    main()
