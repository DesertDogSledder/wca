#!/usr/bin/python
# coding=utf-8

# User interface adapted from https://github.com/Cog-Creators/Red-DiscordBot

import subprocess
import os
import shutil


#########################
# WCA Update and Repair #
#########################
def update_wca():
    try:
        p = subprocess.Popen(('git', 'pull', '--ff-only'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode().strip()
        err = err.decode().strip()
    except FileNotFoundError:
        print("\nError: Git not found. It's either not installed or not in "
              "the PATH environment variable.")
        return
    print(out)
    if p.returncode == 0:
        print("\nWCA has been updated.")
        print("\nClearing cache.")
        for dir_name, subdir_list, file_list in os.walk('.'):
            if '__pycache__' in dir_name:
                print('    Removing {}'.format(dir_name))
                shutil.rmtree(dir_name)
    else:
        if err == 'fatal: Not a git repository (or any of the parent directories): .git':
            print('Git repository not yet initialized.  Run the repair option first.')
        else:
            print("\nWCA could not update properly. If this is caused by edits "
                  "you have made to the code you can try the repair option.")
            print('Error message: {}'.format(err))


def repair_wca():
    print("\nClearing cache.")
    for dir_name, subdir_list, file_list in os.walk('.'):
        if '__pycache__' in dir_name:
            print('    Removing {}'.format(dir_name))
            shutil.rmtree(dir_name)
    print()
    try:
        out, err = subprocess.Popen(('git', 'init'), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        out = out.decode().strip()
        err = err.decode().strip()
        if out != '':
            print(out)
        if err != '':
            print(err)
        print()

        out, err = subprocess.Popen(('git', 'remote', 'add', 'origin', 'https://github.com/DesertDogSledder/wca'), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        out = out.decode().strip()
        err = err.decode().strip()
        if out != '':
            print(out)
        if err == 'fatal: remote origin already exists.':
            print('Remote origin already set.')
        else:
            print(err)
        print()

        out, err = subprocess.Popen(('git', 'fetch', 'origin', 'master'), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        out = out.decode().strip()
        err = err.decode().strip()
        if out != '':
            print(out)
        if err != '':
            print(err)
        print()

        out, err = subprocess.Popen(('git', 'reset', '--hard', 'FETCH_HEAD'), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        out = out.decode().strip()
        err = err.decode().strip()
        if out != '':
            print(out)
        if err != '':
            print(err)
        print()

        out, err = subprocess.Popen(('git', 'branch', '--set-upstream-to=origin/master', 'master'), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        out = out.decode().strip()
        err = err.decode().strip()
        if out != '':
            print(out)
        if err != '':
            print(err)
        print()
    except FileNotFoundError:
        print("\nError: Git not found. It's either not installed or not in "
              "the PATH environment variable.")
        return
