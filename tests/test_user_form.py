from selene import browser

def test_user_page():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Ирина')
    browser.element('#lastName').type('Иванова')
    browser.element('#lastName').type('test132@gmail.com')
    browser.all('#genterWrapper > .col-md-9').element('')
