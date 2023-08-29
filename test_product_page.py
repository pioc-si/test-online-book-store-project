import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


login_link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


class TestUserAddToBasketFromProductPage:
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
                email = str(time.time()) + "@fakemail.org"
                password = str(time.time()) + "fakepassword"
                page = LoginPage(browser, login_link)
                page.open()
                page.register_new_user(email, password)
                page.should_be_authorized_user()

        def test_user_cant_see_success_message(self, browser):
                link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                page = ProductPage(browser, link)
                page.open()
                page.should_not_be_success_message()  

        @pytest.mark.need_review
        def test_user_can_add_product_to_basket(self, browser):
                link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.should_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
                link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.should_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_success_message_is_disappeared() 


def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, link)
        page.should_be_empty_basket()
        page.should_be_empty_basket_message()

"""
@pytest.mark.parametrize('number_link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]) 
class TestClass:
        @pytest.mark.xfail
        def test_should_be_success_message(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_success_message_is_disappeared() #Success message is presented, but should be disappeared

        def test_should_be_correct_name_product(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_correct_name_product()
                
        def test_should_be_basket_price_message(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_basket_price_message()
                
        def test_should_be_correct_price_product_in_message_and_price_product(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_basket_price_message()
                page.should_be_correct_price_product_in_message_and_price_product """

               