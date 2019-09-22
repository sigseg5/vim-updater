#!/usr/bin/env python3

# TODO: add os.path.join

from sys import exit as sys_exit
from os import path
from os import mkdir

from src.Utilities.os_checker import check_os
from src.Utilities.git_downloader_from_internet import openBrowser
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_system
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_src
from src.Utilities.git_utilities import git_action
from src.Utilities.git_utilities import check_git_on_device
from src.Utilities.installer import make_action

UPDATER_VER = "0.1.1"
OS_TYPE = check_os()
GIT_DOWNLOAD_PAGE = "http://git-scm.com/"

try:
    GIT_STATUS = check_git_on_device()
except FileNotFoundError:
    print("git not installed")
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

USER_FOLDER = path.expanduser("~")
UPDATER_DIR = "/.vim_updater"
VIM_FOLDER = "/vim"

VIM_REPO = "https://github.com/vim/vim.git"

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

# FIXME: "fatal: not a git repository (or any of the parent directories): .git" then UPDATER_DIR only exist
if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + UPDATER_DIR):
    print("Work folder and updater dir here, check vim src folder")
    if path.exists(USER_FOLDER + UPDATER_DIR):
        print("VIM folder here")
        print("Pulling from github...")
        isUpdated = git_action("pull", USER_FOLDER + UPDATER_DIR)
        if isUpdated:
            print("VIM already up to date\n")
            print(check_current_vim_version_in_system())
            sys_exit(0)
        print(check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))
        make_action("make", USER_FOLDER + UPDATER_DIR)
        make_action("install", USER_FOLDER + UPDATER_DIR)
        print("VIM updated to {}".format(check_current_vim_version_in_system()))

    else:
        git_action("clone", VIM_REPO, USER_FOLDER + UPDATER_DIR)
        print("Current vim version in src\n" + check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))
        make_action("make", USER_FOLDER + UPDATER_DIR)
        make_action("install", USER_FOLDER + UPDATER_DIR)
        print("VIM updated to {}".format(check_current_vim_version_in_system()))

elif path.isdir(USER_FOLDER) and not path.exists(USER_FOLDER + UPDATER_DIR):
    print("Can't find work folder")
    print("Try to create updater dir")
    try:
        mkdir(USER_FOLDER + UPDATER_DIR)
        print("Directory {user_folder}{updater_dir} successfully created".format(user_folder=USER_FOLDER,
                                                                                 updater_dir=UPDATER_DIR))
    except FileExistsError:
        print("Directory {user_folder}{updater_dir} already exists".format(user_folder=USER_FOLDER,
                                                                           updater_dir=UPDATER_DIR))
        sys_exit(1)

    print("Starting git clone")
    git_action("clone", VIM_REPO, USER_FOLDER + UPDATER_DIR)
    print("Current vim version in src\n" + check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))
    make_action("make", USER_FOLDER + UPDATER_DIR)
    make_action("install", USER_FOLDER + UPDATER_DIR)
    print("VIM updated to {}".format(check_current_vim_version_in_system()))

else:
    print("Error with user folder: {user_folder}".format(user_folder=USER_FOLDER))
    sys_exit(1)
