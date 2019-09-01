import subprocess


def check_git_on_device():
    command = "git --version"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout = []

    while True:
        outputLine = proc.stdout.readline()
        stdout.append(outputLine)

        if outputLine == b'' and proc.poll() is not None:
            break

    return "".join(map(bytes.decode, stdout))
