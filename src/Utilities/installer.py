import getpass
import subprocess
from sys import exit as sys_exit


def make_action(*args):
    # TODO: add make check in system

    if len(args) == 2 and args[0] == "make":
        print("make disk clean")
        print(args[1])

        make_command = "make"
        clean_proc = subprocess.call([make_command, "distclean"], cwd=args[1])
        make_proc = subprocess.call([make_command], cwd=args[1])

    # elif len(args) == 4 and args[0] == "sudo" \
    #         and args[1] == "make" \
    #         and args[2] == "install":
    #
    #     print("make install")
    #     # TODO: add getpass
    #     install_command = "sudo make install"
    #     install_proc = subprocess.Popen(install_command,
    #                                     shell=True,
    #                                     stdout=subprocess.PIPE,
    #                                     stderr=subprocess.STDOUT,
    #                                     cwd=args[3])

    else:
        print("args error")
        sys_exit(1)
