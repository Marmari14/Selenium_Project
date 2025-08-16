import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base
from utilities.fake_data_generator import FakeDataGenerator


class CheckoutPage(Base):

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
        address = self.random_info.random_address()
        self._input(self.__get_address(), address)
        print(f"Address: {address}")

    def __input_surname(self):
        surname = self.random_info.random_surname()
        self._input(self.__get_surname(), surname)
        print(f"Surname: {surname}")

    def __input_name(self):
        name = self.random_info.random_name()
        self._input(self.__get_name(), name)
        print(f"Name: {name}")

    def __input_phone(self):
        phone = self.random_info.random_phone()
        digits = re.sub(r'\D', '', phone)
        self._input(self.__get_phone(), digits[-10:])
        print(f"Phone: {phone}")

    def __input_email(self):
        email = self.random_info.random_email()
        self._input(self.__get_email(), email)
        print(f"Email: {email}")

    def __click_payment_method(self, value):
        payment_method = self.__get_payment_method(value)
        self._click_element(payment_method)
        print(f"Payment method: {payment_method.text}")

    # Methods
    def fill_in_the_data(self, payment_method):
        self.__input_address()
        self.__click_payment_method(payment_method)
        self.__input_surname()
        self.__input_name()
        self.__input_phone()
        self.__input_email()
