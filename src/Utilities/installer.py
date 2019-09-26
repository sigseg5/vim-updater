import getpass
from sys import exit as sys_exit
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError
wrong_pass_count = 0


def passInput(args):
    sudo_pass = getpass.getpass()
    install_command = "sudo make install"
    try:
        install_proc = call("echo {} | sudo -S {}".format(sudo_pass, install_command), shell=True, cwd=args[1])
    except CalledProcessError:
        print("\nWrong password\nRun updater again with '-fm argument'")
        sys_exit(1)
        

def check_make_status():
    make_check_proc = check_output(["make", "--version"])
    if (make_check_proc.decode('utf-8')).count("GNU Make") == 1:
        return True
    else:
        return False


def make_action(*args):
    if len(args) == 2 and args[0] == "make":
        print("make disk clean")

        make_command = "make"
        clean_proc = call([make_command, "distclean"], cwd=args[1])
        make_proc = call([make_command], cwd=args[1])

    elif len(args) == 2 and args[0] == "install":

        print("make install")
        passInput(args)

    else:
        print("args error")
        sys_exit(1)
