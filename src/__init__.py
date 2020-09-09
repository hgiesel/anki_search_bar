from .editor import init_editor
from .main import init_main_window
from .addon_manager import init_addon_manager

def init():
    init_editor()
    init_main_window()
    init_addon_manager()
