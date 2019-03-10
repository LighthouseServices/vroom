#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utils import generate_phone_number

import Driver
from Utils import select_list_by_value, select_list_by_index
from pages.base_page import BasePage


class CreditFinancialInformationPage(BasePage):
    def __init__(self):
        super(CreditFinancialInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.loan_length_choices = self.loan_length_choices_xpath
        self.trade_in_choices = self.yes_no_choices_xpath

    # Selenium wrappers for all fields
    # DOWN_PAYMENT
    @staticmethod
    def get_down_payment_textfield():
        return Driver.Instance.find_element(By.NAME, "downPayment")

    def set_down_payment_textfield(self, down_payment_str="4000"):
        self.get_down_payment_textfield().send_keys(down_payment_str)

    # LOAN_LENGTH CHOICES
    def get_loan_length_choice_tab(self, loan_length_choice):
        loan_lengths_xpath = '//*[@id="container-page"]/div/div/main/div[4]/div[2]/section/form/div[1]/div[1]/div/' + \
                          self.loan_length_choices[loan_length_choice]
        return Driver.Instance.find_element(By.XPATH, loan_lengths_xpath)

    def click_loan_length_choice_tab(self, loan_length_choice="48"):
        self.get_loan_length_choice_tab(loan_length_choice).click()
        
    # TRADE_IN CHOICES
    def get_trade_in_choice_tab(self, trade_in_choice):
        trade_ins_xpath = '//*[@id="container-page"]/div/div/main/div[4]/div[2]/section/form/div[3]/div/div/' + \
                          self.trade_in_choices[trade_in_choice]
        return Driver.Instance.find_element(By.XPATH, trade_ins_xpath)

    def click_trade_in_choice_tab(self, trade_in_choice="No"):
        self.get_trade_in_choice_tab(trade_in_choice).click()

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return BasePage()

    @staticmethod
    def get_review_button(self):
        Driver.Instance.find_element(By.XPATH, "//*[contains(@class, 'btn btn-primary finish-section-btn disabled')]")

