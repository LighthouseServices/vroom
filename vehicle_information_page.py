#!/usr/bin/env python

from selenium.webdriver.common.by import By
import time
import Driver
from search_results import SearchResultsPage

class VehicleInformationPage:
    def __init__(self):
        self.title = "Complete Your Appraisal"

    # Selenium wrappers for all fields on the HomePage
    @staticmethod
    def get_search_textfield():
        return Driver.Instance.find_element(By.CSS_SELECTOR, "#hero-search-input")

    @staticmethod
    def get_search_button():
        return Driver.Instance.find_element(By.CSS_SELECTOR, "#marquee > div > form > span > button")

    # Selenium methods for setting fields
    def set_search_textfield(self, search_str):
        self.get_search_textfield().send_keys(search_str)

    def click_search_button(self):
        return self.get_search_button().click()
