from core.intent import detect
from skills.apps import execute as app_skill
from skills.browser import execute as browser_skill
from skills.search import execute as search_skill
from skills.media import execute as media_skill
from skills.system import execute as system_skill


def process(command):

    intent = detect(command)

    print(f"[BRAIN] Intent -> {intent}")

    if app_skill(command):
        return True

    if browser_skill(command):
        return True

    if search_skill(command):
        return True

    if media_skill(command):
        return True

    if system_skill(command):
        return True

    return False