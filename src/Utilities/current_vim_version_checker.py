from os import system
import subprocess


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


def check_current_vim_version_in_src_folder():
    print("current vim version in src folder")
