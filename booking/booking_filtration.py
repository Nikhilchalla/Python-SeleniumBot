#this file will include a class with instance methods.
# that will be responsible to interact with our website
#after we have some results, to apply filtration.
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __int__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.ID, 'filter_class')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star in star_values:
            for star_child in star_child_elements:
                if str(star_child.get_attribute('innerHTML')).strip() == f'{star} stars':
                    star_child.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')

