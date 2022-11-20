from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from booking import constant as const
from booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"G:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def currency_change(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def search_place_to_go(self, place_to_go):
        search_place = self.find_element(By.ID, 'ss')
        search_place.clear()
        search_place.send_keys(place_to_go)

        first_search = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_search.click()

    def select_dates(self, check_in, check_out):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        check_out_element.click()


    def select_adult(self, count = 1):
        select_element = self.find_element(By.ID, 'xp__guests__toggle')
        select_element.click()

        while True:
            decrease_adults = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decrease_adults.click()

            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute('value')

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.CSS_SELECTOR,'button[aria-label="Increase number of Adults')
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()


    def apply_filtrations(self):
        filtration = BookingFiltration()
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()













