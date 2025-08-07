from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def get_current_url(self):
        """Метод получения текущей url"""
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    def move_to_element(self, element):
        """Метод для перемещения к элементу"""
        self.actions.move_to_element(element).perform()
        print("Move to element")

    def click_btn(self, element):
        """Метод для перемещения к элементу  нажатия"""
        self.move_to_element(element)
        element.click()

    def clear_input(self, element):
        self.move_to_element(element)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

    def input(self, element, value):
        self.move_to_element(element)
        element.send_keys(value )

