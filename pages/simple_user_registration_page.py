from selene import browser


class simpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.currentAddress = browser.element('#currentAddress')
        self.permanentAddress = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/text-box')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_current_address(self, value):
        self.currentAddress.type(value)

    def fill_permanent_address(self, value):
        self.permanentAddress.type(value)

    def submit(self):
        self.submit_button.click()

    def should_have_submited(self, full_name, email, currentAddress, permanentAddress):
        pass
