from aqt import mw
from aqt.qt import QShortcut, QKeySequence, Qt
from aqt.gui_hooks import main_window_did_init, state_did_reset, webview_will_set_content, reviewer_will_end

from ..gui.searchbar import SearchBar


def open_if_in_reviewer():
    if mw.state == 'review':
        mw.searchBar.make_show()

def setup_search_bar_mw():
    sb = SearchBar(mw, mw)

    mw.searchBar = sb
    mw.mainLayout.addWidget(sb)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), mw)
    shortcut.activated.connect(open_if_in_reviewer)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Escape), mw)
    shortcut.activated.connect(sb.hide)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_G), mw)
    shortcut.activated.connect(sb.highlight_next)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_G), mw)
    shortcut.activated.connect(sb.highlight_prev)

def close_search_bar():
    mw.searchBar.hide()

def init_main_window():
    main_window_did_init.append(setup_search_bar_mw)
    reviewer_will_end.append(close_search_bar)
