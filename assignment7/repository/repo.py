import copy
import json
import pickle
import random
import xml.etree.ElementTree as ET

from domain.model import Expense


# repository generic
class Repository:

    def __init__(self):
        pass

    #     here we will define the CRUD functions that the service can call: create, retrieve, update, delete

    # add the expense to the list of expenses
    def create(self, expense: Expense):
        """
        we defined the create, a CRUD function, which we will override more specific
        :param expense: an Expense type
        :return: -
        """
        pass

    # return the list of expenses
    def retrieve(self):
        pass

    def set_expenses(self, new_expenses):
        pass


# in memory repository
def initialize_expenses_list() -> [Expense]:
    expenses = []
    type_values = ["water", "electricity", "gas", "phone", "WI-FI"]
    for _ in range(10):
        while True:
            day = random.randint(1, 30)
            amount_of_money = 10 * day
            type = random.choice(type_values)
            expense = Expense(day, amount_of_money, type)
            if expense not in expenses:
                expenses.append(expense)
                break
    return expenses


class MemoryRepository(Repository):

    def __init__(self):
        super().__init__()

        # initialize the expenses list
        self.expenses: [Expense] = initialize_expenses_list()

    # This will return a list with 10 randomly generated expenses

    #     were we will override the Repository methods

    def create(self, expense: Expense):
        """
        the function defined in the Repository class, we have overridden it here
        - it will first check if the expense is already existing, if not a new expense will be added
        :param expense: an expense of type Expense
        :return: -
        :raises: ValueError as string: - "existing expense!", if the value is already existing
        """
        if expense in self.expenses:
            raise ValueError("existing expense!")
        self.expenses.append(expense)

    def retrieve(self):
        return copy.deepcopy(self.expenses)

    def set_expenses(self, new_expenses):
        self.expenses = new_expenses


if __name__ == "__main__":
    repo: Repository = MemoryRepository()
    repo = MemoryRepository()
    repo.create(Expense(7, 22, "apa"))
    expenses = repo.retrieve()
    print(expenses)
    expenses.append(Expense(2, 54, "caldura"))
    print(expenses)
    print(repo.retrieve())


# file repositories
class FileRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        # print(file_name)
        self.file_name = file_name
        self.write_to_file(initialize_expenses_list())

    #     this needs to have a filename

    def read_from_file(self) -> [Expense]:
        pass

    def write_to_file(self, expenses):
        pass

    #     were we will override the Repository methods
    def retrieve(self):
        expenses = self.read_from_file()
        # return a deep copy of the expenses list
        return copy.deepcopy(expenses)

    def create(self, expense: Expense):
        """
        the function defined in the Repository class, we have overridden it here
        - it will be using read_from_file and write_from_file
        - it will first read the list of expenses from file,
         then check if the expense is already existing, if not a new expense will be added
         and written again to file
        :param expense: an expense of type Expense
        :return: -
        :raises: ValueError as string: - "existing expense!", if the value is already existing
        """
        expenses = self.read_from_file()
        if expense in expenses:
            raise ValueError("existing expense!")
        expenses.append(expense)
        self.write_to_file(expenses)

    def set_expenses(self, new_expenses):
        self.write_to_file(new_expenses)


class TextFileRepository(FileRepository):
    def __init__(self, file_name="expenses.txt"):
        # print(file_name)
        super().__init__(file_name)

    def read_from_file(self) -> [Expense]:
        expenses = []
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line:
                    expenses.append(Expense.create_expense_from_string(line.strip()))
        return expenses

    def write_to_file(self, expenses):
        with open(self.file_name, 'w') as file:
            for expense in expenses:
                file.write(f"{expense}\n")


#    here we will have the concrete implementation of the read_from_file and write_to_file methods from FileRepository

class BinaryFileRepository(FileRepository):
    def __init__(self, file_name="expenses.pkl"):
        super().__init__(file_name)

    def read_from_file(self) -> [Expense]:
        with open(self.file_name, 'rb') as file:
            return pickle.load(file)

    def write_to_file(self, expenses):
        with open(self.file_name, 'wb') as file:
            pickle.dump(expenses, file)


#    here we will have the concrete implementation of the read_from_file and write_to_file methods from FileRepository


class JSONFileRepository(FileRepository):
    def __init__(self, file_name="expenses.json"):
        super().__init__(file_name)

    def read_from_file(self) -> [Expense]:
        expenses = []
        with open(self.file_name, 'r') as file:
            for value in json.load(file):
                expenses.append(Expense(value["day"], value["amount_of_money"], value["type"]))
        return expenses

    def write_to_file(self, expenses):
        with open(self.file_name, 'w') as file:
            serialized_expenses = json.dumps(expenses, default=lambda expense: expense.__dict__)
            file.write(serialized_expenses)


#    here we will have the concrete implementation of the read_from_file and write_to_file methods from FileRepository


class XMLFileRepository(FileRepository):
    def __init__(self, file_name="expenses.xml"):
        super().__init__(file_name)

    #    here we will have the concrete implementation of the read_from_file and write_to_file methods from FileRepository

    def read_from_file(self) -> [Expense]:
        expenses = []
        tree = ET.parse(self.file_name)
        root = tree.getroot()

        for expense_element in root.findall("Expense"):
            day = int(expense_element.find("Day").text)
            amount_of_money = int(expense_element.find("AmountOfMoney").text)
            type = expense_element.find("Type").text

            expenses.append(Expense(day, amount_of_money, type))
        return expenses

    def write_to_file(self, expenses):
        root = ET.Element("Expenses")

        for expense in expenses:
            expense_element = ET.SubElement(root, "Expense")
            day_element = ET.SubElement(expense_element, "Day")
            amount_of_money_element = ET.SubElement(expense_element, "AmountOfMoney")
            type_element = ET.SubElement(expense_element, "Type")

            day_element.text = str(expense.get_day())
            amount_of_money_element.text = str(expense.get_amount_of_money())
            type_element.text = expense.get_type()

        tree = ET.ElementTree(root)
        tree.write(self.file_name)


# database repository

class DatabaseRepository(Repository):
    pass
