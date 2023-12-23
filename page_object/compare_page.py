import allure
from page_object.base_page import BasePage
from page_object.elements.compare_locators import CompareLocators
import time


class ComparePage(BasePage):

    @allure.step
    def open(self, url):
        self._open(url)

    @allure.step("Add n element to the comparison")
    def add_n_element_compare(self, element):
        list_elems = self.elements(CompareLocators.BUTTON_COMPARE_ADD)
        elem = list_elems[element]
        time.sleep(0.5)
        self.click(elem)

    @allure.step("Click link 'product comparison'")
    def click_link_comparison(self):
        self.click(self.element(CompareLocators.COMPARE_PAGE_LINK))

    @allure.step("Сheck whether different products have been added")
    def check_dif_added_products(self):
        time.sleep(1)
        prod_1 = self.element(CompareLocators.COMPARE_PRODUCT_NAME_1).text
        prod_2 = self.element(CompareLocators.COMPARE_PRODUCT_NAME_2).text
        assert prod_1 != prod_2

    @allure.step("Delete n products")
    def remove_product(self, count):
        while count > 0:
            a = self.elements(CompareLocators.COMPARE_DELETE_PROD)
            self.click(a[0])
            count -= 1
            time.sleep(0.5)
        assert self.element(CompareLocators.COMPARE_NON_PROD).text == 'Continue'
