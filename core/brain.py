from skills.scan import execute as scan_skill
from skills.profile import execute as profile_skill

from core.parser import parse

from skills.apps import execute as app_skill
from skills.browser import execute as browser_skill
from skills.search import execute as search_skill
from skills.media import execute as media_skill
from skills.system import execute as system_skill


def process(command):

    data = parse(command)

    print(data)

    # ===========================
    # Scan Skill
    # ===========================
    if scan_skill(command):
        return True

    # ===========================
    # Profile Skill
    # ===========================
    if profile_skill(command):
        return True

    # ===========================
    # App Skill
    # ===========================
    if app_skill(command):
        return True

    # ===========================
    # Browser Skill
    # ===========================
    if browser_skill(command):
        return True

    # ===========================
    # Search Skill
    # ===========================
    if search_skill(command):
        return True

    # ===========================
    # Media Skill
    # ===========================
    if media_skill(command):
        return True

    # ===========================
    # System Skill
    # ===========================
    if system_skill(command):
        return True

    return False