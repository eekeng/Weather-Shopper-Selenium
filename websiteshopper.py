from selenium import webdriver
from selenium.webdriver.common.by import By
import websiteshopper.constants as const
import os
from bs4 import BeautifulSoup
from websiteshopper.pick_product import PickProduct

BASE_URL = 'https://weathershopper.pythonanywhere.com/'

class Shopper(webdriver.Chrome):
    def __init__(self, teardown = False):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.teardown = teardown
        # self.driver_path = driver_path
        # os.environ['PATH'] += self.driver_path
        super(Shopper,self).__init__(options=option)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_on_page(self):
        self.get(BASE_URL)

    def check_temp(self):
       temp = self.find_element(By.ID, 'temperature')

       buy_sunscreen = self.find_element(By.CSS_SELECTOR, '[class="text-center col-4 offset-4"]')
       buy_sunscreen_elements = buy_sunscreen.find_elements(By.CSS_SELECTOR, '*')

       buy_moisturizer = self.find_element(By.CSS_SELECTOR, '[class="text-center col-4"]')
       buy_moisturizer_elements = buy_moisturizer.find_elements(By.CSS_SELECTOR, '*')

       temp_2 = temp.get_attribute('innerHTML')

       soup = BeautifulSoup(temp_2, 'html.parser')
       global temp_final
       temp_final = ''.join(s for s in soup.stripped_strings if s.isdigit())
       print(temp_final)


       if int(temp_final) > 34:
           for i in buy_sunscreen_elements:
               if i.tag_name == 'button':
                   i.click()
                   break
       elif int(temp_final) < 19:
           for i in buy_moisturizer_elements:
               if i.tag_name == 'button':
                   i.click()
                   break

    def pick_product(self):
        product = PickProduct(driver=self)
        if int(temp_final) > 34:
            product.pick_product_sunscreen()
        elif int(temp_final) < 19:
            product.pick_product_moisturizer()






