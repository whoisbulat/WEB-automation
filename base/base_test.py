from pages.form_page import FormPage
from pages.table_page import TablePage

class BaseTest:

    def setup_method(self):
        self.form_page = FormPage(self.driver)
        self.table_page = TablePage(self.driver)
