import time

from base.base_test import BaseTest
from pages.form_page import FormPage


class TestModal(BaseTest):

    def test_open(self):
        self.form_page.open()
        self.form_page.click_block_btn()
        time.sleep(10)

