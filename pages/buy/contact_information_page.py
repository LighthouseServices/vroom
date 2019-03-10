#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
from Utils import generate_str, generate_email, generate_name, generate_phone_number
from pages.base_page import BasePage
from pages.buy.credit_application.credit_residential_information_page import CreditResidentialInformationPage


class ContactInformationPage(BasePage):
    def __init__(self):
        super(ContactInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.trade_in_choices = self.yes_no_choices_xpath

        self.session_id = generate_str()

    # Selenium wrappers for all fields
    # FIRST_NAME
    @staticmethod
    def get_first_name_textfield():
        return Driver.Instance.find_element(By.NAME, "firstName")

    def set_first_name_textfield(self, first_name_str="buyFirstName"):
        self.get_first_name_textfield().send_keys(generate_name(name=first_name_str, unique_id=self.session_id))

    # LAST_NAME
    @staticmethod
    def get_last_name_textfield():
        return Driver.Instance.find_element(By.NAME, "lastName")

    def set_last_name_textfield(self, last_name_str="buyLastName"):
        self.get_last_name_textfield().send_keys(generate_name(name=last_name_str, unique_id=self.session_id))

    # EMAIL
    @staticmethod
    def get_email_textfield():
        return Driver.Instance.find_element(By.NAME, "email")

    def set_email_textfield(self, address="vroomqa-buy"):
        self.get_email_textfield().send_keys(generate_email(address=address, unique_id=self.session_id))

    # PHONE_NUMBER
    @staticmethod
    def get_phone_number_textfield():
        return Driver.Instance.find_element(By.NAME, "phoneNumber")

    def set_phone_number_textfield(self):
        self.get_phone_number_textfield().send_keys(generate_phone_number())

    # TRADE_IN CHOICES
    def get_trade_in_choice_tab(self, trade_in_choice):
        trade_ins_xpath = '//*[@id="container-page"]/div/div/main/form/div[2]/div/' + \
                          self.trade_in_choices[trade_in_choice]
        return Driver.Instance.find_element(By.XPATH, trade_ins_xpath)

    def click_trade_in_choice_tab(self, trade_in_choice="No"):
        self.get_trade_in_choice_tab(trade_in_choice).click()

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return BasePage()
