from aqt import mw


class ProfileSetting:
    def __init__(self, keyword: str, default: str):
        self.keyword = keyword
        self.default = default

    @property
    def value(self):
        return mw.pm.profile.get(self.keyword, self.default)

    @value.setter
    def value(self, new_value: str):
        mw.pm.profile[self.keyword] = new_value

searchbar_open = ProfileSetting('searchBarOpen', 'Ctrl+F')
searchbar_open_browser = ProfileSetting('searchBarOpenBrowser', 'Ctrl+Alt+Shift+F')
searchbar_close = ProfileSetting('searchBarClose', 'Ctrl+Escape')
searchbar_next = ProfileSetting('searchBarNext', 'Ctrl+G')
searchbar_previous = ProfileSetting('searchBarPrevious', 'Ctrl+Shift+G')
