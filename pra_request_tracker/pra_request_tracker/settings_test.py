from pra_request_tracker.settings import *  # noqa: F403


MEDIA_ROOT = APPS_DIR / "media"  # noqa: F405
if "DEFAULT_FILE_STORAGE" in globals():
    del DEFAULT_FILE_STORAGE  # noqa: F821
