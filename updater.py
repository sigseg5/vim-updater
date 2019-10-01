#!/usr/bin/env python3

import argparse
from sys import exit as sys_exit
# TODO: remove import
from sys import argv
from os import path
from os import mkdir
from shutil import rmtree

from src.Utilities.os_checker import check_os
from src.Utilities.git_downloader_from_internet import openBrowser
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_system
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_src
from src.Utilities.git_utilities import git_action
from src.Utilities.git_utilities import check_git_on_device
from src.Utilities.installer import make_action
from src.Utilities.installer import check_make_status

UPDATER_VER = "1.1"

parser = argparse.ArgumentParser()
# TODO: add version output
parser.add_argument("-f", "--fm", help="Force `make` and `make install`", action="store_true")
parser.add_argument("-c", "--clean", help="Clean updater folder", action="store_true")
parser.add_argument("-v", "--version", action="version", version="vim updater {}".format(UPDATER_VER))
args = parser.parse_args()

# if len(args) == 0:
#     print("zero")
#     pass
#     sys_exit(0)
# if args.fm:
#     print("force make")
#     sys_exit(1)
# elif args.clean:
#     print("clean")
#     sys_exit(0)
# else:
#     print("exit")
#     sys_exit(1)

sys_exit(1)


OS_TYPE = check_os()
USER_FOLDER = path.expanduser("~")
UPDATER_DIR = "/.vim_updater"
VIM_FOLDER = "/vim"

GIT_DOWNLOAD_PAGE = "http://git-scm.com/"
VIM_DOWNLOAD_PAGE = "https://www.vim.org/download.php#pc"
VIM_REPO = "https://github.com/vim/vim.git"

if OS_TYPE == "win":
    print("Windows don't fully supported yet")
    print("Please download vim here: {}".format(VIM_DOWNLOAD_PAGE))
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

isMakeInstalled = check_make_status()

# Args parsing
# if len(argv) == 1:
#     pass
# elif len(argv) == 2 and str(argv[1]) == "--fm" and isMakeInstalled:
#     # FIXME: fix `make: *** No rule to make target `distclean'.  Stop.` then updater dir don't exists. Call sys_exit
#     print("Force build and install vim")
#     make_action("make", USER_FOLDER + UPDATER_DIR)
#     make_action("install", USER_FOLDER + UPDATER_DIR)
#     sys_exit(0)
# elif len(argv) == 2 and str(argv[1]) == "--clean" and isMakeInstalled:
#     print("Removing work folder")
#     rmtree(USER_FOLDER + UPDATER_DIR)
#     print("Work folder remover successfully, please run updater again")
#     sys_exit(0)
# else:
#     print("Supported args: '-fm'")
#     print("Something wrong\nTry run script without args")
#     sys_exit(1)

try:
    GIT_STATUS = check_git_on_device()
except FileNotFoundError:
    print("git not installed")
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

if str(GIT_STATUS).count("git version") != 1:
    print("git not found")
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

if not isMakeInstalled and OS_TYPE == "mac":
    print("""
    make not found in system
    Download Xcode from AppStore and run "xcode-select --install" in terminal
    Or run "brew install make" if you have Homebrew installed
    """)
    sys_exit(0)
elif not isMakeInstalled:
    print("Unknown error with make")
    sys_exit(1)

print("""
    VIM updater version: {updater_version}
    OS: {os_type}
    Git status: {git_status}
""".format(updater_version=UPDATER_VER,
           os_type=OS_TYPE,
           git_status=GIT_STATUS))

if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + UPDATER_DIR):
    print("Work folder and updater dir here, check vim src folder")
    if path.exists(USER_FOLDER + UPDATER_DIR):
        print("VIM folder here")
        if not path.exists(USER_FOLDER + UPDATER_DIR + "/.git"):
            print("Can't find .git folder")
            print("Removing work folder")
            rmtree(USER_FOLDER + UPDATER_DIR)
            print("Work folder remover successfully, please run updater again")
            sys_exit(0)

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
        print("Starting git clone")
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
