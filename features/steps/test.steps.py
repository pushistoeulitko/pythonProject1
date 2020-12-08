from behave import *
from selenium.webdriver import chrome, firefox
import json
from features.steps.brower_setting import Browser
from features.steps.my_methods import Methods
from features.steps.Locators import Locators
from features.steps.parse_methods import Parse
from features.steps.Page import Page
from features.steps.storage import Storage


@given('Открываем сайт')
def open_main_page(context):
    Browser.settings(context, chrome, False)
    Methods.open_page(context, Page.MAIN.value)
    Methods.screenshots(context)
    Methods.spam(context)


@when('Переходим на вкладку Котировки')
def go_to_data1(context):
    Methods.move_mouse_to_element(context, Locators.LOCATOR_PATH1)
    Methods.screenshots(context)


@when('Переходим на вкладку Котировки->Акции')
def go_to_data2(context):
    Methods.move_mouse_to_element(context, Locators.LOCATOR_PATH2)
    Methods.screenshots(context)


@when('Переходим на вкладку Акции->Россия по "{path}"')
def go_to_data3(context, path):
    Methods.click_element(context, Locators.LOCATOR_PATH3)
    Methods.screenshots(context)


@then('Проверяем заголовок')
def check_title(context):
    Methods.check_word(context, Locators.LOCATOR_TITLE, 'Россия - акции')
    Methods.screenshots(context)


# вариант  - Словарь


dict_company = {}


@then('Собираем данные в Json 1')
def parse_date_dict(context):
    rows_company_name = Methods.check_elements(context, Locators.LOCATOR_COMPANY_NAME)
    rows_company_price = Methods.check_elements(context, Locators.LOCATOR_COMPANY_PRICE)
    for i in range(len(rows_company_price) - 1):
        company = rows_company_name[i].text
        price = rows_company_price[i].text
        dict_company.update({company: price})
    Methods.screenshots(context)


@then('Выгрузка собранных данных в JSON 1')
def parse_to_json(context):
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(dict_company, file, indent=4, ensure_ascii=False, separators=(',', ': '))
    Methods.screenshots(context)


# вариант  - ООП


@then('Собираем данные в Json 2')
def parse_date_class(context):
    Parse.parse_date_class(context)


@then('Выгрузка собранных данных в JSON 2')
def parse_to_json(context):
    Parse.parse_class_to_json(context)
    Methods.screenshots(context)


@then("Рассчет изменения цены % в большую сторону")
def increase_company_price(context):
    # продолжение следует
    Methods.screenshots(context)


@then('Закрываем сайт')
def close_site(context):
    Methods.screenshots(context)
    Browser.quit(context)


# 2 сценарий
@given('Из Json в Python')
def parse_json_python(context):
    Parse.parse_json_python(context)


@given("Открываем страницу с акциями российских кампаний")
def open_main_page(context):
    Browser.settings(context, chrome, False)
    Methods.open_page(context, Page.EQUITIES_RUSSIA.value)
    Methods.screenshots(context)
    Methods.spam(context)


@then("Собираем данные о дивидентах")
def collect_dividends_info(context):
    Parse.collect_dividends_info(context)


# 3 сценарий

@when('Переходим в форму залогинивания')
def login_form(context):
    Methods.click_element(context, Locators.LOCATOR_LOGIN_FORM)
    Methods.screenshots(context)


@then('Вводим почту "{email}"')
def input_user(context, email):
    Methods.type_text(context, Locators.LOCATOR_EMAIL, email)


@then('Вводим пароль "{password}"')
def input_password(context, password):
    Methods.type_text(context, Locators.LOCATOR_PASSWORD, password)


@then('Кнопка Войти')
def button_enter(context):
    Methods.click_element(context, Locators.LOCATOR_ENTER)
    Methods.screenshots(context)


@then('Заголовок или Предупреждение "{warn}"')
def find_warn(context, warn):
    Methods.check_word(context, Locators.LOCATOR_WARN1, warn)
    Methods.screenshots(context)
