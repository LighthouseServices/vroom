#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver


class BasePage:
    def __init__(self):
        self.vin = "1FDAF56F03EB97783"

        # Buttons used for selection
        self.yes_no_choices_xpath = {
            "Yes": "div[1]",
            "No": "div[2]"
        }

        self.yes_no_notsure_choices_xpath = {
            "Yes": "div[1]",
            "No": "div[2]",
            "Not Sure": "div[3]"
        }

        self.own_rent_other_choices_xpath = {
            "Own": "div[1]",
            "Rent": "div[2]",
            "Other": "div[3]"
        }

        self.loan_length_choices_xpath = {
            "24": "div[1]",
            "36": "div[2]",
            "48": "div[3]",
            "60": "div[4]",
            "72": "div[5]"
        }

        # Checkboxes
        self.averages_xpath = {
            "Above Average": "div[1]/label/h2",
            "Average": "div[2]/label/h2",
            "Below Average": "div[3]/label/h2"
        }

    # CONTINUE
    @staticmethod
    def get_continue_button():
        return Driver.Instance.find_element(By.CLASS_NAME, "finish-section-btn-container")

    def click_continue_button(self):
        self.get_continue_button().click()

    def get_continue_locator(self):
        return By.XPATH, "//*[contains(@class, 'btn btn-primary finish-section-btn disabled')]"

    # Header Functions
    @staticmethod
    def header_get_sell_trade():
        return Driver.Instance.find_element(By.CSS_SELECTOR, "a[href*=sell]")

    def header_click_sell_trade(self):
        return self.header_get_sell_trade().click()

    def get_vin(self):
        return self.vin
