from aqt import mw, QObject, QShortcut, QKeySequence, Qt
from aqt.gui_hooks import editor_did_init, editor_did_init_shortcuts
from aqt.browser import Browser

from ..gui.custom.searchbar import SearchBar

def setup_search_bar_editor(cuts, editor):
    sb = SearchBar(mw, editor)

    editor.searchBar = sb
    editor.outerLayout.addWidget(sb)

    cuts.extend([
        ('Ctrl+Alt+Shift+F' if isinstance(editor.parentWindow, Browser) else 'Ctrl+F', editor.searchBar.make_show, True),
        ('Ctrl+Escape', editor.searchBar.hide, True),
        ('Ctrl+G', editor.searchBar.highlight_next, True),
        ('Ctrl+Shift+G', editor.searchBar.highlight_prev, True),
    ])

def init_editor():
    editor_did_init_shortcuts.append(setup_search_bar_editor)
