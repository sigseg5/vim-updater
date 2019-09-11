#!/usr/bin/env python3

from sys import exit as sys_exit
from os import path
from os import mkdir

from src.Utilities.os_checker import check_os
from src.Utilities.git_checker import check_git_on_device
from src.Utilities.git_downloader_from_internet import openBrowser
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_system
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_src
from src.Utilities.git_utilities import git_action

UPDATER_VER = "0.0.1"
OS_TYPE = check_os()

# fixme: UnicodeDecodeError on windows. Temp solution with try-except
# 'utf-8' codec can't decode byte 0xad in pos 6: invalid start byte
try:
    GIT_STATUS = check_git_on_device()
except UnicodeDecodeError:
    print("unicode decode error")
    sys_exit(1)

GIT_DOWNLOAD_PAGE = "http://git-scm.com/"
USER_FOLDER = path.expanduser("~")
UPDATER_DIR = "/.vim_updater"
VIM_FOLDER = "/vim"

VIM_REPO = "https://github.com/vim/vim.git"
# VIM_REPO = "https://github.com/kirillNK/webpack-template.git"

if OS_TYPE == "win32":
    print("Windows don't support yet")
    sys_exit(666)

print("""
    VIM updater version: {updater_version}
    OS: {os_type}
    Git status: {git_status}
""".format(updater_version=UPDATER_VER,
           os_type=OS_TYPE,
           git_status=GIT_STATUS))

if str(GIT_STATUS).count("git version") != 1:
    print("git not found")
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + UPDATER_DIR):
    print("work folder and updater dir here, check vim src folder")
    # fixme
    if path.exists(USER_FOLDER + UPDATER_DIR):
        print("vim folder here")
        print(check_current_vim_version_in_system())
        print("cd vim & output vim version in system & start pull")
        print("pulling")
        git_action("pull", USER_FOLDER + UPDATER_DIR)
        print(check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))

    else:
        git_action("clone", VIM_REPO, USER_FOLDER + UPDATER_DIR)
        print(check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR + VIM_FOLDER))

elif path.isdir(USER_FOLDER) and not path.exists(USER_FOLDER + UPDATER_DIR):
    print("can't find work folder")
    print("try to create updater dir")
    try:
        mkdir(USER_FOLDER + UPDATER_DIR)
        print("Directory {user_folder}{updater_dir} successfully created".format(user_folder=USER_FOLDER,
                                                                                 updater_dir=UPDATER_DIR))
    except FileExistsError:
        print("Directory {user_folder}{updater_dir} already exists".format(user_folder=USER_FOLDER,
                                                                           updater_dir=UPDATER_DIR))
        sys_exit(1)

    print("start git clone")
    git_action("clone", VIM_REPO, USER_FOLDER + UPDATER_DIR)
    print(check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR + VIM_FOLDER))

else:
    print("error with user folder: {user_folder}".format(user_folder=USER_FOLDER))
    sys_exit(1)
