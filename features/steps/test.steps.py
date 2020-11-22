from behave import *
from selenium.webdriver import chrome, firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure_behave.hooks import allure_report
import json
from features.steps.brower_setting import Browser
from features.steps.my_methods import Methods


@given('Открываем сайт')
def open_main_page(context):
    Browser.settings(context, chrome, False)
    Methods.open_main_page(context)


@when('Переходим на вкладку Котировки->Акции->Россия')
def go_to_date1(context):
    Methods.move_mouse_to_element(context, "//*[@id='navMenu']/ul/li[1]/a")  # Котировки
    Methods.move_mouse_to_element(context, "//*[@id='navMenu']/ul/li[1]/ul/li[4]")  # Акции
    Methods.click_element(context, "//*[@id='navMenu']/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a")  # Россия


@then('Проверяем заголовок')
def check_title(context):
    try:
        path = "//*[@id='leftColumn']/h1"
        # print(context.driver.find_element_by_xpath(path).text)
        assert 'Россия - акции' in context.driver.find_element_by_xpath(path).text
        print('Заголовок Россия – акции присутствует по Xpath ' + path)
    except Exception as e:
        print('Заголовок Россия – акции отсутствует', format(e))


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


@then('Выгрузка собранных данных в JSON 1')
def parse_to_json(context):
    with open("report.json", "w", encoding="utf-8") as write_file:
        json.dump(dict_company, write_file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


# вариант  - ООП

class CollectDateUnsorted:

    def __init__(self, company, price):
        self.company = company
        self.price = price

    def __str__(self):
        company_prise = []
        for company in self.company:
            company_prise.append(company)
            for price in self.price:
                company_prise.append(price)
        return f"{company_prise}"

    # def change_plus_pris(self):


@then('Собираем данные в Json 2')
def parse_date_class(context):
    rows_company_name = Methods.check_elements(context, "//td[@class='bold left noWrap elp plusIconTd']")
    rows_company_price = Methods.check_elements(context, "//td[3][starts-with(@class, 'pid')]")
    collect_date = []
    for i in range(len(rows_company_price) - 1):
        company = rows_company_name[i].text
        price = rows_company_price[i].text
        comp = CollectDateUnsorted(company, price)
        collect_date.append(comp)
    return collect_date


@then('Выгрузка собранных данных в JSON 2')
def parse_to_json(context):
    date = str(CollectDateUnsorted)
    with open("report.json", "w", encoding="utf-8") as write_file:
        json.dump(date, write_file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


@then('Закрываем сайт')
def close_site(context):
    Browser.quit(context)  # context.driver.close()


# 3 сценарий

@when('Переходим в форму залогинивания')
def login_form(context):
    Methods.click_element(context, "//*[@id='userAccount']/div/a[1]")


@then('Вводим почту "{email}"')
def input_user(context, email):
    Methods.type_text(context, "//*[@id='loginFormUser_email']", email)


@then('Вводим пароль "{password}"')
def input_password(context, password):
    Methods.type_text(context, "//*[@id='loginForm_password']", password)


@then('Кнопка Войти')
def button_enter(context):
    try:
        context.driver.find_element_by_xpath("//*[@id='signup']/a").click()
    except:
        context.driver.find_element_by_xpath("//*[@id='emailSigningNotify']")  # warn
