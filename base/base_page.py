from helpers.ui_helper import UIHelper


class BasePage:
    def __init__(self, driver):
        self.ui = UIHelper(driver)
        self.api = ...

    def open(self):
        self.ui.open(self._PAGE_URL)

    def assert_opened(self):
        self.ui.assert_opened(self._PAGE_URL)




