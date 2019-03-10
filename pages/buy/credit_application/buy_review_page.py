#!/usr/bin/env python
from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.buy.credit_application.credit_income_information_page import CreditIncomeInformationPage
from pages.buy.credit_application.credit_financial_information_page import CreditFinancialInformationPage



class BuyReviewPage(BasePage):
    def __init__(self):
        super(BuyReviewPage, self).__init__()

        self.title = "Sell Your Used Car to Vroom"

    @staticmethod
    def get_edit_income_information():
        return Driver.Instance.find_elements(By.CSS_SELECTOR, "a[href*=credit")[2]

    def edit_income_information(self):
        self.get_edit_income_information().click()

        return CreditIncomeInformationPage()

    @staticmethod
    def get_edit_financial_information():
        return Driver.Instance.find_elements(By.CSS_SELECTOR, "a[href*=credit")[3]

    def edit_financial_information(self):
        self.get_edit_financial_information().click()

        return CreditFinancialInformationPage()
