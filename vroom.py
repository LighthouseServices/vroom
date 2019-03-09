#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import Driver
from home_page import HomePage, header_click_sell_trade


import requests


class Testing(unittest.TestCase):
    def setUp(self):
        Driver.Initialize()

    def a_test_vroom_homepage(self):
        HomePage.go_to_url()
        self.assertEqual("Vroom: Buy, Sell or Trade-In Used Vehicles Online", Driver.Instance.title)

    def a_test_vroom_sellpage(self):
        HomePage.go_to_url()
        header_click_sell_trade()
        self.assertEqual("Sell Your Used Car to Vroom", Driver.Instance.title)

    def test_vroom_sell_whatsitworth(self):
        sell_page = HomePage().sell_trade()
        sell_page.click_whats_my_car_worth()
        self.assertEqual("Sell Your Used Car to Vroom", Driver.Instance.title)

    def a_test_vroom_homepage_search(self):
        search_results_page = HomePage().search("bmw")
        self.assertEqual(search_results_page.title, Driver.Instance.title)

        cars_list = search_results_page.get_all_cars()
        for car in cars_list:
            print("car={}\n".format(car.text))

        self.assertEqual(20, len(cars_list))

    def a_test_api_request(self):
        r = requests.get(url='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
        print("status={}".format(r.status_code))
        print("response={}".format(r.json()))

    def tearDown(self):
        Driver.Instance.close()

if __name__ == '__main__':
    unittest.main()
