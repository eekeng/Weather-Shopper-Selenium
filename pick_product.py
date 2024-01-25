from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from websiteshopper.filter_products import FilterProduct

class PickProduct():
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def pick_product_sunscreen(self):
        product_list = []

        container = self.driver.find_element(By.CLASS_NAME, 'container')
        container_elements = container.find_elements(By.CSS_SELECTOR, '*')

        report = FilterProduct(container_elements)
        report.pull_name()

        s50 = 'SPF-50'

        for i in container:
            if str(i.get_attribute('innerHTMl')) == 'Price':
                print(i.get_attribute('innerHTML'))

        print('sunscreen')
        print(product_list)
        print(len(container))

    def pick_product_moisturizer(self):
        print('moisturizer')