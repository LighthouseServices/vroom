#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import Driver
from Utils import generate_address, generate_city, generate_zip_code, select_list_by_value, select_list_by_index
from pages.base_page import BasePage
from pages.buy.credit_application.buy_review_page import BuyReviewPage


class CreditResidentialInformationPage(BasePage):
    def __init__(self):
        super(CreditResidentialInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.own_rent_other_choices = self.own_rent_other_choices_xpath

    # Selenium wrappers for all fields
    # ADDRESS
    @staticmethod
    def get_address_textfield():
        return Driver.Instance.find_element(By.NAME, "address")

    def set_address_textfield(self, address_str="1375 Broadway"):
        self.get_address_textfield().send_keys(generate_address(address=address_str))

    # CITY
    @staticmethod
    def get_city_textfield():
        return Driver.Instance.find_element(By.NAME, "city")

    def set_city_textfield(self, city_str="New York"):
        self.get_city_textfield().send_keys(generate_city(city=city_str))
        
    # ZIP_CODE
    @staticmethod
    def get_zip_code_textfield():
        return Driver.Instance.find_element(By.NAME, "zipCode")

    def set_zip_code_textfield(self, zip_code_str="10018"):
        self.get_zip_code_textfield().send_keys(generate_zip_code(zip_code_str))
        
    # STATE
    @staticmethod
    def get_state_list():
        return Select(Driver.Instance.find_element(By.NAME, "state"))

    # Selenium methods for setting fields
    def select_state_by_value(self, state="NY"):
        select_list_by_value(self.get_state_list(), state)

    def select_state_by_index(self, index=3):
        select_list_by_index(self.get_state_list(), index)
        
        
    # OWN_RENT_OTHER CHOICES
    def get_own_rent_other_choice_tab(self, own_rent_other_choice):
        own_rent_others = '//*[@id="container-page"]/div/div/main/div[2]/div[2]/section/form/div[1]/div/label[5]/div[1]/' + \
                             self.own_rent_other_choices[own_rent_other_choice]
        return Driver.Instance.find_element(By.XPATH, own_rent_others)

    def click_own_rent_other_choice_tab(self, own_rent_other_choice="Own"):
        self.get_own_rent_other_choice_tab(own_rent_other_choice).click()

    # MONTHLY_PAYMENT
    @staticmethod
    def get_monthly_payment_textfield():
        return Driver.Instance.find_element(By.NAME, "monthlyPayment")

    def set_monthly_payment_textfield(self, monthly_payment_str="1000"):
        self.get_monthly_payment_textfield().send_keys(monthly_payment_str)
        
    # YEARS_AT_RESIDENCE
    @staticmethod
    def get_years_at_residence_textfield():
        return Driver.Instance.find_element(By.NAME, "residenceYearsLived")

    def set_years_at_residence_textfield(self, years_at_residence_str="10"):
        self.get_years_at_residence_textfield().send_keys(years_at_residence_str)

    # MONTHS_AT_RESIDENCE
    @staticmethod
    def get_months_at_residence_textfield():
        return Driver.Instance.find_element(By.NAME, "residenceMonthsLived")

    def set_months_at_residence_textfield(self, months_at_residence_str="5"):
        self.get_months_at_residence_textfield().send_keys(months_at_residence_str)

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return BuyReviewPage()
