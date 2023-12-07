from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from States.data import property_xpath, details_xpath,contact_xpath
from selenium.webdriver.common.by import By 
from urllib.error import HTTPError as PageNotFoundError
from States.data import gecko_driver_path, url, property_url, home_xpath
from selenium import webdriver as web
import os

class webDriver:
    def __init__(self):
        self.driver = None

    def startDriver(self):
        print("start Driver")
        firefox_options = web.FirefoxOptions()
        os.environ[
            "webdriver.firefox.driver"
            ] =  gecko_driver_path
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()

    def Browser(self):
        try:
            self.driver.get(url)
            print("Browser")
        except PageNotFoundError as err:
            print(err)
            if err.code == 404:
                print("Error: Page not found")
            else:
                self.driver.get(url)

    def navbar(self):
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, property_xpath
            )))
            self.driver.find_element(By.XPATH, property_xpath).click()
            print('Properties clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
            self.driver.get(property_url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, details_xpath
            )))
            self.driver.find_element(
                By.XPATH, 
                details_xpath).click()
            print('Details clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, contact_xpath
            )))
            self.driver.find_element(By.XPATH, contact_xpath).click()
            print('Contact clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, details_xpath
            )))
            self.driver.find_element(
                By.XPATH, 
                details_xpath).click()
            print('Details clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, property_xpath
            )))
            self.driver.find_element(By.XPATH, property_xpath).click()
            print('Properties clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
            self.driver.get(property_url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH, home_xpath
            )))
            self.driver.find_element(By.XPATH, home_xpath).click()
            print('home clicked')
        except (NoSuchElementException, ElementNotInteractableException) as err:
            print(err)
            self.driver.get(property_url)
            
    def closeBrowser(self):
        self.driver.implicitly_wait(5)
        print('close clicked')
        self.driver.close()

if __name__ == '__main__':
    func = webDriver()
    counter = 10
    func.startDriver()
    func.Browser()
    for i in range(counter):
        counter+=1
        func.navbar()
    func.closeBrowser()