import getpass
from sys import exit as sys_exit
from subprocess import call
from subprocess import check_output


def pass_input(args):
    """
    Function to parse sudo pass and perform installation with superuser privileges
    :param args:
    :return:
    """
    sudo_pass = getpass.getpass()
    install_command = "sudo make install"
    _ = call("echo {} | sudo -S {}".format(sudo_pass, install_command), shell=True, cwd=args[1])


def check_make_installation_status():
    """
    Function that checks whether GNU Make is installed on the device
    :return: Boolean status
    """
    make_check_proc = check_output(["make", "--version"])
    if (make_check_proc.decode('utf-8')).count("GNU Make") == 1:
        return True
    else:
        return False


def make_action(*args):
    """
    Function to perform all GNU Make related actions (`make distclean` and `make install`)
    :param args: work with `make distclean` and `make install`
    :return:
    """
    if len(args) == 2 and args[0] == "make":
        print("make diskclean")

        make_command = "make"
        _ = call([make_command, "distclean"], cwd=args[1])
        _ = call([make_command], cwd=args[1])

    elif len(args) == 2 and args[0] == "install":
        print("Performing Make install")
        pass_input(args)

    else:
        print("Unexpected args error")
        sys_exit(1)
