from sys import platform


def check_os():
    """
    Function to detect type of OS
    :return: String value of OS type
    """
    if platform.startswith("linux"):
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "win"
    else:
        return "other"
