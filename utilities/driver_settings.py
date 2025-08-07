from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Settings:
    @staticmethod
    def set_settings(url):
        options = webdriver.ChromeOptions()  # возможность добавлять дополнительные настройки для браузера
        options.add_experimental_option('detach', True)  # опция, которая не позволит нашему браузеру закрыться
        options.add_argument("--guest")  # опция, которая отключает оповещения от Браузера, с просьбой смены пароля
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("--headless")
        service = Service(executable_path="C:/Users/User/PycharmProjects/SeleniunProject/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        driver.maximize_window()
        return driver
