import sqlite3 as sql
from features.steps.Company import Company
import json


class Storage:

    def __init__(self, collect_date=None, dict_dividends=None):
        self.company_from_base = get_company_list_from_db()
        self.company_from_ui_equities = collect_date if collect_date else []
        self.company_from_ui_dividends = dict_dividends if dict_dividends else []

    def __repr__(self):
        return f"{self.company_from_base} \n + {self.company_from_ui_equities} \n + {self.company_from_ui_dividends}"

    # Предусмотреть возможность вывода размера хранилища.
    def __len__(self):
        return len(self.company_from_base) + len(self.company_from_ui_equities) + len(self.company_from_ui_dividends)

    #@company_from_ui_equities.setter
    #def company_from_ui_equities(self, value):
        #self.company_from_ui_equities = value

    # Возможность сохранения / получения данных из сценария по ключу

    # Выгрузка данных в файл
    # def write_into_file(self):
    # report=
    # with open("report_all.json", "w", encoding="utf-8") as file:
    # json.dump(report, file, indent=4, ensure_ascii=False, separators=(',', ': '))


# Загрузка данных из базы при инициализации класса.
def get_company_list_from_db():
    with sql.connect("C:/Users/pushi/PycharmProjects/stocks.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        collect_company = []
        for result in cur.execute('SELECT name, price FROM stock_price'):
            company_from_base = Company(result['name'], result['price'])
            collect_company.append(company_from_base)
    return collect_company


if __name__ == "__main__":
    s = Storage()

# print(Storage().__repr__())
# print(Storage().__len__())
