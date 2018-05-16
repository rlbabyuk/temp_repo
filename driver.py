#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver


class Driver(object):
    instance = None

    def __new__(cls, base_url=None, browser='firefox'):

        if cls.instance is None:
            driver_odj = object.__new__(cls)
            cls.instance = driver_odj
            cls.base_url = base_url if base_url else "https://www.online-convert.com/"
            cls.browser = browser

            if browser == "firefox":
                # Create a new instance of the Firefox driver
                cls.driver = webdriver.Firefox()
            elif browser == "remote":
                # Create a new instance of the Chrome driver
                cls.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
        else:

            driver_odj = cls.instance

        return driver_odj
