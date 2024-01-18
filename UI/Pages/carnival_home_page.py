import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.carnival.com/'


class CarnivalHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_btn = '//button[@class="cdc-filters-search-cta"]' #class
        self.title = 'logo' #data-testid
        self.sail_to_dd = 'cdc-destinations' #id
        self.bahamas = '//button[contains(text(), "The Bahamas")]'  #xpath
        self.sail_duration_dd = 'cdc-durations' #id
        self.six_to_nine_days = '//button[contains(text(), "6 - 9 Days")]' #xpath

    def select_destination(self):
        sail_to_dd = self.driver.find_element(By.ID,  self.sail_to_dd)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sail_to_dd)
        sail_to_dd.click()
        destination = self.driver.find_element(By.XPATH, self.bahamas)
        destination.click()

    def select_duration(self):
        sail_duration = self.driver.find_element(By.ID,  self.sail_duration_dd)
        sail_duration.scrollIntoView(block="start")
        sail_duration.click()
        self.driver.find_element(By.XPATH, self.six_to_nine_days).click()

    def clic_search_btn(self):
        search_btn = self.driver.find_element(By.XPATH, self.search_btn)
        search_btn.click()

    @staticmethod
    def getBaseUrl():
        return base_url
