from sys import exit as sys_exit
import subprocess


# can only clone and pull from github repo


def git_action(*args):
    """
    :param args: git command: clone or pull
    If command == pull: you need pass command and repo link to args
    Else pass only command, without repo link
    :return:
    """

    if len(args) == 2 and args[0] == "pull":
        print("git pull")
        command = "git {cmd}".format(cmd=args[0])
        # reset_command = "git reset --hard"

        # rest_proc = subprocess.Popen(reset_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=args[1])

        # print(rest_proc.stdout.read(350).strip().decode("utf-8"))

        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=args[1])

        print(proc.stdout.read(350).strip().decode("utf-8"))

    elif len(args) == 3 and args[0] == "clone":
        print("git clone {repo} {path}".format(repo=args[1], path=args[2]))
        _ = subprocess.call(["git", args[0], args[1], args[2]])

    else:
        print("trouble with args")
        sys_exit(1)

    pass
