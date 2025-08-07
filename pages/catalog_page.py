import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import Base


class CatalogPage(Base):
    # Locators

    __filter_price_from = "//div[@id='sls-pricef']//input[@id='range-begin']"
    __filter_price_to = "//div[@id='sls-pricef']//input[@id='range-finish']"
    __all_filters_btn = "//button[@class = 'sls__item sls__link showall-btn']"
    __filter_brand = "//div[@id='sls-list-trademark']//span[@class='filter__title']"
    __filter_color = "//div[@id='sls-list-colors']//span[@class='filter__title']"
    __filter_length_from = "//div[@id='sls-htdlinanitim']//input[@id='range-begin']"
    __filter_length_to = "//div[@id='sls-htdlinanitim']//input[@id='range-finish']"

    # Getters

    def __get_filter_price_from(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_price_from)))

    def __get_filter_price_to(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_price_to)))

    def __get_all_filters_btn(self, data_toggle):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__all_filters_btn}[contains(@data-toggle, '{data_toggle}')]")))

    def __get_filter_brand(self, name_brand):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__filter_brand}[normalize-space()='{name_brand}']/ancestor::label")))

    def __get_filter_color(self, color):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__filter_color}[normalize-space()='{color}']/ancestor::label")))

    def __get_filter_length_from(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_length_from)))

    def __get_filter_length_to(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__filter_length_to)))

    # Actions

    def __clear_filter_price_from(self):
        self.clear_input(self.__get_filter_price_from())
        print("Clear price from")

    def __input_filter_price_from(self, value):
        self.input(self.__get_filter_price_from(), value)
        print(f"Set price from {value}")

    def __clear_filter_price_to(self):
        self.clear_input(self.__get_filter_price_to())
        print("Clear price to")

    def __input_filter_price_to(self, value):
        self.input(self.__get_filter_price_to(), value)
        print(f"Set price to {value}")

    def __click_brand(self, name_brand):
        self.click_btn(self.__get_filter_brand(name_brand))
        print(f"Brand '{name_brand}' is selected")

    def __click_color(self, color):
        self.click_btn(self.__get_filter_color(color))
        print(f"Color '{color}' is selected")

    def __expand_filter(self, data_toggle):
        """Раскрывает список фильтра"""
        try:
            # Находим кнопку "Все" для раскрытия списка
            expand_button = self.__get_all_filters_btn(data_toggle)

            # Проверяем, не раскрыт ли уже список
            if expand_button.get_attribute("aria-expanded") == "false":
                self.click_btn(expand_button)

        except Exception as e:
            print(f"Не удалось раскрыть фильтр: {str(e)}")
            raise

    def __clear_filter_length_from(self):
        self.clear_input(self.__get_filter_length_from())
        print("Clear length from")

    def __input_filter_length_from(self, value):
        self.input(self.__get_filter_length_from(), value)
        print(f"Set length from {value}")

    def __clear_filter_length_to(self):
        self.clear_input(self.__get_filter_length_to())
        print("Clear length to")

    def __input_filter_length_to(self, value):
        self.input(self.__get_filter_length_to(), value)
        print(f"Set length to {value}")

    # Methods
    def install_filters(self):
        self.get_current_url()
        self.__clear_filter_price_from()
        self.__input_filter_price_from("100")
        self.__clear_filter_price_to()
        self.__input_filter_price_to("500")
        self.__expand_filter("sls-list-trademark")
        self.click_btn(self.__get_filter_brand("Alize"))
        self.__expand_filter("sls-list-colors")
        self.__click_color("Розовый")
        self.__clear_filter_length_from()
        self.__input_filter_length_from("10")
        self.__clear_filter_length_to()
        self.__input_filter_length_to("200")
        time.sleep(5)
