#!/usr/bin/python
# coding=utf-8

# User interface adapted from https://github.com/Cog-Creators/Red-DiscordBot

import platform
import subprocess


#####################
# Support functions #
#####################
def clear_screen():
    if platform.system() == 'Windows':
        command = 'cls'
    else:
        command = 'clear'
    subprocess.call(command, shell=True)


def select_yes_no():
    selection = None
    while selection != 'y' and selection != 'n':
        selection = input('(Y/N)> ').lower().strip()
    return selection == 'y'


def user_selection():
    return input('> ').strip()


def tidy_line(count):
    # This little bit ensures that we get a line break no matter what count ends on
    if not (count - 1) % 3 == 0:
        print()


def wait():
    input('Press enter to continue.')
