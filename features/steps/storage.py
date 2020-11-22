import sqlite3

#with sqlite3.connect("stocks") as conn:
    #cur = conn.cursor()
    #result_company = cur.fetchall()
    #print(result_company)
    #or result_company in cur.execute("SELECT name FROM stock_price"):
        #print(result_company)


class Storage(object):

    def __init__(self, company_list, before_prise):
        self.company = company_list
        self.beforePrise = before_prise

    def __len__(self):
        return len(self.company)

        # name
        # price

# Предусмотреть возможность вывода размера хранилища.
# Загрузка данных из базы при инициализации класса.
# Возможность сохранения / получения данных из сценария по ключу
# Выгрузка данных в файл
