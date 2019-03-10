#!/usr/bin/env python
import Driver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.sell.vehicle_information_page import VehicleInformationPage


class SellPage:
    def __init__(self):
        super(SellPage, self).__init__()

        self.title = "Sell Your Used Car to Vroom"

    @staticmethod
    def get_whats_my_car_worth():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=vehicleinformation")

    def click_whats_my_car_worth(self):
        self.get_whats_my_car_worth().click()

        return VehicleInformationPage()
