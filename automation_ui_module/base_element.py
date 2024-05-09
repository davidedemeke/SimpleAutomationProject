import os
import time
import json

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, WebDriverException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from datetime import datetime


class BaseElement:
    """
    Base page class that is initialized on every page object class.
    The driver is a web automation tool which enables you to run
    Every page that inherited the BaseElement will be able to use the driver
    """

    def __init__(self, driver, delay=15, long_delay=240):
        self.name = self.__class__.__name__
        self.driver = driver
        self.wait = WebDriverWait(self.driver, delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])
        self.long_wait = WebDriverWait(self.driver, long_delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])

