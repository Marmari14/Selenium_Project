from selenium.webdriver.common.by import By

from base.base_page import Base


class ProductPage(Base):
	""" Класс для работы со страницей товара """
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

	def __get_btn_add(self, min_price=None, max_price=None):
		""" Метод для поиска кнопки корзины для заданного ценового диапазона """
		price_blocks = self.__get_prices()
		self.logger.debug(f"Поиск товара с фильтром цены: от {min_price} до {max_price} руб")
		self.logger.debug(f"Найдено блоков с ценами: {len(price_blocks)}")

		for block in price_blocks:
			try:
				price_element = block.find_element(By.XPATH, self.__price)
				price_text = price_element.text
				price = float(price_text.replace('руб', '').replace(' ', '').strip())

				self.logger.debug(f"Обработка товара с ценой: {price} руб")

				# Проверяем условия
				price_condition = True
				if min_price is not None:
					price_condition &= (price >= min_price)
					if not price_condition:
						self.logger.debug(f"Цена {price} руб ниже минимальной {min_price} руб")
						continue
				if max_price is not None:
					price_condition &= (price <= max_price)
					if not price_condition:
						self.logger.debug(f"Цена {price} руб выше максимальной {max_price} руб")
						continue

				if price_condition:
					add_button = block.find_element(By.XPATH, self.__btn_add)
					self.logger.info(f"Найден подходящий товар: {price} руб")
					return add_button, price

			except Exception as e:
				self.logger.warning(f"Ошибка при обработке блока товара: {e}")
				continue

		# Формируем сообщение об ошибке
		error_msg = ""
		if min_price is None and max_price is None:
			error_msg = "Не найдено товаров на странице"
		elif min_price is not None and max_price is None:
			error_msg = f"Не найдено товаров с ценой от {min_price} руб"
		elif min_price is None and max_price is not None:
			error_msg = f"Не найдено товаров с ценой до {max_price} руб"
		else:
			error_msg = f"Не найдено товаров в диапазоне {min_price}-{max_price} руб"

		self.logger.error(error_msg)
		raise Exception(error_msg)

	def add_to_cart_filter_price(self, price_from=None, price_to=None):
		""" Метод для добавления товара в заданном ценом диапазоне в корзину """
		try:
			btn_add, price = self.__get_btn_add(price_from, price_to)
			self._click_element(btn_add)
			self.logger.info(f"Товар добавлен в корзину | Цена: {price} руб")
			return price
		except Exception as e:
			self.logger.error(f"Ошибка добавления товара в корзину: {str(e)}")
			raise

	def verify_filters(self, list_filters):
		""" Метод для проверки соответсвия тора заданным фильтрам """
		try:
			data_product = self.__get_product_data()
			combined_values = " ".join(data_product).lower()

			matches = sum(1 for filter_text in list_filters if filter_text.lower() in combined_values)

			self.logger.info(
				f"Проверка фильтров: товар соответствует {matches} из {len(list_filters)} фильтров"
			)

			return matches
		except Exception as e:
			self.logger.error(f"Ошибка проверки фильтров: {str(e)}")
			raise
