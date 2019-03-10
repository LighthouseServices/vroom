#!/usr/bin/env python
from selenium.webdriver.common.by import By

import Driver
from pages.base_page import BasePage
from pages.buy.payment_page import PaymentPage


class BuyPage(BasePage):
    def __init__(self):
        super(BuyPage, self).__init__()

        self.title = "Sell Your Used Car to Vroom"

    @staticmethod
    def get_start_purchase():
        return Driver.Instance.find_element(
            By.CSS_SELECTOR, "a[href*=payment")

    def click_start_purchase(self):
        self.get_start_purchase().click()

        return PaymentPage()
