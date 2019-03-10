#!/usr/bin/env python

import sys


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


def generate_name(name, unique_id=None, use_name_only=False):
    if use_name_only:
        return name

    if unique_id is None:
        unique_id = generate_str()

    return "{}-AUTO-{}".format(name, unique_id)


def generate_email(address, host="test.com", unique_id=None, use_address_only=False):
    if use_address_only:
        return address

    if unique_id is None:
        unique_id = generate_str()

    return "{}+auto-{}@{}".format(address, unique_id, host)


def generate_phone_number(area_code="555", prefix="111", number="2222"):
    return "{}{}{}".format(area_code, prefix, number)
