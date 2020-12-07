import sqlite3 as sql
from features.steps.Company import Company


class Storage():

    def __init__(self):
        self.company_from_base = get_company_list_from_db()

    def __repr__(self):
        return f"{self.company_from_base}"


    # def write_into_file(self):
    # try:
        # with open(f"dateCompany.")


def get_company_list_from_db():
    with sql.connect("C:/Users/pushi/PycharmProjects/stocks.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        collect_company = []
        for result in cur.execute('SELECT name, price FROM stock_price'):
            company_from_base = Company(result['name'], result['price'])
            collect_company.append(company_from_base)
    return collect_company


print(Storage().__repr__())



# Предусмотреть возможность вывода размера хранилища.
# Загрузка данных из базы при инициализации класса.
# Возможность сохранения / получения данных из сценария по ключу
# Выгрузка данных в файл
