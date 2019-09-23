import getpass
from sys import exit as sys_exit
from subprocess import call
from subprocess import check_output


def check_make_status():
    make_check_proc = check_output(["make", "--version"])
    if (make_check_proc.decode('utf-8')).count("GNU Make") == 1:
        return True
    else:
        return False


def make_action(*args):
    if len(args) == 2 and args[0] == "make":
        print("make disk clean")
        print(args[1])

        make_command = "make"
        clean_proc = call([make_command, "distclean"], cwd=args[1])
        make_proc = call([make_command], cwd=args[1])

    elif len(args) == 2 and args[0] == "install":

        print("make install")
        # TODO: add wrong pass checker
        sudo_pass = getpass.getpass()
        install_command = "sudo make install"
        install_proc = check_output("echo {} | sudo -S {}".format(sudo_pass, install_command), shell=True, cwd=args[1])
        if install_proc.decode('utf-8').count("Sorry, try again.") >= 1:
            pass

    else:
        print("args error")
        sys_exit(1)
