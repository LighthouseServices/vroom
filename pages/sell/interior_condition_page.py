#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
import pages.sell.sell_review_page as sell_review
from pages.base_page import BasePage


class InteriorConditionPage(BasePage):
    def __init__(self):
        super(InteriorConditionPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.interior_condition = {
            "Above Average": "div[1]/label/h2",
            "Average": "div[2]/label/h2",
            "Below Average": "div[3]/label/h2"
        }

        self.seat_choices = {
            "Leather": "div[1]",
            "Cloth": "div[2]",
            "Other": "div[3]"
        }

        self.smoked_in_choices = {
            "Yes": "div[1]",
            "No": "div[2]",
            "Not Sure": "div[3]"
        }

    # Selenium wrappers for all field
    # INTERIOR CONDITION
    def get_interior_condition_checkbox(self, interior_condition_type):
        interior_condition_xpath = '//*[@id="container-page"]/div/main/div[4]/div[2]/section/form/div[1]/div[1]/' + \
                                   self.interior_condition[interior_condition_type]
        return Driver.Instance.find_element(By.XPATH, interior_condition_xpath)

    def check_interior_condition_checkbox(self, interior_condition_type="Average"):
        self.get_interior_condition_checkbox(interior_condition_type).click()

    # SEAT CHOICES
    def get_seat_choice_tab(self, seat_choice):
        seats_xpath = '//*[@id="container-page"]/div/main/div[4]/div[2]/section/form/div[1]/div[2]/label[1]/div/' + \
                      self.seat_choices[seat_choice]
        return Driver.Instance.find_element(By.XPATH, seats_xpath)

    def click_seat_choice_tab(self, seat_choice="Cloth"):
        self.get_seat_choice_tab(seat_choice).click()

    # SMOKED IN CHOICES
    def get_smoked_in_choice_tab(self, smoked_in_choice):
        smoked_in_xpath = '//*[@id="container-page"]/div/main/div[4]/div[2]/section/form/div[1]/div[2]/label[2]/div/' + \
                          self.smoked_in_choices[smoked_in_choice]
        return Driver.Instance.find_element(By.XPATH, smoked_in_xpath)

    def click_smoked_in_choice_tab(self, smoked_in_choice="No"):
        self.get_smoked_in_choice_tab(smoked_in_choice).click()

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return sell_review.SellReview()
