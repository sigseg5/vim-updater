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
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=args[1])

        print(proc.stdout.read(350).strip())
        # for line in proc.stdout:
        # fixme: can't encode bytes
        # print(proc.stdout.read(150).strip())
        # print("".join(map(bytes.decode(), line)))
        # print(line.strip())

    elif len(args) == 3 and args[0] == "clone":
        print("git clone {repo} {path}".format(repo=args[1], path=args[2]))
        command = "git {cmd} {repo} {path}".format(cmd=args[0], repo=args[1], path=args[2])
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # for line in proc.stdout:
        #     # fixme: can't encode bytes
        #     print("".join(map(bytes.decode, line)))
        #     print(line.strip())
        print(proc.stdout.read(350).strip())
    else:
        print("trouble with args")
        sys_exit(1)

    pass
