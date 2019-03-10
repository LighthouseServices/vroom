#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import Driver
from Utils import select_list_by_value, select_list_by_index, generate_phone_number, generate_email, generate_name
from pages.base_page import BasePage


class PersonalInformationPage(BasePage):
    def __init__(self):
        super(PersonalInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

    # Selenium wrappers for all fields
    # FIRST_NAME
    @staticmethod
    def get_first_name_textfield():
        return Driver.Instance.find_element(By.NAME, "firstName")

    def set_first_name_textfield(self, first_name_str="sellFirstName"):
        self.get_first_name_textfield().send_keys(generate_name(name=first_name_str))

    # LAST_NAME
    @staticmethod
    def get_last_name_textfield():
        return Driver.Instance.find_element(By.NAME, "lastName")

    def set_last_name_textfield(self, last_name_str="sellLastName"):
        self.get_last_name_textfield().send_keys(generate_name(name=last_name_str))

    # EMAIL
    @staticmethod
    def get_email_textfield():
        return Driver.Instance.find_element(By.NAME, "email")

    def set_email_textfield(self, email_str="vroomqa-sell"):
        self.get_email_textfield().send_keys(generate_email(address=email_str, unique_id=self.vin))


    # PHONE_NUMBER
    @staticmethod
    def get_phone_number_textfield():
        return Driver.Instance.find_element(By.NAME, "phoneNumber")

    def set_phone_number_textfield(self):
        self.get_phone_number_textfield().send_keys(generate_phone_number())

    # ZIP_CODE
    @staticmethod
    def get_zip_code_textfield():
        return Driver.Instance.find_element(By.NAME, "zipCode")

    def set_zip_code_textfield(self, zip_code_str="10018"):
        self.get_zip_code_textfield().send_keys(zip_code_str)

    # SELL_TIMING
    @staticmethod
    def get_sell_timing_list():
        return Select(Driver.Instance.find_element(By.NAME, "sellTiming"))

    # Selenium methods for setting fields
    def select_sell_timing_by_value(self, sell_timing):
        select_list_by_value(self.get_sell_timing_list(), sell_timing)

    def select_sell_timing_by_index(self, index=3):
        select_list_by_index(self.get_sell_timing_list(), index)

    # EXPECTED_OFFER
    @staticmethod
    def get_expected_offer_textfield():
        return Driver.Instance.find_element(By.NAME, "expectedOffer")

    def set_expected_offer_textfield(self, expected_offer_str="10000000"):
        self.get_expected_offer_textfield().send_keys(expected_offer_str)

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return BasePage()
