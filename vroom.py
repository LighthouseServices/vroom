#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import Driver


class Testing(unittest.TestCase):
    def setUp(self):
        Driver.Initialize()
        Driver.Instance.get("http://www.python.org")

    def test_vroom_search(self):
        assert "Python" in Driver.Instance.title
        elem = Driver.Instance.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in Driver.Instance.page_source

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def tearDown(self):
        Driver.Instance.close()

if __name__ == '__main__':
    unittest.main()
