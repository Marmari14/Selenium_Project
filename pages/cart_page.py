from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class CartPage(Base):
    """ Класс для работы со страницей корзины """
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
        """ Метод для сравнения цены товара в каталоге и в корзине """
        try:
            cart_price = self.__get_product_price()
            cart_price_text = cart_price.text
            cart_price_value = float(cart_price_text.replace(" ", ""))

            self.logger.info(f"Сравнение цен: каталог={catalog_price}, корзина={cart_price_value}")

            assert cart_price_value == catalog_price, \
                f"Цена в каталоге ({catalog_price}) и корзине ({cart_price_value}) не совпадает"

            self.logger.info("Цены в каталоге и корзине совпадают")

        except AssertionError as ae:
            self.logger.error(f"Ошибка сравнения цен: {str(ae)}")
            raise
        except Exception as ex:
            self.logger.error(f"Неожиданная ошибка при сравнении цен: {str(ex)}")
            raise

    def click_checkout_btn(self):
        """ Метод для перехода к оформлению товара """
        try:
            self._click_element(self.__get_checkout_btn())
            self.logger.info(f"Переход к оформлению заказа | URL {self._get_current_url()}")
        except Exception as ex:
            self.logger.error(f"Ошибка перехода к оформлению заказа: {str(ex)}")
            raise
