import getpass


def make_action():
    print("make")
    try:
        passw = getpass.getpass(prompt='Password: ', stream=None)
    except getpass.GetPassWarning:
        print("echo")
    print(passw)


def make_install_action():
    print("make install")
