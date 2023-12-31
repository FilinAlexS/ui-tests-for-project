import time

import allure
from page_object.base_page import BasePage
from page_object.elements.cart_locators import CartLocators


class CartPage(BasePage):

    @allure.step("Open home page")
    def open(self, url):
        self._open(url)

    @allure.step("Add n element to the cart")
    def add_n_element_cart(self, element, count=1):
        count_items = self.quantity_items_on_button_cart()
        while count > 0:
            time.sleep(1)
            list_elems = self.elements(CartLocators.BUTTON_CART_ADD)
            self.click(list_elems[element])
            count_items += 1
            time.sleep(1)
            on_web = self.quantity_items_on_button_cart()
            assert on_web == count_items
            count -= 1

    @allure.step("Check quantity product in cart")
    def check_quantity_product_in_cart(self, quantity):
        quantity_product = len(self.elements(CartLocators.QUANTITY_PRODUCT_IN_CART))
        assert quantity_product == quantity

    @allure.step("Remove all products")
    def remove_all_product(self):
        quantity_product = len(self.elements(CartLocators.QUANTITY_PRODUCT_IN_CART))
        while quantity_product > 0:
            time.sleep(1)
            self.click(self.elements(CartLocators.REMOVE_PRODUCT)[0])
            quantity_product -= 1

    @allure.step("Check that remove all products")
    def check_remove_all_product(self):
        self.verify_text_in_element(CartLocators.NON_PRODUCT, CartLocators.CONTINUE)

    @allure.step("Go to the cart")
    def go_to_cart(self):
        time.sleep(1)
        with allure.step('Click cart button top'):
            self.click(self.element(CartLocators.CART_BUTTON_TOP))
        time.sleep(1)
        with allure.step('Click link to cart'):
            self.click(self.element(CartLocators.LINK_TO_CART))

    def quantity_items_on_button_cart(self):
        time.sleep(0.5)
        text_on_button_cart = self.element(CartLocators.CART_BUTTON_TOP).text
        count_items_on_web = text_on_button_cart[0]
        return int(count_items_on_web)
