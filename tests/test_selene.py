from selene import browser, be, have, command, by


def test_githab():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.open('https://github.com')
    browser.element('.search-input').click()
    browser.element('#query-builder-test').should(be.enabled)
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
    (browser.element('#query-builder-test').submit())

    browser.element("//em[contains(text(), 'allure')]").click()

    browser.element('[data-content="Pull requests"]').click()

    browser.element(by.partial_text('#79')).should(be.visible)   # #79

