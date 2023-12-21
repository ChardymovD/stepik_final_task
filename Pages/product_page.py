from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def item_added_to_cart(self):
        self.name_should_match()
        self.price_should_match()

    def name_should_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_notification = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION).text
        assert str(product_name) == str(product_name_in_notification), "The product name does not match."

    def price_should_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_notification = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_NOTIFICATION).text
        assert str(product_price) == str(product_price_in_notification), "The cost of the product does not match."
