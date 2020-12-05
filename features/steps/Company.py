class Company:

    def __init__(self, company_name, company_price):
        self.name = company_name
        self.price = company_price

    def __repr__(self):
        return f"{self.name}, {self.price}"

    def __str__(self):
        return f"{self.name}:{self.price}"

    # def change_plus_pris(self):