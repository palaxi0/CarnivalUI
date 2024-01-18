
from CarnivalUI.UI.Utils.Base import WebDriverSetup
from CarnivalUI.UI.Pages.carnival_home_page import CarnivalHomePage


class TestCarnival(WebDriverSetup):

    def test_search_bahamas_sixnine(self):
        driver = self.driver
        self.driver.get(CarnivalHomePage.getBaseUrl())
        c_page = CarnivalHomePage(driver)
        c_page.select_destination()
        c_page.select_duration()
        c_page.clic_search_btn()

