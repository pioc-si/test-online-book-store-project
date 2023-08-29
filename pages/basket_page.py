from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'Busket is not empty, but should be'

    def should_be_empty_basket_message(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text , \
        f'Basket is not empty, but should be'   

