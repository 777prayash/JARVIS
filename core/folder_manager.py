import json
import os
from tkinter import Tk, filedialog

FOLDER_FILE = "memory/folders.json"


def load_folders():

    if not os.path.exists(FOLDER_FILE):
        return {}

    with open(FOLDER_FILE, "r") as file:
        return json.load(file)


def save_folders(folders):

    with open(FOLDER_FILE, "w") as file:
        json.dump(folders, file, indent=4)


def remember_folder(folder_name):

    root = Tk()
    root.withdraw()

    path = filedialog.askdirectory(
        title=f"Select your {folder_name} folder"
    )

    root.destroy()

    if not path:
        return False

    folders = load_folders()

    folders[folder_name.lower()] = path

    save_folders(folders)

    return True


def get_folder(folder_name):

    folders = load_folders()

    return folders.get(folder_name.lower())


def list_folders():

    return load_folders()


def remove_folder(folder_name):

    folders = load_folders()

    if folder_name.lower() in folders:

        del folders[folder_name.lower()]

        save_folders(folders)

        return True

    return False