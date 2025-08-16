import time

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from utilities.driver_settings import Settings


def test_e2e(set_up):

    driver = Settings.set_settings("https://www.zootovar-spb.ru/")

    catalog = CatalogPage(driver)
    catalog.select_category("Кошки>Сухой корм>Взрослые")
    list_filters = ['Brit', 'Florida', 'индейка', 'клюква', 'супер-премиум']
    price_min = 1000
    price_max = 3000
    catalog.install_filters(list_filters, price_min, price_max)

    product = catalog.choose_random_product()
    product._get_current_url()
    product.verify_filters(list_filters)
    product_price = product.add_to_cart_filter_price(price_min, price_max)

    cart = CartPage(driver)
    cart.view_cart()
    cart.compare_prices(product_price)
    cart.click_checkout_btn()

    checkout = CheckoutPage(driver)
    checkout.fill_in_the_data("QR")

    time.sleep(5)
    driver.quit()
