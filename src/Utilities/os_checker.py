from sys import platform


def check_os():
    if platform.startswith("linux"):
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "win"
    else:
        return "other"
