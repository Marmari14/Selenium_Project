import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import Base
from pages.product_page import ProductPage


class CatalogPage(Base):
    """ Класс для работы со страницей каталога """
    # Locators

    __filter_price_from = "//input[@id='amount-min']"
    __filter_price_to = "//input[@id='amount-max']"
    __all_filters_btn = "//a[contains(@class, 'show-extended')]"
    __filter_checkbox = ("//div[contains(@class,'mb-0 custom-control custom-checkbox  ')]//a[contains(text(), '{}')]")
    __product_cards = "//div[@id='ajax_cont']//div[@class='px-2 py-3 item-wrap']"

    # Getters

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
        # Ждем появления хотя бы одной карточки
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.__product_cards)))
        return self.driver.find_elements(By.XPATH, self.__product_cards)

    # Actions

    def __clear_filter_price_from(self):
        try:
            self._clear_input(self.__get_filter_price_from())
            self.logger.debug("Очистка поля 'Цена от' выполнена")
        except Exception as e:
            self.logger.error(f"Ошибка при очистке поля 'Цена от': {str(e)}")
            raise

    def __input_filter_price_from(self, value):
        try:
            self._input(self.__get_filter_price_from(), value)
            self.logger.info(f"Установка значения 'Цена от': {value}")
        except Exception as e:
            self.logger.error(f"Ошибка при установке значения 'Цена от': {str(e)}")
            raise

    def __clear_filter_price_to(self):
        try:
            self._clear_input(self.__get_filter_price_to())
            self.logger.debug("Очистка поля 'Цена до' выполнена")
        except Exception as e:
            self.logger.error(f"Ошибка при очистке поля 'Цена до': {str(e)}")
            raise

    def __input_filter_price_to(self, value):
        try:
            self._input(self.__get_filter_price_to(), value)
            self.logger.info(f"Установка значения 'Цена до': {value}")
        except Exception as e:
            self.logger.error(f"Ошибка при установке значения 'Цена до': {str(e)}")
            raise

    def __click_checkbox(self, value):
        try:
            self._click_element(self.__get_filter_checkbox(value))
            self.logger.info(f"Выбран фильтр: '{value}'")
        except Exception as e:
            self.logger.error(f"Ошибка при выборе фильтра '{value}': {str(e)}")
            raise

    def __expand_filter(self):
        """ Метод для раскрытия списков фильтров """
        try:
            expand_button = self.__get_all_filters_btn()
            for btn in expand_button:
                if btn.text == "показать ещё":
                    self._click_element(btn)
        except Exception as e:
            error_msg = f"Не удалось раскрыть фильтр: {str(e)}"
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def choose_random_product(self):
        """ Метод выбора случайного товара на странице """
        try:
            product_cards = self.__get_product_cards()
            product = random.choice(product_cards)
            t = product.find_element(By.CLASS_NAME, "title")
            product_name = t.text
            product_link = product.find_element(By.CLASS_NAME, "img-link")
            product_url = product_link.get_attribute("href")

            self.logger.info(f"Выбран товар: '{product_name}' (URL: {product_url})")
            return ProductPage(self.driver, product_url)
        except Exception as e:
            self.logger.error(f"Ошибка при выборе случайного товара: {str(e)}")
            raise

    # Methods
    def install_filters(self, list_filters, price_from=None, price_to=None):
        """ Метод для установки фильтров """
        if price_from is not None:
            self.__clear_filter_price_from()
            self.__input_filter_price_from(price_from)
        if price_to is not None:
            self.__clear_filter_price_to()
            self.__input_filter_price_to(price_to)
        self.__expand_filter()
        for filter in list_filters:
            self.__click_checkbox(filter)

        # Временная задержка для применения фильтров и обновления товаров
        time.sleep(3)