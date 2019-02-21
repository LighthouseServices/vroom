#!/usr/bin/env python

from selenium import webdriver

Instance = None

def Initialize():
    global Instance
    Instance = webdriver.Chrome()
    Instance.implicitly_wait(5)
    return Instance

def CloseDriver():
    global Instance
    Instance.quit()
