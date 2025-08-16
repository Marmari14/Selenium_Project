from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class CartPage(Base):
    # Locators

    __product_price = "//span[contains(@id, 'summa')]"
    __checkout_btn = "//div[@class='mt-3']//button[contains(@class, ' fbInitiateCheckoutBtn')]"

    # Getters

    def __get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__product_price)))

    def __get_checkout_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.__checkout_btn)))

    # Methods
    def compare_prices(self, catalog_price):
        cart_price = self.__get_product_price()
        cart_price_text = cart_price.text
        assert float(cart_price_text.replace(" ", "")) == catalog_price, "The price in the catalog and in the shopping cart do not match"
        print("The price in the catalog and in the shopping cart are the same")

    def click_checkout_btn(self):
        self._click_element(self.__get_checkout_btn())
        print("Going to checkout")
