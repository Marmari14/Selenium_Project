import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class MainPage(Base):
    # Locators

    __close_city_btn = "//button[contains(@class, '__close-btn-action currentcity-determinator__actions-wrapper-btn')]"
    __menu_btn = "//a[@class='header__burger']"
    __menu_item = "//li[@data-cover='1444732062']"
    __menu_subitem = "//a[@data-treelev='1446522862']"

    # Getters
    def __get_close_city_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__close_city_btn)))


    def __get_menu_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.__menu_btn)))

    def __get_menu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__menu_item)))

    def __get_menu_subitem(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__menu_subitem)))

    # Actions

    def click_close_city_btn(self):
        self.click_btn(self.__get_close_city_btn())
        print("Close city btn")

    def __click_menu_btn(self):
        self.click_btn(self.__get_menu_btn())
        print("Click menu")

    def __click_menu_item(self):
        self.click_btn(self.__get_menu_item())
        print("Click menu item")

    def __click_menu_subitem(self):
        self.click_btn(self.__get_menu_subitem())
        print("Click menu subitem")

    # Methods
    def select_category(self):
        self.get_current_url()
        self.click_close_city_btn()
        self.__click_menu_btn()
        self.__click_menu_item()
        self.__click_menu_subitem()

