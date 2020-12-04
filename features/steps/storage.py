import sqlite3 as sql


with sql.connect("C:/Users/pushi/PycharmProjects/stocks.db") as conn:
    conn.row_factory = sql.Row
    cur = conn.cursor()
    for result in cur.execute('SELECT name, price FROM stock_price'):
        obj = (result['name'], result['price'])


class Storage(object):

    def __init__(self, company_list, before_prise):
        self.company = company_list
        self.beforePrise = before_prise

    def __len__(self):
        return len(self.company)

        # name
        # price

    def __str__(self):
        return f"{self.company}:{self.beforePrise}"

    # def write_into_file(self):
    # try:
    # with open(f"dateCompany.")




# Предусмотреть возможность вывода размера хранилища.
# Загрузка данных из базы при инициализации класса.
# Возможность сохранения / получения данных из сценария по ключу
# Выгрузка данных в файл
