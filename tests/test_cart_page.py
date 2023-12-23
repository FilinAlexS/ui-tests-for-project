import allure
from page_object.cart_page import CartPage


@allure.feature('Cart page')
@allure.story('Adding, deleting and checking cart')
def test_product_comparison_page(browser):
    cart = CartPage(browser)
    cart.open(browser.url)
    cart.add_n_element_cart(0, 5)
    cart.add_n_element_cart(1)
    cart.go_to_cart()
    cart.check_quantity_product_in_cart(2)
    cart.remove_all_product()
    cart.check_remove_all_product()
