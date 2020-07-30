from aqt import mw, QObject, QShortcut, QKeySequence, Qt
from aqt.gui_hooks import main_window_did_init

from .gui.custom.searchbar import SearchBar

def setup_search_bar_mw():
    sb = SearchBar(mw, mw)

    mw.searchBar = sb
    mw.mainLayout.addWidget(sb)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), mw)
    shortcut.activated.connect(sb.make_show)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Escape), mw)
    shortcut.activated.connect(sb.hide)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_G), mw)
    shortcut.activated.connect(sb.highlight_next)

    shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_G), mw)
    shortcut.activated.connect(sb.highlight_prev)

def init_main_window():
    main_window_did_init.append(setup_search_bar_mw)
