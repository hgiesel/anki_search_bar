



from aqt.gui_hooks import editor_did_init
from aqt.utils import showText

from .gui.custom.searchbar import SearchBar

def setup_search_bar(editor):
    pass
    sb = SearchBar

def foo(editor):
    showText('hi')

editor_did_init.append(foo)
