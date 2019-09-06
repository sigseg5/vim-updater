from sys import exit as sys_exit
import subprocess
# can only clone and pull from github repo


def consoleOutputParse(console_command, repo):
    command = "git {cmd} {repo}".format(cmd=console_command,
                                        repo=repo)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in proc.stdout:
        print("".join(map(bytes.decode, line)))
    pass


def git_action(command):
    VIM_REPO = "https://github.com/vim/vim.git"
    if command == "clone":
        print("clone")
        print(consoleOutputParse(command, VIM_REPO))
    elif command == "pull":
        print("pull")
        print(consoleOutputParse(command))
    else:
        print("command error")
        sys_exit(1)
