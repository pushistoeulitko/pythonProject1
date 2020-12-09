import allure
from features.steps.Company import Company
from features.steps.brower_setting import Browser
from features.steps.Locators import Locators
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidSelectorException
import time
import json
from features.steps.my_methods import Methods
from features.steps.storage import Storage

collect_date = [] # коллекция класса
collect_date_filter = {} # список отфильтрованных кампаний (название и процент)
collect_date_filter0 =[]
company_list = [] # список кампаний
increase_prise =[] # список процентов
dict_company = {}
dict_dividends = {}


class Parse(Browser):

    def parse_date_class(self):
        rows_company_name = Methods.check_elements(self, Locators.LOCATOR_COMPANY_NAME)
        rows_company_price = Methods.check_elements(self, Locators.LOCATOR_COMPANY_PRICE)
        Methods.screenshots(self)
        for i in range(len(rows_company_price) - 1):
            company_name = rows_company_name[i].text
            company_price = rows_company_price[i].text
            comp = Company(company_name, company_price)
            collect_date.append(comp)
        return collect_date

    def increase_price(self):
        for i in range(len(collect_date) - 1):
            company_name = Storage.company_from_base[i].name
            company_price = Methods.str_to_float(self, collect_date[i].price)
            current_price = Methods.str_to_float(self, Storage.company_from_base[i].price)
            if current_price > company_price:
                percent_increase = round((current_price - company_price) / company_price * 100, 2)
                # print(f"кампания {company_name} цена ранее {before_price} цена сейчас {current_price} {percent_increase} %")
                collect_date_filter.update({company_name: percent_increase})
                #comp = Company(company_name, company_price, percent_increase)
                #collect_date_filter0.append(comp)
        print(collect_date_filter)
       # return collect_date_filter0


    def parse_dict_to_json(self):
        try:
            with open("report.json", "w", encoding="utf-8") as file:
                json.dump(collect_date_filter, file, indent=4, ensure_ascii=False, separators=(',', ': '))
        except IOError as e:
            print(e)
            assert False

    def parse_class_to_json(self):

        try:
            for obj in collect_date:
                dict_company.update({obj.name: obj.price})
            with open("report.json", "w", encoding="utf-8") as file:
                json.dump(dict_company, file, indent=4, ensure_ascii=False, separators=(',', ': '))
            print('Выгрузились собранные данные в JSON')
        except IOError as e:
            print(e)
            assert False

    def parse_json_python(self):

        try:
            json_file = 'report.json'
            with open(json_file, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for i in data.keys():
                    company_list.append(i)
            print('Выгрузились из JSON в Python')
        except IOError as e:
            print(e)
            assert False

    def collect_dividends_info(self):

        for i in range(len(company_list) - 1):
            Methods.spam3(self)
            path = Locators.LOCATOR_NAME_DIVIDENTS + f'"{company_list[i]}"]'
            Methods.click_element(self, path)
            dividends = Methods.get_text(self, Locators.LOCATOR_DIVIDENTS)
            dict_dividends.update({company_list[i]: dividends})
            Methods.screenshots(self)
            self.driver.back()
        print(dict_dividends)
        return dict_dividends
