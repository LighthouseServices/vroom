#!/usr/bin/env python

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Driver
from Utils import select_list_by_value, select_list_by_index
from search_results import SearchResultsPage

class VehicleInformationPage:
    def __init__(self):
        self.title = "Complete Your Appraisal"
        self.available_options = {
            "Sunroof": "li[1]/div/label/h2",
            "Navigation": "li[2]/div/label/h2",
            "Heated Seats": "li[3]/div/label/h2",
            "Alloy Wheels": "li[4]/div/label/h2",
            "Bluetooth": "li[5]/div/label/h2",
            "Other": "li[6]/div/label/h2",
        }

    @staticmethod
    def go_to_url():
        Driver.Instance.get("https://www.vroom.com/sell/vehicleinformation")

    # Selenium wrappers for all fields
    # Required Fields

    # VIN
    @staticmethod
    def get_vin_textfield():
        return Driver.Instance.find_element(By.NAME, "vin")
    def set_vin_textfield(self, vin_str="1FDAF56F03EB97783"):
        self.get_vin_textfield().send_keys(vin_str)

    # TRIM
    @staticmethod
    def get_trim_list():
        return Select(Driver.Instance.find_element(By.NAME, "trim"))
    # Selenium methods for setting fields
    def select_trim_by_value(self, trim="F550 Regular Cab"):
        select_list_by_value(self.get_trim_list(), trim)
    def select_trim_by_index(self, index=1):
        select_list_by_index(self.get_trim_list(), index)

    # MILEAGE
    @staticmethod
    def get_mileage_textfield():
        return Driver.Instance.find_element(By.NAME, "mileage")
    def set_mileage_textfield(self, mileage_str="40001"):
        self.get_mileage_textfield().send_keys(mileage_str)

    # EXTERIOR COLOR
    @staticmethod
    def get_exterior_color_list():
        return Select(Driver.Instance.find_element(By.NAME, "exteriorColor"))
    # Selenium methods for setting fields
    def select_exterior_color_by_value(self, trim="Blue"):
        self.get_exterior_color_list().select_by_visible_text(trim)
    def select_exterior_color_by_index(self, index="2"):
        self.get_exterior_color_list().select_by_value(index)

    # NUMBER OF KEYS
    @staticmethod
    def get_onekey_tab():
        return Driver.Instance.find_element(
            By.XPATH, '//*[@id="container-page"]/div/main/div[2]/div[2]/section/form/div[1]/div[2]/div[2]/label/div[1]/div[1]')
    def click_onekey_tab(self):
        self.get_onekey_tab().click()
    @staticmethod
    def get_twokeys_tab():
        return Driver.Instance.find_element(
            By.XPATH, '//*[@id="container-page"]/div/main/div[2]/div[2]/section/form/div[1]/div[2]/div[2]/label/div/div[2]')
    def click_twokeys_tab(self):
        self.get_twokeys_tab().click()

    # OPTIONS
    def get_options_checkbox(self, option_name):
        options_xpath = '//*[@id="container-page"]/div/main/div[2]/div[2]/section/form/div[1]/div[2]/div[3]/div/ul/' + self.available_options[option_name]
        return Driver.Instance.find_element(By.XPATH, options_xpath)

    def check_options_checkbox(self, option_name="Sunroof"):
        self.get_options_checkbox(option_name).click()

    def check_all_options_checkboxes(self):
        for option_name in self.available_options.keys():
            self.check_options_checkbox(option_name)






