from sys import exit as sys_exit
import subprocess
# can only clone and pull from github repo


def consoleOutputParse(*args):
    """
    :param args: git command: clone or pull
    If command == pull: you need pass command and repo link to args
    Else pass only command, without repo link
    :return:
    """

    if len(args) == 1 and args[0] == "pull":
        print("git pull")
        command = "git {cmd}".format(cmd=args[0])
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for line in proc.stdout:
            print("".join(map(bytes.decode, line)))

    elif len(args) == 2 and args[0] == "clone":
        print("git clone {repo}".format(repo=args[1]))
        command = "git {cmd} {repo}".format(cmd=args[0], repo=args[1])
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for line in proc.stdout:
            print("".join(map(bytes.decode, line)))
    else:
        print("trouble with args")
        sys_exit(1)

    pass


def git_action(command):
    # VIM_REPO = "https://github.com/vim/vim.git"
    VIM_REPO = "https://github.com/kirillNK/webpack-template.git"
    if command == "clone":
        print("clone")
        # TODO: add progress output
        print(consoleOutputParse(command, VIM_REPO))
    elif command == "pull":
        print("pull")
        print(consoleOutputParse(command, VIM_REPO))
    else:
        print("command error")
        sys_exit(1)
