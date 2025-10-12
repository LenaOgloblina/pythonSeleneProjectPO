from selene import browser
import os
from faker import Faker
from selene.support.shared import browser
from selene import have, be, command

fake = Faker()
fake_ru = Faker('ru_RU')
first_name = fake_ru.first_name()
last_name = fake_ru.last_name()
full_name = (first_name + ' ' + last_name)
email = fake_ru.email()
address = fake_ru.address()


def test_user_page():
    browser.open("/automation-practice-form")
    browser.element('.text-center').should(be.visible)

    #WHEN
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('input[value="Female"]+label').click()
    browser.element('#userNumber').type('9995555555')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="9"]').click()
    browser.element('.react-datepicker__day--028').click()

    browser.element('#subjectsInput').type('Hindi').press_tab()
    browser.element('#subjectsInput').type('Social Studies').press_tab()

    browser.all('.custom-checkbox').element_by(have.text("Music")).click()
    browser.all('.custom-checkbox').element_by(have.text("Reading")).click()
    correct_dir = os.path.abspath(os.path.dirname(__file__))
    resources_dir = os.path.join(correct_dir, 'resources')
    file_path = os.path.join(resources_dir, 'mem-kot.jpg')
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type(address)
    browser.element("#state").perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.exact_text('Haryana')
    ).click()
    browser.element("#city").perform(command.js.scroll_into_view)
    browser.element("#city").click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.exact_text('Karnal')
    ).click()

    browser.element('#submit').perform(command.js.click)

    #THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            full_name,
            email,
            'Female',
            '9995555555',
            '28 October,1990',
            'Hindi, Social Studies',
            'Music, Reading',
            'mem-kot.jpg',
            address,
            'Haryana Karnal',
        )
    )





