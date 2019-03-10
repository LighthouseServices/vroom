#!/usr/bin/env python

import unittest

import requests

import Driver
from pages.home_page import HomePage


class VROOM(unittest.TestCase):
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
    def test_vroom_homepage_search_results(self):
        search_results_page = HomePage().search("bmw")
        self.assertEqual(search_results_page.title, Driver.Instance.title)

        cars_list = search_results_page.get_all_cars()
        for car in cars_list:
            print("car={}\n".format(car.text))

        self.assertEqual(25, len(cars_list))

    def a_test_api_request(self):
        r = requests.get(url='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
        print("status={}".format(r.status_code))
        print("response={}".format(r.json()))

    def tearDown(self):
        Driver.Instance.close()


if __name__ == '__main__':
    unittest.main()
