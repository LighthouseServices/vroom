#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import Driver
from home_page import HomePage, header_click_sell_trade
from vehicle_information_page import VehicleInformationPage


import requests


class Testing(unittest.TestCase):
    def setUp(self):
        Driver.Initialize()

    # Basic Tests
    def a_test_vroom_homepage(self):
        self.assertEqual(HomePage().title, Driver.Instance.title)

    def a_test_vroom_homepage_search(self):
        self.assertEqual(HomePage().search("bmw").title, Driver.Instance.title)

    def a_test_vroom_homepage_header_sellpage(self):
        self.assertEqual(HomePage().sell_trade().title, Driver.Instance.title)

    # Functional Tests
    def a_test_vroom_homepage_search_results(self):
        search_results_page = HomePage().search("bmw")
        self.assertEqual(search_results_page.title, Driver.Instance.title)

        cars_list = search_results_page.get_all_cars()
        for car in cars_list:
            print("car={}\n".format(car.text))

        self.assertEqual(25, len(cars_list))

    def test_vroom_sell_whatsitworth(self):
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
        vehicle_history = vehicle_info.click_continue_button()
        time.sleep(5)

        vehicle_history.click_accident_choice_tab()
        vehicle_history.check_title_type_checkbox()
        sell_review = vehicle_history.click_continue_button()
        time.sleep(5)

        interior_condition = sell_review.edit_interior_condition()
        time.sleep(5)

        interior_condition.check_interior_condition_checkbox()
        interior_condition.click_seat_choice_tab()
        interior_condition.click_smoked_in_choice_tab()
        sell_review = interior_condition.click_continue_button()
        time.sleep(5)

        exterior_condition = sell_review.edit_exterior_condition()
        time.sleep(5)

        exterior_condition.check_exterior_condition_checkbox()
        exterior_condition.click_hail_damage_choice_tab()
        exterior_condition.check_mileage_on_tires_checkbox()
        exterior_condition.check_all_aftermarket_modifications_checkboxes()
        sell_review = exterior_condition.click_continue_button()
        time.sleep(5)

        mechanical_condition = sell_review.edit_mechanical_condition()
        mechanical_condition.click_vehicle_run_choice_tab()
        mechanical_condition.check_mechanical_condition_checkbox()
        mechanical_condition.click_active_warning_light_choice_tab()
        mechanical_condition.click_flood_or_fire_damage_choice_tab()
        mechanical_condition.set_anything_else_textfield()
        sell_review = mechanical_condition.click_continue_button()
        time.sleep(5)




    def a_test_api_request(self):
        r = requests.get(url='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
        print("status={}".format(r.status_code))
        print("response={}".format(r.json()))

    def tearDown(self):
        pass
        Driver.Instance.close()

if __name__ == '__main__':
    unittest.main()
