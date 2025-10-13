from faker import Faker
from selene import have

from pythonSeleneProjectPO.pages.registration_page import RegistrationPage

fake = Faker()
fake_ru = Faker('ru_RU')
first_name = fake_ru.first_name()
last_name = fake_ru.last_name()
full_name = (first_name + ' ' + last_name)
email = fake_ru.email()
address = fake_ru.address()


def test_user_page():

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_email(email)
    registration_page.fill_gender('Female')
    registration_page.fill_phone('9995555555')
    registration_page.fill_date_of_birth('1990', 'October', '28')
    registration_page.fill_subjects('Hindi')
    registration_page.fill_subjects('Social Studies')
    registration_page.fill_hobbies('Music')
    registration_page.fill_hobbies('Reading')
    registration_page.select_picture('mem-kot.jpg')
    registration_page.fill_address(address)
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.press_registration_button()

    #THEN
    registration_page.registered_user_data.should(
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
            'Haryana Karnal'
        )
    )
    # registration_page.should_have_registered_user_info_with(full_name, email, 'Female',
    #                                                         '9995555555', '28 October,1990',
    #                                                         'Hindi, Social Studies', 'Music, Reading',
    #                                                       'mem-kot.jpg', address, 'Haryana Karnal')






