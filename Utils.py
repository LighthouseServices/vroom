#!/usr/bin/env python

import sys
from selenium import webdriver


def select_list_by_value(select_list, value):
    select_list.select_by_visible_text(value)


def select_list_by_index(select_list, index):
    try:
        select_list.select_by_visible_text(select_list.options[index].text)
    except IndexError:
        print("ERROR: Option #: {} does not exist!".format(index))
        sys.exit(1)

from random import choice
from string import ascii_uppercase
def generate_str(size=4):
    return ''.join(choice(ascii_uppercase) for i in list(range(size)))
