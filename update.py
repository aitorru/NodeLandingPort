import os
import subprocess
import sys

def updateDeps():
    print("Updating deps...")
    try:
        subprocess.check_call("npm update -g", shell=True)
    except subprocess.CalledProcessError:
        raise EnvironmentError("No se ha podido hacer update")

def updateGit():
    print("Updating repo...")
    try:
        sp = subprocess.check_call("git status --porcelain", shell=True, universal_newlines=True)
        if sp:
            subprocess.check_call("git reset --hard", shell=True)
        else:
            pass
        subprocess.check_call("git pull", shell=True)
    except subprocess.CalledProcessError:
        raise OSError("No se ha podido actualizar el repo")

updateDeps()
updateGit()
try:
    subprocess.check_call("npm run start", shell=True)
except:
    raise EnvironmentError("No se puede iniciar node...")