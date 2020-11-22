from behave import *
from selenium.webdriver import chrome, firefox
import json
from features.steps.brower_setting import Browser
from features.steps.my_methods import Methods


@given('Открываем сайт')
def open_main_page(context):
    Browser.settings(context, chrome, False)
    Methods.open_main_page(context)
    Methods.screenshots(context)
    Methods.spam(context)


@when('Переходим на вкладку Котировки')
def go_to_date1(context):
    path = "//*[@id='navMenu']/ul/li[1]/a"
    Methods.move_mouse_to_element(context, path)
    Methods.screenshots(context)


@when('Переходим на вкладку Котировки->Акции')
def go_to_date2(context):
    path = "//*[@id='navMenu']/ul/li[1]/ul/li[4]"
    Methods.move_mouse_to_element(context, path)
    Methods.screenshots(context)


@when('Переходим на вкладку Акции->Россия')
def go_to_date3(context):
    path = "//*[@id='navMenu']/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a"
    Methods.click_element(context, path)
    Methods.screenshots(context)


@then('Проверяем заголовок')
def check_title(context):
    path = "//*[@id='leftColumn']/h1"
    word = 'Россия - акции'
    Methods.check_word(context, path, word)
    Methods.screenshots(context)


# вариант  - Словарь


dict_company = {}


@then('Собираем данные в Json 1')
def parse_date_dict(context):
    rows_company_name = Methods.check_elements(context, "//td[@class='bold left noWrap elp plusIconTd']")
    rows_company_price = Methods.check_elements(context, "//td[3][starts-with(@class, 'pid')]")
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

class CollectDateUnsorted:

    def __init__(self, company, price):
        self.company = company
        self.price = price

    def __repr__(self):
        return f"{self.company}, {self.price}"

    def get_str(self):
        return f"{self.company}:{self.price}"

    # def change_plus_pris(self):


collect_date = []


@then('Собираем данные в Json 2')
def parse_date_class(context):
    rows_company_name = Methods.check_elements(context, "//td[@class='bold left noWrap elp plusIconTd']")
    rows_company_price = Methods.check_elements(context, "//td[3][starts-with(@class, 'pid')]")
    Methods.screenshots(context)
    for i in range(len(rows_company_price) - 1):
        company = rows_company_name[i].text
        price = rows_company_price[i].text
        comp = CollectDateUnsorted(company, price)
        collect_date.append(comp)
    return collect_date

@then('Выгрузка собранных данных в JSON 2')
def parse_to_json(context):
    for obj in collect_date:
        dict_company.update({obj.company: obj.price})
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(dict_company, file, indent=4, ensure_ascii=False, separators=(',', ': '))
    Methods.screenshots(context) # ничего не происходит

@then('Закрываем сайт')
def close_site(context):
    Methods.screenshots(context)
    Browser.quit(context)


# 2 сценарий
@given('Из Json в Python')
def parse_json_python(context):
    json_file = 'report.json'
    with open(json_file, 'r') as file:
        data = json.load(file)


# 3 сценарий

@when('Переходим в форму залогинивания')
def login_form(context):
    Methods.click_element(context, "//*[@id='userAccount']/div/a[1]")
    Methods.screenshots(context)

@then('Вводим почту "{email}"')
def input_user(context, email):
    Methods.type_text(context, "//*[@id='loginFormUser_email']", email)
    Methods.screenshots(context)

@then('Вводим пароль "{password}"')
def input_password(context, password):
    Methods.type_text(context, "//*[@id='loginForm_password']", password)
    Methods.screenshots(context)

@then('Кнопка Войти')
def button_enter(context):
    Methods.click_element(context, "//*[@id='signup']/a")
    Methods.screenshots(context)

@then('Заголовок или Предупреждение "{warn}"')
def find_warn(context, warn):
    path = "//*[@id='emailSigningNotify']"
    Methods.check_word(context, path, warn)
    Methods.screenshots(context)
