from aqt import mw, QObject, QShortcut, QKeySequence, Qt
from aqt.gui_hooks import main_window_did_init, editor_did_init, editor_did_init_shortcuts
from aqt.utils import showText

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

main_window_did_init.append(setup_search_bar_mw)

from aqt.browser import Browser

def search_bar_shortcuts(cuts, editor):
    sb = SearchBar(mw, editor)

    editor.searchBar = sb
    editor.outerLayout.addWidget(sb)

    cuts.extend([
        ('Ctrl+Alt+Shift+F' if isinstance(editor.parentWindow, Browser) else 'Ctrl+F', editor.searchBar.make_show, True),
        ('Ctrl+Escape', editor.searchBar.hide, True),
        ('Ctrl+G', editor.searchBar.highlight_next, True),
        ('Ctrl+Shift+G', editor.searchBar.highlight_prev, True),
    ])

editor_did_init_shortcuts.append(search_bar_shortcuts)
