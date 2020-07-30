from aqt import QWidget
from aqt.utils import showText

from ..searchbar_ui import Ui_SearchBar

class SearchBar(QWidget):
    def __init__(self, mw, parent):
        super().__init__(parent=mw)

        self.mw = mw
        self.parent = parent

        self.ui = Ui_SearchBar()
        self.ui.setupUi(self)

        self.setupUi()

    def setupUi(self):
        self.setVisible(False)

        self.ui.next.clicked.connect(self.highlight_next)
        self.ui.prev.clicked.connect(self.highlight_prev)
        self.ui.close.clicked.connect(self.hide)

    def make_show(self):
        self.setVisible(True)

        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.selectAll()

    def get_input(self):
        return self.ui.lineEdit.text()

    def highlight_next(self):
        cmd = f'window.find("{self.get_input()}", false /* case-sensitive */, false /* backwards */, true /* wrap */, false /* unimplemented */, true /* iframes */)'
        self.parent.web.eval(cmd)

    def highlight_prev(self):
        cmd = f'window.find("{self.get_input()}", false /* case-sensitive */, true /* backwards */, true /* wrap */, false /* unimplemented */, true /* iframes */)'
        self.parent.web.eval(cmd)
