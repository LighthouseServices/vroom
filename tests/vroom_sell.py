#!/usr/bin/env python

import unittest

import Driver
# from pages.home_page import HomePage
from pages.sell.vehicle_information_page import VehicleInformationPage


class VROOM_SELL(unittest.TestCase):
    def setUp(self):
        Driver.Initialize()

    def test_vroom_sell(self):
        # sell_page = HomePage().sell_trade()
        # vehicle_info = sell_page.click_whats_my_car_worth()
        # self.assertEqual(vehicle_info.title, Driver.Instance.title)

        vehicle_info = VehicleInformationPage()
        vehicle_info.go_to_url()
        vehicle_info.set_vin_textfield()
        vehicle_info.select_trim_by_index()
        vehicle_info.set_mileage_textfield()
        vehicle_info.select_exterior_color_by_value()
        vehicle_info.click_keys_tab()
        vehicle_info.check_all_options_checkboxes()
        vehicle_history = vehicle_info.continue_button()

        vehicle_history.click_accident_choice_tab()
        vehicle_history.check_title_type_checkbox()
        sell_review = vehicle_history.continue_button()

        # Potential BUG: Navigates to the Sell Review page and does not automatically navigate to the next step
        interior_condition = sell_review.edit_interior_condition()
        # Potential BUG: END

        interior_condition.check_interior_condition_checkbox()
        interior_condition.click_seat_choice_tab()
        interior_condition.click_smoked_in_choice_tab()
        sell_review = interior_condition.continue_button()

        exterior_condition = sell_review.edit_exterior_condition()
        exterior_condition.check_exterior_condition_checkbox()
        exterior_condition.click_hail_damage_choice_tab()
        exterior_condition.check_mileage_on_tires_checkbox()
        exterior_condition.check_all_aftermarket_modifications_checkboxes()
        sell_review = exterior_condition.continue_button()

        mechanical_condition = sell_review.edit_mechanical_condition()
        mechanical_condition.click_vehicle_run_choice_tab()
        mechanical_condition.check_mechanical_condition_checkbox()
        mechanical_condition.click_active_warning_light_choice_tab()
        mechanical_condition.click_flood_or_fire_damage_choice_tab()
        mechanical_condition.set_anything_else_textfield()
        sell_review = mechanical_condition.continue_button()

        personal_information = sell_review.edit_personal_information()
        personal_information.set_first_name_textfield()
        personal_information.set_last_name_textfield()
        personal_information.set_email_textfield()
        personal_information.set_phone_number_textfield()
        personal_information.set_zip_code_textfield()
        personal_information.select_sell_timing_by_index()
        personal_information.set_expected_offer_textfield()

    def tearDown(self):
        Driver.Instance.close()


if __name__ == '__main__':
    unittest.main()
