import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import Base
from pages.product_page import ProductPage


class CatalogPage(Base):
    # Locators

    __filter_price_from = "//input[@id='amount-min']"
    __filter_price_to = "//input[@id='amount-max']"
    __all_filters_btn = "//a[contains(@class, 'show-extended')]"
    __filter_checkbox = ("//div[contains(@class,'mb-0 custom-control custom-checkbox  ')]//a[contains(text(), '{}')]")
    __agree_cookies_btn = "//button[@class='btn btn-info mt-2']"
    __product_cards = "//div[contains(@class, 'justify-content-md-start') or .//div[@id='productContainer']]//div[@class='px-2 py-3 item-wrap']"

    # Getters

    def __get_agree_cookies_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__agree_cookies_btn)))

    def __get_filter_price_from(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_price_from)))

    def __get_filter_price_to(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_price_to)))

    def __get_all_filters_btn(self):
        all_buttons = self.driver.find_elements(By.XPATH, self.__all_filters_btn)
        visible_buttons = [btn for btn in all_buttons if btn.is_displayed()]
        return visible_buttons

    def __get_filter_checkbox(self, value):
        xpath = self.__filter_checkbox.format(value)
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def __get_product_cards(self):
        return self.driver.find_elements(By.XPATH, self.__product_cards)

    # Actions

    def __agree_cookies(self):
        self._click_element(self.__get_agree_cookies_btn())
        print("agree cookies")

    def __clear_filter_price_from(self):
        self._clear_input(self.__get_filter_price_from())
        print("Clear price from")

    def __input_filter_price_from(self, value):
        self._input(self.__get_filter_price_from(), value)
        print(f"Set price from {value}")

    def __clear_filter_price_to(self):
        self._clear_input(self.__get_filter_price_to())
        print("Clear price to")

    def __input_filter_price_to(self, value):
        self._input(self.__get_filter_price_to(), value)
        print(f"Set price to {value}")

    def __click_checkbox(self, value):
        self._click_element(self.__get_filter_checkbox(value))
        print(f"Filter '{value}' is selected")

    def __expand_filter(self):
        """Раскрывает список фильтра"""
        try:
            # Находим кнопку "Все" для раскрытия списка
            expand_button = self.__get_all_filters_btn()

            # Проверяем, не раскрыт ли уже список
            for btn in expand_button:
                if btn.text == "показать ещё":
                    self._click_element(btn)

        except Exception as e:
            print(f"Не удалось раскрыть фильтр: {str(e)}")
            raise

    def choose_random_product(self):
        product_cards = self.__get_product_cards()
        product = random.choice(product_cards)
        t = product.find_element(By.CLASS_NAME, "title")
        print(f"Select product: {t.text}")
        product_link = product.find_element(By.CLASS_NAME, "img-link")
        product_url = product_link.get_attribute("href")
        return ProductPage(self.driver, product_url)

    # Methods
    def install_filters(self, list_filters, price_from=None, price_to=None):
        self._get_current_url()
        self.__agree_cookies()
        if price_from is not None:
            self.__clear_filter_price_from()
            self.__input_filter_price_from(price_from)
        if price_to is not None:
            self.__clear_filter_price_to()
            self.__input_filter_price_to(price_to)
        self.__expand_filter()
        for filter in list_filters:
            self.__click_checkbox(filter)
        time.sleep(5)