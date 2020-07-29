from aqt import QWidget

from ..searchbar_ui import Ui_SearchBar

class SearchBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.ui = Ui_SearchBar()
        self.ui.setupUi(self)

    def setupUi(self):
        pass
