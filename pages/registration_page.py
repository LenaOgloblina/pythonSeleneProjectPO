from selene import browser, be, have, command

from ..pythonSeleneProjectPO import resource


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even
        self.firstName = browser.element('#firstName')
        self.lastName = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.address = browser.element('#currentAddress')
        self.subject = browser.element('#subjectsInput')
        self.gender = browser.all('[name="gender"]')
        self.phone = browser.element('#userNumber')
        self.hobby = browser.all(".custom-checkbox")
        self.dateOfBirth = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')
        self.picture = browser.element('#uploadPicture')
        self.state = browser.element("#state")
        self.city = browser.element("#city")
        self.submit = browser.element('#submit')

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('.text-center').should(be.visible)

    def fill_first_name(self, value):
        self.firstName.type(value)

    def fill_last_name(self, value):
        self.lastName.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_address(self, value):
        self.address.type(value)

    def fill_subjects(self, value):
        self.subject.type(value).press_tab()

    def fill_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()

    def fill_phone(self, value):
        self.phone.type(value)

    def fill_hobbies(self, value):
        self.hobby.element_by(have.text(value)).perform(command.js.scroll_into_view)
        self.hobby.element_by(have.text(value)).click()


    def fill_date_of_birth(self, year, month, day):
        self.dateOfBirth.click()
        self.year.type(year)
        self.month.type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    # @property
    # def registered_user_data(self):
    #     return browser.element('.table').all('td').even

    # def should_have_registered_user_info_with(self, full_name, email, gender,
    #                                           phone, date_of_birth, subjects,
    #                                           hobbies, profile_pic, address, city):
    #     browser.element('.table').all('td').even.should(
    #         have.exact_texts(
    #             full_name,
    #             email,
    #             gender,
    #             phone,
    #             date_of_birth,
    #             subjects,
    #             hobbies,
    #             profile_pic,
    #             address,
    #             city
    #         )
    #     )

    def select_picture(self, value):
        self.picture.send_keys(resource.resource_path(value))

    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        self.city.perform(command.js.scroll_into_view)
        self.city.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def press_registration_button(self):
        self.submit.perform(command.js.click)
