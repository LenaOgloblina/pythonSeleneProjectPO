import allure
from selene import browser, be, have, command, by


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.config.window_width = 1280
        browser.config.window_height = 800
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').should(be.enabled)
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
        (browser.element('#query-builder-test').submit())

    with allure.step('Переходим по ссылке репозитория'):
        browser.element("//em[contains(text(), 'allure')]").click()

    with allure.step('Открываем таб Pull request'):
        browser.element('[data-content="Pull requests"]').click()

    with allure.step('Проверяем наличие Pull request #79'):
        browser.element(by.partial_text('#79')).should(be.visible)   # #79 'eroshenkoam/allure-example' 'allure'


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('allure')
    open_pull_request_tab()
    should_see_pull_request_with_number('#79')

@allure.step('Открываем главную страницу')
def open_main_page():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').should(be.enabled)
    browser.element('#query-builder-test').send_keys(repo)
    (browser.element('#query-builder-test').submit())

@allure.step('Переходим по ссылке репозитория {repo_past}')
def go_to_repository(repo_past):
    browser.element(f"//em[contains(text(), {repo_past})]").click()

@allure.step('Открываем таб Pull request')
def open_pull_request_tab():
    browser.element('[data-content="Pull requests"]').click()

@allure.step('Проверяем наличие Pull request {number}')
def should_see_pull_request_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)