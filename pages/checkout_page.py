import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base
from utilities.fake_data_generator import FakeDataGenerator


class CheckoutPage(Base):
    """ Класс для работы со страницей оформления заказа """

    def __init__(self, driver):
        super().__init__(driver)
        self.random_info = FakeDataGenerator()

    # Locators

    __address = "//input[@id='delivery_address']"
    __payment_method = ("//div[contains(@class, 'oplata-li')]//label[contains(text(), '{}')]")
    __surname = "//input[@id='fio']"
    __name = "//input[@name='name']"
    __phone = "//input[@id='phone']"
    __email = "//input[@id='email']"

    # Getters

    def __get_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__address)))

    def __get_payment_method(self, value):
        xpath = self.__payment_method.format(value)
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def __get_surname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__surname)))

    def __get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__name)))

    def __get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__phone)))

    def __get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__email)))

    # Actions

    def __input_address(self):
        try:
            address = self.random_info.random_address()
            self._input(self.__get_address(), address)
            self.logger.info(f"Введен адрес: '{address}'")
        except Exception as ex:
            self.logger.error(f"Ошибка ввода адреса: {str(ex)}")
            raise

    def __input_surname(self):
        try:
            surname = self.random_info.random_surname()
            self._input(self.__get_surname(), surname)
            self.logger.info(f"Введена фамилия: '{surname}'")
        except Exception as ex:
            self.logger.error(f"Ошибка ввода фамилии: {str(ex)}")
            raise

    def __input_name(self):
        try:
            name = self.random_info.random_name()
            self._input(self.__get_name(), name)
            self.logger.info(f"Введено имя: '{name}'")
        except Exception as ex:
            self.logger.error(f"Ошибка ввода имени: {str(ex)}")
            raise

    def __input_phone(self):
        try:
            phone = self.random_info.random_phone()
            digits = re.sub(r'\D', '', phone)
            formatted_phone = digits[-10:]
            self._input(self.__get_phone(), formatted_phone)
            self.logger.info(f"Введен телефон: '{phone}' -> '{formatted_phone}'")
        except Exception as ex:
            self.logger.error(f"Ошибка ввода телефона: {str(ex)}")
            raise

    def __input_email(self):
        try:
            email = self.random_info.random_email()
            self._input(self.__get_email(), email)
            self.logger.info(f"Введен email: '{email}'")
        except Exception as ex:
            self.logger.error(f"Ошибка ввода email: {str(ex)}")
            raise

    def __click_payment_method(self, value):
        try:
            payment_method = self.__get_payment_method(value)
            method_text = payment_method.text
            self._click_element(payment_method)
            self.logger.info(f"Выбран способ оплаты: '{method_text}'")
        except Exception as ex:
            self.logger.error(f"Ошибка выбора способа оплаты '{value}': {str(ex)}")
            raise

    # Methods
    def fill_in_the_data(self, payment_method):
        """ Метод для заполнения данных для оформления заказа """
        self.__input_address()
        self.__click_payment_method(payment_method)
        self.__input_surname()
        self.__input_name()
        self.__input_phone()
        self.__input_email()
