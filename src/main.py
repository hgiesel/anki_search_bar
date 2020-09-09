from aqt import mw
from aqt.qt import QShortcut, QKeySequence, Qt
from aqt.gui_hooks import (
    main_window_did_init,
    profile_did_open,
    profile_will_close,
    reviewer_will_end,
)

from ..gui.searchbar import SearchBar

from .utils import (
    searchbar_open,
    searchbar_close,
    searchbar_next,
    searchbar_previous,
)


def open_if_in_reviewer():
    if mw.state == 'review':
        mw.searchBar.make_show()

def setup_search_bar():
    sb = SearchBar(mw, mw)

    mw.searchBar = sb
    mw.mainLayout.addWidget(sb)

def setup_shortcut(shortcut_string: str, func):
    shortcut = QShortcut(QKeySequence(shortcut_string), mw)
    shortcut.activated.connect(func)

    mw.searchBar.add_shortcut(shortcut)

def setup_shortcuts():
    setup_shortcut(searchbar_open.value, open_if_in_reviewer)
    setup_shortcut(searchbar_close.value, mw.searchBar.hide)
    setup_shortcut(searchbar_next.value, mw.searchBar.highlight_next)
    setup_shortcut(searchbar_previous.value, mw.searchBar.highlight_previous)

def close_search_bar():
    mw.searchBar.hide()

def teardown_shortcuts():
    mw.searchBar.cleanup()

def init_main_window():
    main_window_did_init.append(setup_search_bar)
    profile_did_open.append(setup_shortcuts)
    reviewer_will_end.append(close_search_bar)
    profile_will_close.append(teardown_shortcuts)
