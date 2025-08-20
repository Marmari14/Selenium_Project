from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import setup_logger


class Base:
    """ Базовый класс, содержащий универсальные методы """

    # Locators

    __menu_item = "//div[@class = 'animal d-flex flex-column']"
    __menu_subitem = "//a[@class = 'p-2 text-center']"
    __cart_btn = "//div[@class='top-right-menu w-100 ']//a[@class='text-decoration-none top-cart']"
    __agree_cookies_btn = "//button[@class='btn btn-info mt-2']"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.logger = setup_logger(self.__class__.__name__)

    # Getters

    def __get_menu_item(self, value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__menu_item}//a[contains(text(), '{value}')]")))

    def __get_menu_subitem(self, value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__menu_subitem}//div[contains(text(), '{value}')]")))

    def __get_cart_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__cart_btn)))

    def __get_agree_cookies_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__agree_cookies_btn)))

    # Actions

    def __click_menu_item(self, value):
        try:
            self._click_element(self.__get_menu_item(value))
            self.logger.info(f"Выбрана категория: '{value}'")
        except Exception as e:
            self.logger.error(f"Ошибка выбора категории '{value}': {str(e)}")
            raise

    def __click_menu_subitem(self, value):
        try:
            self._click_element(self.__get_menu_subitem(value))
            self.logger.info(f"Выбрана подкатегория: '{value}'")
        except Exception as e:
            self.logger.error(f"Ошибка выбора подкатегории '{value}': {str(e)}")
            raise

    def __click_cart_btn(self):
        try:
            self._click_element(self.__get_cart_btn())
            self.logger.info(f"Переход в корзину | URL {self._get_current_url()}")
        except Exception as e:
            self.logger.error(f"Ошибка перехода в корзину: {str(e)}")
            raise

    # Methods
    def select_category(self, list_items):
        """ Метод для перехода в каталог по указанному пути """
        items = list_items.split('>')
        self.__click_menu_item(items[0])
        items.pop(0)
        for item in items:
            self.__click_menu_subitem(item)
        self.logger.info(f"Переход в каталог | URL {self._get_current_url()}")

    def view_cart(self):
        """ Метод для перехода в корзину """
        self.__click_cart_btn()

    def agree_cookies(self):
        """ Метод для соглашения с использование cookies """
        try:
            self._click_element(self.__get_agree_cookies_btn())
            self.logger.info("Принятие cookies выполнено")
        except Exception as e:
            self.logger.error(f"Ошибка при принятии cookies: {str(e)}")
            raise

    def _get_current_url(self):
        """ Метод получения текущей url """
        return self.driver.current_url

    def _move_to_element(self, element):
        """ Метод для перемещения к элементу """
        self.actions.move_to_element(element).perform()

    def _click_element(self, element):
        """ Метод для нажатия на элемент """
        self._move_to_element(element)
        element.click()

    def _clear_input(self, element):
        """ Метод для очищения поля ввода """
        self._move_to_element(element)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

    def _input(self, element, value):
        """ Метод для ввода данных в поле """
        self._move_to_element(element)
        element.send_keys(value)

