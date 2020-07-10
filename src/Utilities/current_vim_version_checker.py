import subprocess
from os import path
from sys import exit as sys_exit


def check_current_vim_version_in_system():
    print("Current vim version in system:")
    command = "vim --version"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []

    for line in proc.stdout:
        if b"VIM - Vi IMproved" in line:
            stdout.append(line)
        if b"Included patches" in line:
            stdout.append(line)
    return "".join(map(bytes.decode, stdout))


def check_current_vim_version_in_src(path_to_vim_folder):
    complete_version = ""

    if not path.isdir(path_to_vim_folder):
        sys_exit(1)

    # check major and minor version
    major_and_minor_version = ""
    try:
        with open(path_to_vim_folder + "/Makefile", "r") as make_file:
            first_minor_in_text_flag = False
            for line in make_file:
                if not first_minor_in_text_flag:
                    if line.find("MAJOR") != -1:
                        major_and_minor_version += line.strip("MAJOR = \n")
                        major_and_minor_version += "."
                    if line.find("MINOR") != -1:
                        major_and_minor_version += line.strip("MINOR = ")
                        first_minor_in_text_flag = True
            complete_version += "VIM - Vi IMproved " + major_and_minor_version
    except FileNotFoundError:
        print("error")
        sys_exit(1)

    # check included patches
    included_patches = ""
    try:
        first_version_in_file_flag = False
        with open(path_to_vim_folder + "/src/version.c", "r") as src_version:
            for line in src_version:
                if line.find("static int included_patches[]") != -1:
                    first_version_in_file_flag = True
                if first_version_in_file_flag:
                    if line.find(",") != -1:
                        first_version_in_file_flag = False
                        included_patches += line
        complete_version += "Included patches: " + included_patches.strip().strip(",")
    except FileNotFoundError:
        print("error")
        sys_exit(1)
    return complete_version
