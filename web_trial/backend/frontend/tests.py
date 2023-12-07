from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from States.data import *
from time import sleep  
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
        print("Browser")
        self.driver.get(url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                    EC.url_matches(
                        url))
        except PageNotFoundError as err:
            if err.code == 404:
                print(
        "Error: Page not found")
        sleep(10)
        
    def navbar(self, num_cycles=10):
        nav_items_xpath_list = [
            property_xpath,
            details_xpath,
            contact_xpath,
        ]

        for i in range(num_cycles):
            for nav_xpath in nav_items_xpath_list + list(reversed(nav_items_xpath_list)):
                try:
                    WDW(
                        self.driver,
                        timeout=10).until(
                            EC.presence_of_element_located((
                                By.XPATH, nav_xpath
                            )))
                    nav_item = self.driver.find_element(
                        By.XPATH, nav_xpath)
                    nav_item.click()
                    print(f'{nav_xpath} clicked')
                except NoSuchElementException as err:
                    print(err)

    def closeBrowser(self):
        self.driver.implicitly_wait(5)
        self.driver.close()

if __name__ == '__main__' :
    func = webDriver()
    func.startDriver()
    func.Browser()
    func.navbar()
    func.closeBrowser()