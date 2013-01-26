from fabric.api import local,run

def test():
    return "test"

def uname():
    result=local("uname -a",capture=True)
    return result.stdout

def run_command(cmd):
    result=local(cmd,capture=True)
    return result.stdout

def run_remote_command(cmd):
    result=run(cmd)
    return result.stdout
