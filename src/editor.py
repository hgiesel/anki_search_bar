from aqt import mw
from aqt.qt import QObject, QShortcut, QKeySequence, Qt
from aqt.gui_hooks import editor_did_init, editor_did_init_shortcuts
from aqt.browser import Browser

from ..gui.searchbar import SearchBar

from .utils import (
    searchbar_open,
    searchbar_open_browser,
    searchbar_close,
    searchbar_next,
    searchbar_previous,
)


def setup_search_bar_editor(cuts, editor):
    sb = SearchBar(mw, editor)

    editor.searchBar = sb
    editor.outerLayout.addWidget(sb)

    cuts.extend([
        (searchbar_open_browser.value if isinstance(editor.parentWindow, Browser) else searchbar_open.value, editor.searchBar.make_show, True),
        (searchbar_close.value, editor.searchBar.hide, True),
        (searchbar_next.value, editor.searchBar.highlight_next, True),
        (searchbar_previous.value, editor.searchBar.highlight_prev, True),
    ])

def init_editor():
    editor_did_init_shortcuts.append(setup_search_bar_editor)
