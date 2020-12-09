class Company:

    def __init__(self, company_name, company_price, percent_increase = None, dividends = None):
        self.name = company_name
        self.price = company_price
        self.percent_increase = percent_increase if percent_increase else []
        self.dividends = dividends if dividends else []

    def __repr__(self):
        return f"{self.name}, {self.price}"

    def __str__(self):
        return f"{self.name}:{self.price}"

    # def change_plus_pris(self):