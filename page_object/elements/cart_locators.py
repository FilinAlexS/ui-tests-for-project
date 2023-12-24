from selenium.webdriver.common.by import By


class CartLocators:
    BUTTON_CART_ADD = (By.XPATH, "//*[contains(@class, 'button-group')]/button[1]")
    CART_BUTTON_TOP = (By.XPATH, "//*[@id='cart']//span/..")
    LINK_TO_CART = (By.XPATH, "//*/a[.=' View Cart']")
    QUANTITY_PRODUCT_IN_CART = (By.XPATH, "//*[@id='content']/form/div/table/tbody/tr")
    REMOVE_PRODUCT = (By.XPATH, "//*/table//button[2]")
    NON_PRODUCT = (By.XPATH, "//*/a[.='Continue']")
    CONTINUE = 'Continue'
