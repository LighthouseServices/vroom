#!/usr/bin/env python
from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.buy.contact_information_page import ContactInformationPage
from pages.buy.credit_application.credit_personal_information_page import CreditPersonalInformationPage


class PaymentPage(BasePage):
    def __init__(self):
        super(PaymentPage, self).__init__()

        self.title = "Sell Your Used Car to Vroom"

    @staticmethod
    def get_apply_now():
        return Driver.Instance.find_element(By.CSS_SELECTOR, "a[href*=credit")

    def click_apply_now(self):
        self.get_apply_now().click()

        return CreditPersonalInformationPage()

    @staticmethod
    def get_pay_cash():
        return Driver.Instance.find_elements(By.CSS_SELECTOR, "a[href*=cash-osf")[0]

    def click_pay_cash(self):
        self.get_pay_cash().click()

        return ContactInformationPage()

    @staticmethod
    def get_use_my_bank():
        # pay_cash also navigates to same href
        # selects use_my_bank [1]
        return Driver.Instance.find_elements(By.CSS_SELECTOR, "a[href*=cash-osf")[1]

    def click_use_my_bank(self):
        self.get_use_my_bank().click()

        return ContactInformationPage()
