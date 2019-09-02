import subprocess
from os import path
from sys import exit as sys_exit


def check_current_vim_version_in_system():
    print("current vim version in system")
    command = "vim --version"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []

    for line in proc.stdout:
        if b"VIM - Vi IMproved" in line:
            stdout.append(line)
        if b"Included patches" in line:
            stdout.append(line)
    return "".join(map(bytes.decode, stdout))


def check_current_vim_version_in_src_folder(path_to_vim_folder):
    print("current vim version in src folder")
    # TODO: add 'not' to statement
    # if path.isdir(path_to_vim_folder):
    if not path.isdir(path_to_vim_folder):
        sys_exit(1)
    with open(path_to_vim_folder + "/src/version.c", "r") as src_version:
        last_patch_flag = False
        additional_line_count = 0
        for line in src_version:
            if "static int included_patches[]" in line:
                last_patch_flag = True
            if last_patch_flag:
                additional_line_count = 2
