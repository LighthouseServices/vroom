#!/usr/bin/env python
from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.sell.exterior_condition_page import ExteriorConditionPage
from pages.sell.interior_condition_page import InteriorConditionPage
from pages.sell.mechanical_condition_page import MechanicalConditionPage
from pages.sell.personal_information_page import PersonalInformationPage


class SellReview(BasePage):
    def __init__(self):
        super(SellReview, self).__init__()

        self.title = "Sell Your Used Car to Vroom"

    @staticmethod
    def get_edit_interior_condition():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=interiorcondition")

    def edit_interior_condition(self):
        self.get_edit_interior_condition().click()

        return InteriorConditionPage()

    @staticmethod
    def get_edit_exterior_condition():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=exteriorcondition")

    def edit_exterior_condition(self):
        self.get_edit_exterior_condition().click()

        return ExteriorConditionPage()

    @staticmethod
    def get_edit_mechanical_condition():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=mechanicalcondition")

    def edit_mechanical_condition(self):
        self.get_edit_mechanical_condition().click()

        return MechanicalConditionPage()

    @staticmethod
    def get_edit_personal_information():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=personalinformation")

    def edit_personal_information(self):
        self.get_edit_personal_information().click()

        return PersonalInformationPage()
