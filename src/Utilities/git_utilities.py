from sys import exit as sys_exit
import subprocess

# can only clone and pull from github repo

def consoleOutputParse(console_command):
    command = "vim --version"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []

    for line in proc.stdout:
        if b"VIM - Vi IMproved" in line:
            stdout.append(line)
        if b"Included patches" in line:
            stdout.append(line)
    return "".join(map(bytes.decode, stdout))

def git_action(command):
    VIM_REPO = "https://github.com/vim/vim.git"
    if command == "clone":
        print("clone")
    elif command == "pull":
        print("pull")
    else:
        print("command error")
        sys_exit(1)
