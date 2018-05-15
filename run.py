import subprocess, shlex
from subprocess import CompletedProcess, Popen


def bash_c(command_line: str):
    # p = Popen(['bash','-c',command_line],stdout=subprocess.PIPE)

    CP = subprocess.run(['bash', '-c', command_line], stdout=subprocess.PIPE)
    buffer = CP.stdout.decode('utf-8')

    return buffer
