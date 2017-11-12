#!/usr/bin/python
# coding=utf-8

# User interface adapted from https://github.com/Cog-Creators/Red-DiscordBot

import subprocess


#########################
# WCA Update and Repair #
#########################
def update_wca():
    try:
        p = subprocess.Popen(("git", "pull", "--ff-only"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
    except FileNotFoundError:
        print("\nError: Git not found. It's either not installed or not in "
              "the PATH environment variable like requested in the guide.")
        return
    if p.returncode == 0:
        print("\nWCA has been updated")
    else:
        print("\nWCA could not update properly. If this is caused by edits "
              "you have made to the code you can try the repair option ")
        print('STDOUT: {}'.format(out))
        print('STDERR: {}'.format(err))


def repair_wca():
    p = subprocess.Popen(("git", "reset", "--hard"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode == 0:
        print("WCA has been restored to the last local commit.")
    else:
        print("The repair has failed.")
        print('STDOUT: {}'.format(out))
        print('STDERR: {}'.format(err))
