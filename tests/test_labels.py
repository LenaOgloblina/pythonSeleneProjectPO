import allure
from allure_commons.types import Severity

def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'eroshenkoam')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Навторизированный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')
    pass

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизированный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass