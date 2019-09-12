import getpass
import subprocess
from sys import exit as sys_exit


def make_action(*args):
    # TODO: add make check in system

    if len(args) == 2 and args[0] == "make":
        print("just make")
        command = "make"
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=args[1])

    elif len(args) == 4 and args[0] == "sudo" and args[1] == "make" and args[2] == "install":
        print("make install")
        command = "sudo make install"
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=args[3])

    else:
        print("args error")
        sys_exit(1)



    # try:
    #     passw = getpass.getpass(prompt='Password: ', stream=stderr)
    # except getpass.GetPassWarning:
    #     print("echo")
    # print(passw)

