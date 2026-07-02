import json
import os
import subprocess
from tkinter import Tk, filedialog

APP_FILE = "memory/apps.json"


def load_apps():
    if not os.path.exists(APP_FILE):
        return {}

    with open(APP_FILE, "r") as file:
        return json.load(file)


def save_apps(apps):
    with open(APP_FILE, "w") as file:
        json.dump(apps, file, indent=4)


def remember_app(app_name):

    root = Tk()
    root.withdraw()

    path = filedialog.askopenfilename(
        title=f"Select {app_name}.exe",
        filetypes=[("Executable Files", "*.exe")]
    )

    if not path:
        return False

    apps = load_apps()

    apps[app_name.lower()] = path

    save_apps(apps)

    return True


def get_app_path(app_name):

    apps = load_apps()

    return apps.get(app_name.lower())


def open_app(app_name):

    path = get_app_path(app_name)

    if path:

        subprocess.Popen(path)

        return True

    return False


def remove_app(app_name):

    apps = load_apps()

    if app_name.lower() in apps:

        del apps[app_name.lower()]

        save_apps(apps)

        return True

    return False


def list_apps():

    return load_apps()