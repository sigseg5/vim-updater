#!/usr/bin/env python3

import argparse
from sys import exit as sys_exit
from sys import argv
from os import path, mkdir, environ
from shutil import rmtree

from src.Utilities.os_checker import check_os
from src.Utilities.git_downloader_from_internet import open_browser
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_system
from src.Utilities.current_vim_version_checker import check_current_vim_version_in_src
from src.Utilities.git_utilities import git_action
from src.Utilities.git_utilities import check_git_on_device
from src.Utilities.installer import make_action
from src.Utilities.installer import check_make_installation_status

UPDATER_VER = "1.2.0"
GIT_DOWNLOAD_PAGE = "http://git-scm.com/"
VIM_DOWNLOAD_PAGE = "https://www.vim.org/download.php#pc"
VIM_REPO = "https://github.com/vim/vim.git"
USER_FOLDER = path.expanduser("~")
UPDATER_DIR = "/.vim_updater"
OS_TYPE = check_os()


def clean_install():
    """
    Function to perform clean installation of vim: `git clone` and `make install`
    :return:
    """
    print("Starting git clone, it may not be quite fast.")
    try:
        git_action("clone", VIM_REPO, USER_FOLDER + UPDATER_DIR)
    except Exception:
        print("Fatal error: unable for access.\nCheck internet connection.")
        sys_exit(1)

    print("Current vim version in src:\n" + check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))
    make_action("make", USER_FOLDER + UPDATER_DIR)
    make_action("install", USER_FOLDER + UPDATER_DIR)
    print("VIM updated to {}".format(check_current_vim_version_in_system()))


def main():
    if "SUDO_UID" in environ.keys():
        print("Please don't use this application with superuser privileges.")
        sys_exit(1)

    if OS_TYPE == "win":
        print("Windows is not supported yet.")
        print("Please download vim here: {}".format(VIM_DOWNLOAD_PAGE))
        open_browser(GIT_DOWNLOAD_PAGE)
        sys_exit(0)

    is_make_installed = check_make_installation_status()

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fm", help="Force `make` and `make install`", action="store_true")
    parser.add_argument("-c", "--clean", help="Clean updater folder", action="store_true")
    parser.add_argument("-v", "--version", action="version", version="vim updater {}".format(UPDATER_VER))
    args = parser.parse_args()

    if len(argv) == 1:
        pass
    elif args.fm and is_make_installed:
        print("Trying to force build and install vim…")
        make_action("make", USER_FOLDER + UPDATER_DIR)
        make_action("install", USER_FOLDER + UPDATER_DIR)
        sys_exit(0)
    elif args.clean:
        print("Removing work folder…")
        rmtree(USER_FOLDER + UPDATER_DIR)
        print("Work folder removed successfully, please run updater again.")
        sys_exit(0)
    else:
        print("Check supported args by `./updater [-h, --help]` command.")
        print("Something wrong\nTry run script without args.")

    try:
        git_version_output = check_git_on_device()
    except FileNotFoundError:
        print("git is not installed on the system.")
        open_browser(GIT_DOWNLOAD_PAGE)
        sys_exit(0)

    if str(git_version_output).count("git version") != 1:
        print("git is not found on the system.")
        open_browser(GIT_DOWNLOAD_PAGE)
        sys_exit(0)

    if not is_make_installed and OS_TYPE == "mac":
        print("""
        make not found in system
        Download Xcode from AppStore and run "xcode-select --install" in terminal.
        Or run "brew install make" if you have Homebrew installed.
        """)
        sys_exit(0)
    elif not is_make_installed:
        print("Unknown error with make")
        sys_exit(1)

    print("""
        VIM updater version: {updater_version}
        OS: {os_type}
        Git status: {git_status}
    """.format(updater_version=UPDATER_VER,
               os_type=OS_TYPE,
               git_status=git_version_output))

    if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + UPDATER_DIR):
        print("Work folder and updater dir here, checking vim src folder…")
        if path.exists(USER_FOLDER + UPDATER_DIR):
            if not path.exists(USER_FOLDER + UPDATER_DIR + "/.git"):
                print("Can't find .git folder.")
                print("Removing work folder…")
                rmtree(USER_FOLDER + UPDATER_DIR)
                print("Work folder remover successfully, please run updater again.")
                sys_exit(0)

            print("Pulling from github...")
            try:
                is_updated = git_action("pull", USER_FOLDER + UPDATER_DIR)
            except Exception:
                print("Fatal error: unable for access.\nCheck internet connection.")
                sys_exit(1)

            if is_updated:
                print("VIM already up to date.\n")
                print(check_current_vim_version_in_system())
                sys_exit(0)
            print(check_current_vim_version_in_src(USER_FOLDER + UPDATER_DIR))
            make_action("make", USER_FOLDER + UPDATER_DIR)
            make_action("install", USER_FOLDER + UPDATER_DIR)
            print("vim updated to {}.".format(check_current_vim_version_in_system()))

        else:
            clean_install()

    elif path.isdir(USER_FOLDER) and not path.exists(USER_FOLDER + UPDATER_DIR):
        print("Can't find work folder.")
        print("Trying to create updater directory…")
        try:
            mkdir(USER_FOLDER + UPDATER_DIR)
            print("Directory {user_folder}{updater_dir} successfully created.".format(user_folder=USER_FOLDER,
                                                                                     updater_dir=UPDATER_DIR))
        except FileExistsError:
            print("Directory {user_folder}{updater_dir} already exists.".format(user_folder=USER_FOLDER,
                                                                               updater_dir=UPDATER_DIR))
            sys_exit(1)

        clean_install()

    else:
        print("Error with user folder: {user_folder}.".format(user_folder=USER_FOLDER))
        sys_exit(1)


if __name__ == '__main__':
    main()
