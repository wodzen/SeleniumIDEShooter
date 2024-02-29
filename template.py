
'''
This file dynamically calls
'''

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

class TestTypesearch():

       
  def shoot(self, targets):
    for target in targets:
        self.call_methods(target)

  def call_methods(self, target):
    i = 0
    while True:
        method_name = f'execute_function_{i}()'
        if hasattr(TestTypesearch, method_name):
            method = getattr(TestTypesearch, method_name)
            method(target)
            i += 1
        else:
            break
  
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  '''
  Dynamic action cases will be populated below as `execute_function_n`
  '''
