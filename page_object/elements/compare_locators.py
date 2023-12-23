from selenium.webdriver.common.by import By


class CompareLocators:
    BUTTON_COMPARE_ADD = (By.XPATH, "//*[contains(@class, 'button-group')]/button[3]")
    COMPARE_PAGE_LINK = (By.XPATH, "//*/a[.='product comparison']")
    COMPARE_PRODUCT_NAME_1 = (By.XPATH, '//*[@id="content"]/table/tbody[1]//tr[1]/td[2]/a/strong')
    COMPARE_PRODUCT_NAME_2 = (By.XPATH, '//*[@id="content"]/table/tbody[1]//tr[1]/td[3]/a/strong')
    COMPARE_DELETE_PROD = (By.XPATH, "//*/a[.='Remove']")
    COMPARE_NON_PROD = (By.XPATH, "//*/a[.='Continue']")
