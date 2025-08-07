import time

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from utilities.driver_settings import Settings


def test_filtering_and_buying():
    # driver = Settings.set_settings("https://leonardo.ru/")
    #
    # mp = MainPage(driver)
    # mp.select_category()
    driver = Settings.set_settings("https://leonardo.ru/ishop/tree_1446522862/")
    mp = MainPage(driver)
    mp.click_close_city_btn()

    cp = CatalogPage(driver)
    cp.install_filters()

    time.sleep(5)
    # driver.quit()
