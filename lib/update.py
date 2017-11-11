#!/usr/bin/python
# coding=utf-8

# User interface adapted from https://github.com/Cog-Creators/Red-DiscordBot

import subprocess


#########################
# WCA Update and Repair #
#########################
def update_wca():
    try:
        code = subprocess.call(("git", "pull", "--ff-only"))
    except FileNotFoundError:
        print("\nError: Git not found. It's either not installed or not in "
              "the PATH environment variable like requested in the guide.")
        return
    if code == 0:
        print("\nWCA has been updated")
    else:
        print("\nWCA could not update properly. If this is caused by edits "
              "you have made to the code you can try the repair option ")


def repair_wca():
    code = subprocess.call(("git", "reset", "--hard"))
    if code == 0:
        print("WCA has been restored to the last local commit.")
    else:
        print("The repair has failed.")
