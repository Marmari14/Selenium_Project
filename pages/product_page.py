from selenium.webdriver.common.by import By

from base.base_page import Base


class ProductPage(Base):
    def __init__(self, driver, url=None):
        super().__init__(driver)
        if url:
            self.driver.get(url)  # Переходим на страницу товара, если URL задан

    __price_blocks = "//div[contains(@class,'tocart-row row')]"
    __price = ".//span[@class = 'big text-semibold']"
    __btn_add = ".//button[contains(@class, 'incart_btn')]"

    def __get_prices(self):
        return self.driver.find_elements(By.XPATH, self.__price_blocks)


    def __get_product_data(self):
        details = self.driver.find_elements(By.CSS_SELECTOR, '.mt-2.mb-1 div')
        return [detail.text.split(":")[1].strip() for detail in details if ":" in detail.text]

    def __get_btn_add(self, min_price, max_price):
        price_blocks = self.__get_prices()
        for block in price_blocks:
            try:
                # Получаем элемент с ценой
                price_element = block.find_element(By.XPATH, self.__price)
                price_text = price_element.text

                # Очищаем цену от лишних символов и пробелов
                price = float(price_text.replace('руб', '').replace(' ', '').strip())

                # Проверяем попадает ли цена в диапазон
                if min_price <= price <= max_price:
                    # Находим кнопку "В корзину" в этом блоке
                    add_button = block.find_element(By.XPATH, self.__btn_add)
                    return add_button, price

            except Exception as e:
                print(f"Ошибка при обработке блока: {e}")
                continue

            # Если ничего не найдено
        raise Exception(f"Не найдено товаров в диапазоне {min_price}-{max_price} руб")


    def add_to_cart_filter_price(self, price_from, price_to):
        btn_add, price = self.__get_btn_add(price_from, price_to)
        self._click_element(btn_add)
        print("Product add to cart")
        return price

    def verify_filters(self, list_filters):
        data_product = self.__get_product_data()
        combined_values = " ".join(data_product).lower()
        matches =  sum(1 for filter_text in list_filters if filter_text.lower() in combined_values)
        print(f"The product matches {matches} filters out of {len(list_filters)}")