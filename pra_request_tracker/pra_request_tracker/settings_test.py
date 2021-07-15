from pra_request_tracker.settings import *  # noqa: F403


MEDIA_ROOT = APPS_DIR / "media"  # noqa: F405
del DEFAULT_FILE_STORAGE  # noqa: F821
