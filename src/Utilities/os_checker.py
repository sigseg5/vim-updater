from sys import platform


def check_os():
    # fixme: platform == "linux2" return true on macOS
    if platform == "linux":
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "win"
    else:
        return "other"
