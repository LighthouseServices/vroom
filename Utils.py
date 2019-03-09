#!/usr/bin/env python

import sys
from selenium import webdriver

Instance = None

def select_list_by_value(select_list, value):
    select_list.select_by_visible_text(value)

def select_list_by_index(select_list, index):
    try:
        select_list.select_by_visible_text(select_list.options[index].text)
    except IndexError:
        print("ERROR: Option #: {} does not exist!".format(index))
        sys.exit(1)

