import getpass
from sys import exit as sys_exit
from subprocess import call


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
        # TODO: specify getpass by OS type
        sudo_pass = getpass.getpass("Please enter your password: ")
        install_command = "sudo make install"
        install_proc = call("echo {} | sudo -S {}".format(sudo_pass, install_command), shell=True, cwd=args[1])

    else:
        print("args error")
        sys_exit(1)
