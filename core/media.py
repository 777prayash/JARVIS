import os
import subprocess

VIDEO_EXTENSIONS = (
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".webm"
)

AUDIO_EXTENSIONS = (
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a"
)


def play_movie(media_name, vlc_path, folders):

    media_name = media_name.lower()

    for folder in folders:

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            for file in files:

                name = file.lower()

                if media_name in name:

                    if (
                        name.endswith(VIDEO_EXTENSIONS)
                        or
                        name.endswith(AUDIO_EXTENSIONS)
                    ):

                        subprocess.Popen([vlc_path, os.path.join(root, file)])

                        return True

    return False