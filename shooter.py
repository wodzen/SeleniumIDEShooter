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

  def execute_method_0(self, target):
    # 2 | setWindowSize | 1047x691 | 
    self.driver.set_window_size(1047, 691)
    # 3 | mouseOver | css=.gb_d | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".gb_d")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOut | css=.gb_d | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 5 | click | id=APjFqb | 
    self.driver.find_element(By.ID, "APjFqb").click()
    # 6 | type | id=APjFqb | where is the grand canyon?
    self.driver.find_element(By.ID, "APjFqb").send_keys("where is the grand canyon?")
    # 7 | mouseOver | css=.zp6Lyf:nth-child(2) .nPDzT:nth-child(5) > .GKS7s | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".zp6Lyf:nth-child(2) .nPDzT:nth-child(5) > .GKS7s")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | mouseOut | css=.zp6Lyf:nth-child(2) .nPDzT:nth-child(5) > .GKS7s | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 9 | mouseOver | id=tsuid_55 | 
    element = self.driver.find_element(By.ID, "tsuid_55")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | mouseOut | id=tsuid_55 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 11 | mouseOver | id=tsuid_55 | 
    element = self.driver.find_element(By.ID, "tsuid_55")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 12 | mouseOut | id=tsuid_55 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 13 | mouseOver | css=.gb_d | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".gb_d")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOut | css=.gb_d | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()

if __name__ == "__main__":
    TestTypesearch().shoot(["google.com"])