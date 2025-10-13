from selene import browser, be, have, command

from ..pythonSeleneProjectPO import resource


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('.text-center').should(be.visible)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_tab()

    def fill_gender(self, value):
        browser.all('[name="gender"]').element_by(have.value(value)).element('..').click()

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)

    def fill_hobbies(self, value):
        #browser.all('.custom-checkbox').element_by(have.text(value)).click()
        browser.all(".custom-checkbox").element_by(have.text(value)).perform(command.js.scroll_into_view)
        browser.all(".custom-checkbox").element_by(have.text(value)).click()


    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
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
        browser.element('#uploadPicture').send_keys(resource.resource_path(value))

    def fill_state(self, value):
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        browser.element("#city").perform(command.js.scroll_into_view)
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def press_registration_button(self):
        browser.element('#submit').perform(command.js.click)
