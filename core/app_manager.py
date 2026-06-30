import json
import os

APP_FILE = "data/apps.json"


def load_apps():
    if not os.path.exists(APP_FILE):
        return {}

    with open(APP_FILE, "r") as file:
        return json.load(file)


def save_apps(apps):
    with open(APP_FILE, "w") as file:
        json.dump(apps, file, indent=4)


def add_app(name, path):

    apps = load_apps()

    apps[name.lower()] = path

    save_apps(apps)


def get_app(name):

    apps = load_apps()

    return apps.get(name.lower())