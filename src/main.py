from aqt import mw
from aqt.qt import QShortcut, QKeySequence, Qt
from aqt.gui_hooks import (
    main_window_did_init,
    reviewer_will_end,
    state_did_change,
)

from ..gui.searchbar import SearchBar

from .utils import (
    searchbar_open,
    searchbar_close,
    searchbar_next,
    searchbar_previous,
)

def setup_search_bar():
    sb = SearchBar(mw, mw)

    mw.searchBar = sb
    mw.mainLayout.addWidget(sb)

def setup_shortcut(shortcut_string: str, func):
    shortcut = QShortcut(QKeySequence(shortcut_string), mw)
    shortcut.activated.connect(func)

    mw.searchBar.add_shortcut(shortcut)

def setup_shortcuts(state, old_state):
    if state != 'review':
        return

    setup_shortcut(searchbar_open.value, mw.searchBar.make_show)
    setup_shortcut(searchbar_close.value, mw.searchBar.hide)
    setup_shortcut(searchbar_next.value, mw.searchBar.highlight_next)
    setup_shortcut(searchbar_previous.value, mw.searchBar.highlight_previous)

def teardown_shortcuts():
    mw.searchBar.hide()
    mw.searchBar.cleanup()

def init_main_window():
    main_window_did_init.append(setup_search_bar)
    state_did_change.append(setup_shortcuts)
    reviewer_will_end.append(teardown_shortcuts)
