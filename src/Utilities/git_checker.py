import subprocess


def check_git_on_device():
    proc = subprocess.check_output(["git", "--version"])
    return proc.decode()
