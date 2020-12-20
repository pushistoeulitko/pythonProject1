import sqlite3 as sql
from features.steps.Company import Company
import json


def get_company_list_from_db():
    with sql.connect("C:/Users/pushi/PycharmProjects/stocks.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        collect_company = []
        for result in cur.execute('SELECT name, price FROM stock_price'):
            company_from_base = Company(result['name'], result['price'])
            collect_company.append(company_from_base)
    return collect_company


def get_company_list_from_ui():  # получаем ключи
    company_list = []
    json_file = "C:/Users/pushi/PycharmProjects/pythonProject1/report.json"
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        for i in data.keys():
            company_list.append(i)
    return company_list


def get_from_ui_dividends():   # получаем значения
    dividends = []
    price = []
    percent = []
    json_file = "C:/Users/pushi/PycharmProjects/pythonProject1/report.json"
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        for key, value in data.items():
            price.append(value['price'])
            percent.append(value['percent'])
            dividends.append(value['dividends'])

    return price, percent, dividends,


def get_from_report():   # получаем данные из final_report
    json_file = "C:/Users/pushi/PycharmProjects/pythonProject1/features/steps/final_report.json"
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        scenario1 = []
        scenario2 = []
        scenario3 = []
        for key, value in data.items():
            if "Часть 1" in key:
                name = scenario1
            if "Часть 2" in key:
                name = scenario2
            if "Часть 3" in key:
                name = scenario3
            name.append(key)
            name.append(value['status'])
            name.append(value['steps'])
            name.append(value['start'])
            name.append(value['stop'])

    return scenario1, scenario2, scenario3


class Storage:

    # Загрузка данных из базы при инициализации класса.
    company_from_base = get_company_list_from_db()
    # Возможность сохранения / получения данных из сценария по ключу
    company_list = get_company_list_from_ui()
    company_from_ui_percent_increase = get_from_ui_dividends()[0]
    company_from_ui_price = get_from_ui_dividends()[1]
    dividends = get_from_ui_dividends()[2]

    scenario1 = get_from_report()[0]
    scenario2 = get_from_report()[1]
    scenario3 = get_from_report()[2]


    def __repr__(self):
        return f"Кампании и их цена из базы: {self.company_from_base} \n " \
               f"Список кампаний чьи акции выросли: {self.company_list}\n \
               текущая цена: {self.company_from_ui_price}\n процент тзменения цены: {self.company_from_ui_percent_increase}\n  \
               дивиденды: {self.dividends}\n Тестовые сценарии: {self.scenario1}\n+{self.scenario2}\n+ {self.scenario3}\n"

    # Предусмотреть возможность вывода размера хранилища.
    def __len__(self):
        return f"Данные извлеченные из базы по кампаниям: {len(self.company_from_base)} \n" \
               f"Данные полученные с сайта (кампания/цена/процент/дивиденты)" \
               f": {len(self.company_list)}/{len(self.company_from_ui_price)}/{len(self.company_from_ui_percent_increase)}/" \
               f"{len(self.dividends)} \n"\
               f"Описание сценариев: {len(self.scenario1)}/{len(self.scenario2)}/{len(self.scenario3)}\n"\
               f"Всего значений: " \
               f"{len(self.company_from_base)+len(self.company_list)+len(self.company_from_ui_price)+len(self.company_from_ui_percent_increase)+len(self.dividends)+len(self.scenario1)+len(self.scenario2)+len(self.scenario3)}"


    #@company_from_ui_equities.setter
    #def company_from_ui_equities(self, value):
        #self.company_from_ui_equities = value


    # Выгрузка данных в файл
    # def write_into_file(self):
    # report=
    # with open("report_all.json", "w", encoding="utf-8") as file:
    # json.dump(report, file, indent=4, ensure_ascii=False, separators=(',', ': '))


if __name__ == "__main__":
    s = Storage()

print(Storage().__repr__())
#print(Storage().__len__())

#