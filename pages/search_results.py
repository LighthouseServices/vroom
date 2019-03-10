#!/usr/bin/env python
import Driver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.buy.buy_page import BuyPage


class SearchResultsPage(BasePage):
    def __init__(self):
        super(SearchResultsPage, self).__init__()

        self.title = "Buy Low-Mileage Used Cars & Trucks Online - Vroom"

    @staticmethod
    def get_cars_list():
        return Driver.Instance.find_element(By.XPATH, "//*[@id='cars-section']/ul")

    def get_all_cars(self):
        car_list_section = self.get_cars_list()
        cars_list = car_list_section.find_elements(By.CSS_SELECTOR, "a[href*=inventory]")

        return cars_list

    def select_a_car_by_index(self, index=0):
        self.get_all_cars()[index].click()

        return BuyPage()
