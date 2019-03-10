#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
import pages.sell.sell_review_page as sell_review
from pages.base_page import BasePage


class ExteriorConditionPage(BasePage):
    def __init__(self):
        super(ExteriorConditionPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.exterior_condition = {
            "Above Average": "div[1]/label/h2",
            "Average": "div[2]/label/h2",
            "Below Average": "div[3]/label/h2"
        }

        self.hail_damage_choices = {
            "Yes": "div[1]",
            "No": "div[2]",
            "Not Sure": "div[3]"
        }

        self.mileage_on_tires = {
            "Under 5k": "div[1]/label/h2",
            "10k-20k": "div[2]/label/h2",
            "More than 30k": "div[3]/label/h2",
            "5k-10k": "div[4]/label/h2",
            "20k-30k": "div[5]/label/h2"
        }

        self.aftermarket_modifications = {
            "Stereo System": "div[1]/label/h2",
            "Exhaust": "div[2]/label/h2",
            "Performance": "div[3]/label/h2",
            "Wheels and tires": "div[4]/label/h2",  # BUG
            "Suspension": "div[5]/label/h2",
            "Other": "div[6]/label/h2"
        }

    # selenium wrappers for all field
    # EXTERIOR CONDITION
    def get_exterior_condition_checkbox(self, exterior_condition_type):
        exterior_condition_xpath = '//*[@id="container-page"]/div/main/div[5]/div[2]/section/form/div[1]/div[1]/' + \
                                   self.exterior_condition[exterior_condition_type]
        return Driver.Instance.find_element(By.XPATH, exterior_condition_xpath)

    def check_exterior_condition_checkbox(self, exterior_condition_type="Below Average"):
        self.get_exterior_condition_checkbox(exterior_condition_type).click()

    # HAIL_DAMAGE CHOICES
    def get_hail_damage_choice_tab(self, hail_damage_choice):
        hail_damages_xpath = '//*[@id="container-page"]/div/main/div[5]/div[2]/section/form/div[1]/div[2]/label/div/' + \
                             self.hail_damage_choices[hail_damage_choice]
        return Driver.Instance.find_element(By.XPATH, hail_damages_xpath)

    def click_hail_damage_choice_tab(self, hail_damage_choice="Not Sure"):
        self.get_hail_damage_choice_tab(hail_damage_choice).click()

    # MILES ON TIRES
    def get_mileage_on_tires_checkbox(self, mileage_on_tires):
        mileage_on_tires_xpath = '//*[@id="container-page"]/div/main/div[5]/div[2]/section/form/div[1]/div[3]/div/' + \
                                 self.mileage_on_tires[mileage_on_tires]
        return Driver.Instance.find_element(By.XPATH, mileage_on_tires_xpath)

    def check_mileage_on_tires_checkbox(self, mileage_on_tires="5k-10k"):
        self.get_mileage_on_tires_checkbox(mileage_on_tires).click()

    # AFTERMARKET MODIFICATIONS
    def get_aftermarket_modifications_checkbox(self, aftermarket_modifications_type):
        aftermarket_modifications_xpath = '//*[@id="container-page"]/div/main/div[5]/div[2]/section/form/div[1]/div[4]/div[2]/' + \
                                          self.aftermarket_modifications[aftermarket_modifications_type]
        return Driver.Instance.find_element(By.XPATH, aftermarket_modifications_xpath)

    def check_aftermarket_modifications_checkbox(self, aftermarket_modifications_type="Wheels and tires"):
        self.get_aftermarket_modifications_checkbox(aftermarket_modifications_type).click()

    def check_all_aftermarket_modifications_checkboxes(self):
        for aftermarket_modification_name in self.aftermarket_modifications.keys():
            self.check_aftermarket_modifications_checkbox(aftermarket_modification_name)

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return sell_review.SellReview()
