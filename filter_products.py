from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FilterProduct():
    def __init__(self, container_element:WebDriver):
        self.container_element = container_element
        self.products = self.pull_products()


    def pull_products(self):
        return self.container_element.find_elements(By.CLASS_NAME,'text-center col-4')

    def pull_name(self):
        for i in self.products:
            product_name = i.find_elements(By.CLASS_NAME, 'font-weight-bold top-space-10').__getattribute__('innerHTMl').strip()
            print(product_name)