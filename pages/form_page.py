from selenium.webdriver.common.by import By

from base.base_page import BasePage


class FormPage(BasePage):

    _PAGE_URL = "https://aqa-proka4.org/sandbox/web"


    _BTN_BLOCK = (By.XPATH, "//a[@href='#drag-drop']")





    def click_block_btn(self):
        self.ui.click(self._BTN_BLOCK)





