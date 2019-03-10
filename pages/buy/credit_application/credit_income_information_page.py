#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utils import generate_phone_number

import Driver
from Utils import select_list_by_value, select_list_by_index
from pages.base_page import BasePage
import pages.buy.credit_application.buy_review_page as buy_review_page


class CreditIncomeInformationPage(BasePage):
    def __init__(self):
        super(CreditIncomeInformationPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.own_rent_other_choices = self.own_rent_other_choices_xpath

    # Selenium wrappers for all fields
    # EMPLOYMENT_STATUS
    @staticmethod
    def get_employment_status_list():
        return Select(Driver.Instance.find_element(By.NAME, "employmentStatus"))

    def select_employment_status_by_value(self, employment_status="Self-Employed"):
        select_list_by_value(self.get_employment_status_list(), employment_status)

    def select_employment_status_by_index(self, index=3):
        select_list_by_index(self.get_employment_status_list(), index)

    # EMPLOYER
    @staticmethod
    def get_employer_textfield():
        return Driver.Instance.find_element(By.NAME, "employer")

    def set_employer_textfield(self, employer_str="Vroom"):
        self.get_employer_textfield().send_keys(employer_str)

    # JOB_TITLE
    @staticmethod
    def get_job_title_textfield():
        return Driver.Instance.find_element(By.NAME, "jobTitle")

    def set_job_title_textfield(self, job_title_str="SDET"):
        self.get_job_title_textfield().send_keys(job_title_str)

    # YEARS_EMPLOYED
    @staticmethod
    def get_years_employed_textfield():
        return Driver.Instance.find_element(By.NAME, "yearsEmployed")

    def set_years_employed_textfield(self, years_employed_str="12"):
        self.get_years_employed_textfield().send_keys(years_employed_str)

    # MONTHS_EMPLOYED
    @staticmethod
    def get_months_employed_textfield():
        return Driver.Instance.find_element(By.NAME, "monthsEmployed")

    def set_months_employed_textfield(self, months_employed_str="7"):
        self.get_months_employed_textfield().send_keys(months_employed_str)

    @staticmethod
    def get_phone_number_textfield():
        return Driver.Instance.find_element(By.NAME, "employerPhone")

    def set_phone_number_textfield(self):
        self.get_phone_number_textfield().send_keys(generate_phone_number())
        
    # GROSS_INCOME
    @staticmethod
    def get_gross_income_textfield():
        return Driver.Instance.find_element(By.NAME, "income")

    def set_gross_income_textfield(self, gross_income_str="68543"):
        self.get_gross_income_textfield().send_keys(gross_income_str)
        
    # SSN
    @staticmethod
    def get_ssn_textfield():
        return Driver.Instance.find_element(By.NAME, "ssn")

    def set_ssn_textfield(self, ssn_str="999999999"):
        self.get_ssn_textfield().send_keys(ssn_str)

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()

        return buy_review_page.BuyReviewPage()
