import json
import os

PROFILE_DIR = "profiles"


def load_profile(name):

    file_path = os.path.join(PROFILE_DIR, f"{name.lower()}.json")

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as f:
        return json.load(f)