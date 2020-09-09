from aqt import mw

from ..gui.settings import Settings

from .utils import (
    searchbar_open,
    searchbar_open_browser,
    searchbar_close,
    searchbar_next,
    searchbar_previous,
)


def set_settings(
    open_shortcut: str,
    open_browser_shortcut: str,
    close_shortcut: str,
    next_shortcut: str,
    previous_shortcut: str,
):
    searchbar_open.value = open_shortcut
    searchbar_open_browser.value = open_browser_shortcut
    searchbar_close.value = close_shortcut
    searchbar_next.value = next_shortcut
    searchbar_previous.value = previous_shortcut

def show_settings():
    dialog = Settings(mw, set_settings)
    dialog.setupUi(
        searchbar_open.value,
        searchbar_open_browser.value,
        searchbar_close.value,
        searchbar_next.value,
        searchbar_previous.value,
    )

    return dialog.exec_()

def init_addon_manager():
    mw.addonManager.setConfigAction(__name__, show_settings)
