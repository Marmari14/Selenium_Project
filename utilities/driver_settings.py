from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from utilities.logger import setup_logger


class Settings:
	@staticmethod
	def set_settings(url):
		options = webdriver.ChromeOptions()

		# Настройки ChromeOptions
		chrome_options = [
			'--guest',
			'--ignore-certificate-errors',
			'--ignore-ssl-errors',
			'--start-maximized',
			'--disable-notifications'
		]

		for option in chrome_options:
			options.add_argument(option)

		options.add_experimental_option('detach', True)
		options.add_experimental_option('excludeSwitches', ['enable-logging'])

		service = Service(chromedriver_autoinstaller.install())

		driver = webdriver.Chrome(service=service, options=options)
		driver.get(url)
		logger = setup_logger("Settings")
		logger.info(f"Открыта страница: {url}")
		return driver