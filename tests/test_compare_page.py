import allure
from page_object.compare_page import ComparePage


@allure.feature('Compare page')
@allure.story('Adding, deleting and checking product comparisons')
def test_product_comparison_page(browser):
    compare = ComparePage(browser)
    compare.open(browser.url)
    compare.add_n_element_compare(0)
    compare.add_n_element_compare(2)
    compare.click_link_comparison()
    compare.check_dif_added_products()
    compare.remove_product(2)
