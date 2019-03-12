#!/usr/bin/env python

import unittest
import time
import Driver
import selenium.webdriver.support.expected_conditions as exp_condition
from pages.home_page import HomePage


class VROOM_BUY(unittest.TestCase):
    def setUp(self):
        Driver.Initialize()

    # Functional Tests
    def test_vroom_buy_apply_now(self):
        search_results_page = HomePage().search("bmw")
        buy_page = search_results_page.select_a_car_by_index()
        payment_page = buy_page.click_start_purchase()
        credit_application = payment_page.click_apply_now()
        credit_application.set_first_name_textfield()
        credit_application.set_last_name_textfield()
        credit_application.set_email_textfield()
        credit_application.set_phone_number_textfield()
        credit_application.set_birth_date_textfield()
        residential_information = credit_application.continue_button()

        residential_information.set_address_textfield()
        residential_information.set_city_textfield()
        residential_information.select_state_by_value()
        residential_information.set_zip_code_textfield()
        residential_information.click_own_rent_other_choice_tab()
        residential_information.set_monthly_payment_textfield()
        residential_information.set_years_at_residence_textfield()
        residential_information.set_months_at_residence_textfield()
        buy_review = residential_information.continue_button()

        income_information = buy_review.edit_income_information()
        income_information.select_employment_status_by_index()
        income_information.set_employer_textfield()
        income_information.set_job_title_textfield()
        income_information.set_years_employed_textfield()
        income_information.set_months_employed_textfield()
        income_information.set_phone_number_textfield()
        income_information.set_gross_income_textfield()
        income_information.set_ssn_textfield()
        buy_review = income_information.continue_button()

        financial_information = buy_review.edit_financial_information()
        financial_information.set_down_payment_textfield()
        financial_information.click_loan_length_choice_tab()
        financial_information.click_trade_in_choice_tab()

        # self.assertEquals(True, exp_condition.element_to_be_clickable(financial_information.get_continue_locator()))

    def test_vroom_buy_pay_cash(self):
        search_results_page = HomePage().search("bmw")
        buy_page = search_results_page.select_a_car_by_index()
        payment_page = buy_page.click_start_purchase()

        # TODO: Must confirm this is hitting right button
        contact_information = payment_page.click_pay_cash()
        contact_information.set_first_name_textfield()
        contact_information.set_last_name_textfield()
        contact_information.set_email_textfield()
        contact_information.set_phone_number_textfield()
        contact_information.click_trade_in_choice_tab()

    def test_vroom_buy_use_my_bank(self):
        search_results_page = HomePage().search("audi")
        buy_page = search_results_page.select_a_car_by_index()
        payment_page = buy_page.click_start_purchase()

        contact_information = payment_page.click_use_my_bank()
        contact_information.set_first_name_textfield()
        contact_information.set_last_name_textfield()
        contact_information.set_email_textfield()
        contact_information.set_phone_number_textfield()
        contact_information.click_trade_in_choice_tab()

    def tearDown(self):
        Driver.Instance.quit()


if __name__ == '__main__':
    unittest.main()
