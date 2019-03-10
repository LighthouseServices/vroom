#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.sell.sell_review_page import SellReview


class VehicleHistoryPage(BasePage):
    def __init__(self):
        super(VehicleHistoryPage, self).__init__()

        self.title = "Complete Your Appraisal"
        self.accident_choices = {
            "Yes": "div[1]",
            "No": "div[2]",
            "Not Sure": "div[3]"
        }
        self.title_types = {
            "Clean": "div[1]/label/h2",
            "Lemon": "div[2]/label/h2",
            "Rebuilt Salvage": "div[3]/label/h2"
        }

    # Selenium wrappers for all field
    # ACCIDENT CHOICES
    def get_accident_choice_tab(self, accident_choice):
        accidents_xpath = '//*[@id="container-page"]/div/main/div[3]/div[2]/section/form/div[1]/div[1]/label/div[1]/' + \
                          self.accident_choices[accident_choice]
        return Driver.Instance.find_element(By.XPATH, accidents_xpath)

    def click_accident_choice_tab(self, yes_no_notsure="No"):
        self.get_accident_choice_tab(yes_no_notsure).click()

    # OPTIONS
    def get_title_type_checkbox(self, title_type):
        title_type_xpath = '//*[@id="container-page"]/div/main/div[3]/div[2]/section/form/div[1]/div[2]/div/' + \
                           self.title_types[title_type]
        return Driver.Instance.find_element(By.XPATH, title_type_xpath)

    def check_title_type_checkbox(self, title_type="Clean"):
        self.get_title_type_checkbox(title_type).click()

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        # THIS IS A BUG
        return SellReview()
