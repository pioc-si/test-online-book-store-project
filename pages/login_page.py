from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):  
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        self.should_be_authorized_user()
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login is expected in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"




