#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
from Utils import generate_email, generate_name, generate_phone_number, generate_birth_date
from pages.base_page import BasePage
from pages.buy.credit_application.credit_residential_information_page import CreditResidentialInformationPage



class CreditPersonalInformationPage(BasePage):
    def __init__(self):
        super(CreditPersonalInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

    # Selenium wrappers for all fields
    # FIRST_NAME
    @staticmethod
    def get_first_name_textfield():
        return Driver.Instance.find_element(By.NAME, "firstName")

    def set_first_name_textfield(self, first_name_str="buyCreditFirstName"):
        self.get_first_name_textfield().send_keys(generate_name(name=first_name_str))

    # LAST_NAME
    @staticmethod
    def get_last_name_textfield():
        return Driver.Instance.find_element(By.NAME, "lastName")

    def set_last_name_textfield(self, last_name_str="buyCreditLastName"):
        self.get_last_name_textfield().send_keys(generate_name(name=last_name_str))

    # EMAIL
    @staticmethod
    def get_email_textfield():
        return Driver.Instance.find_element(By.NAME, "email")

    def set_email_textfield(self, address="vroomqa-buy-credit"):
        self.get_email_textfield().send_keys(generate_email(address=address))

    @staticmethod
    def get_phone_number_textfield():
        return Driver.Instance.find_element(By.NAME, "phoneNumber")

    def set_phone_number_textfield(self):
        self.get_phone_number_textfield().send_keys(generate_phone_number())

    # BIRTH_DATE
    @staticmethod
    def get_birth_date_textfield():
        return Driver.Instance.find_element(By.NAME, "birthday")

    def set_birth_date_textfield(self):
        self.get_birth_date_textfield().send_keys(generate_birth_date())

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return CreditResidentialInformationPage()
