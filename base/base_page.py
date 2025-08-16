from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    """ Базовый класс, содержащий универсальные методы """

    # Locators

    __menu_item = "//div[@class = 'animal d-flex flex-column']"
    __menu_subitem = "//a[@class = 'p-2 text-center']"
    __cart_btn = "//div[@class='top-right-menu w-100 ']//a[@class='text-decoration-none top-cart']"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    # Getters

    def __get_menu_item(self, value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__menu_item}//a[contains(text(), '{value}')]")))

    def __get_menu_subitem(self, value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"{self.__menu_subitem}//div[contains(text(), '{value}')]")))

    def __get_cart_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__cart_btn)))

    # Actions

    def __click_menu_item(self, value):
        self._click_element(self.__get_menu_item(value))
        print(f"Select category {value}")

    def __click_menu_subitem(self, value):
        self._click_element(self.__get_menu_subitem(value))
        print(f"Select category {value}")

    def __click_cart_btn(self):
        self._click_element(self.__get_cart_btn())
        self._get_current_url()
        print("Go to the shopping cart")

    # Methods
    def select_category(self, list_items):
        self._get_current_url()
        items = list_items.split('>')
        self.__click_menu_item(items[0])
        items.pop(0)
        for item in items:
            self.__click_menu_subitem(item)

    def view_cart(self):
        self.__click_cart_btn()

    def _get_current_url(self):
        """Метод получения текущей url"""
        get_url = self.driver.current_url
        print(f"\nCurrent URL: {get_url}")

    def _move_to_element(self, element):
        """Метод для перемещения к элементу"""
        self.actions.move_to_element(element).perform()

    def _click_element(self, element):
        """Метод для перемещения к элементу  нажатия"""
        self._move_to_element(element)
        element.click()

    def _clear_input(self, element):
        self._move_to_element(element)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

    def _input(self, element, value):
        self._move_to_element(element)
        element.send_keys(value)

