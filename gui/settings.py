from aqt import QDialog, QLayout, QKeySequence

from .forms.settings_ui import Ui_Settings

class Settings(QDialog):
    def __init__(self, mw, callback):
        super().__init__(parent=mw)

        self.mw = mw

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.cb = callback

        self.layout().setSizeConstraint(QLayout.SetFixedSize)

    def setupUi(
        self,
        open: str,
        open_browser: str,
        close: str,
        next: str,
        previous: str,
    ):
        self.ui.shortcutOpen.setKeySequence(QKeySequence(open))
        self.ui.shortcutOpenBrowser.setKeySequence(QKeySequence(open_browser))
        self.ui.shortcutClose.setKeySequence(QKeySequence(close))
        self.ui.shortcutNext.setKeySequence(QKeySequence(next))
        self.ui.shortcutPrevious.setKeySequence(QKeySequence(previous))

    def accept(self):
        open_shortcut = self.ui.shortcutOpen.keySequence().toString()
        open_browser_shortcut = self.ui.shortcutOpenBrowser.keySequence().toString()
        close_shortcut = self.ui.shortcutClose.keySequence().toString()
        next_shortcut = self.ui.shortcutNext.keySequence().toString()
        previous_shortcut = self.ui.shortcutPrevious.keySequence().toString()

        self.cb(
            open_shortcut,
            open_browser_shortcut,
            close_shortcut,
            next_shortcut,
            previous_shortcut,
        )
        super().accept()
