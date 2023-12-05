class Expense:
    def __init__(self, day, amount_of_money, type):
        self.day = day
        self.amount_of_money = amount_of_money
        self.type = type

    def get_day(self):
        return self.day

    def get_amount_of_money(self):
        return self.amount_of_money

    def get_type(self):
        return self.type

    def __eq__(self, other_expense):
        if self.get_day() == other_expense.get_day() and self.get_amount_of_money() == other_expense.get_amount_of_money() and self.type == other_expense.get_type():
            return True
        return False

    def __str__(self):
        return f"{self.get_day()},{self.get_amount_of_money()},{self.get_type()}"

    def __repr__(self):
        return str(self)

    @staticmethod
    def create_expense_from_string(string: str):
        day, amount_of_money, type = string.split(",")
        return Expense(int(day), int(amount_of_money), type)



# class HouselyExpenses(Expense):
#
#     def __init__(self, provider, day, amount_of_money, type):
#         super().__init__(day, amount_of_money, type)
#         self.provider = provider


if __name__ == '__main__':
    exp = Expense(5, 200, 'apa')
    print(exp.__dict__)
