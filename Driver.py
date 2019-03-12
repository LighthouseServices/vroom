#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

Instance = None

desired_cap = {
'os' : 'OS X',
'os_version' : 'Mojave',
'browser' : 'Chrome',
'browser_version' : '73.0 beta',
'browserstack.local' : 'false',
'browserstack.selenium_version' : '3.5.2',
'browserstack.debug' : True
}

def Initialize():
    global Instance
    Instance = webdriver.Remote(command_executor='http://ike18:oejsDmiqNkXK597Catp9@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

    # Local - Instance = webdriver.Chrome()
    Instance.implicitly_wait(5)
    return Instance


def CloseDriver():
    global Instance
    Instance.quit()
