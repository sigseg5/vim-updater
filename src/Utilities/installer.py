import getpass
from sys import exit as sys_exit
from subprocess import call
import subprocess


def make_action(*args):
    # TODO: add make check in system

    if len(args) == 2 and args[0] == "make":
        print("make disk clean")
        print(args[1])

        make_command = "make"
        clean_proc = call([make_command, "distclean"], cwd=args[1])
        make_proc = call([make_command], cwd=args[1])

    elif len(args) == 2 and args[0] == "install":

        print("make install")
        # TODO: add getpass
        sudo_pass = "123"
        install_command = "sudo make install"
        # _ = call(["sudo", "make", "install"], cwd=args[1])
        install_proc = subprocess.Popen(install_command, cwd=args[1], stdin=subprocess.PIPE)
        install_proc.communicate(sudo_pass)[0]

    else:
        print("args error")
        sys_exit(1)
