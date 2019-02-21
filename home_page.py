#!/usr/bin/env python
import Driver
from selenium.webdriver.common.by import By
import time

class HomePage:
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

class SearchResultsPage:
    def __init__(self):
        self.title = "Buy Low-Mileage Used Cars & Trucks Online - Vroom"

    @staticmethod
    def get_cars_list():
        return Driver.Instance.find_element(By.XPATH, "//*[@id='cars-section']/ul")

    def get_all_cars(self):
        car_list_section = self.get_cars_list()
        cars_list = car_list_section.find_elements(By.CSS_SELECTOR, "a[href*=inventory]")

        return cars_list
