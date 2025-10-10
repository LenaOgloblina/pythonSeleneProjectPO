from .base_page import BasePage
from .locators import RegistrationPageLocator


class RegistrationPage(BasePage):
    def should_be_registration_page(self):
        self.student_registration_form()

    def student_registration_form(self):
        assert self.is_element_present(*RegistrationPage.REGISTER_FORM), "Register form is not presented"
