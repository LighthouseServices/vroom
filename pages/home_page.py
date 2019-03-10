#!/usr/bin/env python

import time

from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.search_results import SearchResultsPage
from pages.sell.sell_page import SellPage


class HomePage(BasePage):
    def __init__(self):
        self.title = "Vroom: Buy, Sell or Trade-In Used Vehicles Online"
        self.go_to_url()

    @staticmethod
    def go_to_url():
        Driver.Instance.get("https://vroom.com")

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

        # Business Function(s)

    def search(self, search_str):
        self.set_search_textfield(search_str)
        self.click_search_button()

        # TODO: waitUntil page is rendered
        time.sleep(1)

        return SearchResultsPage()

    def sell_trade(self):
        self.header_click_sell_trade()

        # TODO: waitUntil page is rendered
        time.sleep(1)

        return SellPage()
