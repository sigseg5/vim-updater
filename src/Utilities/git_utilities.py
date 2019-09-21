from sys import exit as sys_exit
from subprocess import call
from subprocess import check_output


def check_git_on_device():
    proc = check_output(["git", "--version"])
    return proc.decode()


def git_action(*args):
    if len(args) == 2 and args[0] == "pull":
        pull_proc_out = check_output(["git", args[0]], cwd=args[1])
        if (pull_proc_out.decode('utf-8')).count("Already up to date.") == 1:
            return True

    elif len(args) == 3 and args[0] == "clone":
        print("git clone {repo} {path}".format(repo=args[1], path=args[2]))
        _ = call(["git", args[0], args[1], args[2]])

    else:
        print("Trouble with args")
        sys_exit(1)
    pass
