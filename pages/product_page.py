from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'There is no success message'
    
    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should be disappeared'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_be_correct_name_product(self, product_name, product_name_in_message):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, 'Product name in message is not correct product name'
        
    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), 'There is no message with product price'   
    
    def should_be_correct_price_product_in_message_and_price_product(self, product_price, product_price_in_message):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, 'Product price in message is not correct product price'



 

    

