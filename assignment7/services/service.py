from domain.model import Expense
from repository.repo import Repository, MemoryRepository, BinaryFileRepository, TextFileRepository, JSONFileRepository, \
    XMLFileRepository
from services.validate import ValidationService

REPO_CHOICES = {
    "memory": MemoryRepository,
    "text": TextFileRepository,
    "binary": BinaryFileRepository,
    "json": JSONFileRepository,
    "xml": XMLFileRepository,
}


class Service:

    def __init__(self, repo: Repository, validator: ValidationService):
        self.validator = validator
        self.repo = repo
        self.list_of_undos: [[Expense]] = [repo.retrieve()]

    def add_to_list_of_undos(self):
        expenses = self.repo.retrieve()
        self.list_of_undos.append(expenses)

    def create(self, day, amount_of_money, type):
        """
        function that adds to the list a new element, after validating it. The create function from Service is "talking" to the create function from Repository.
        :param day: the date as an integer
        :param amount_of_money: the amount of money as an integer
        :param type: the type of expence as a string
        :return: -
        """
        expense = Expense(day, amount_of_money, type)
        self.validator.validate_expense(expense)
        self.repo.create(expense)
        self.add_to_list_of_undos()

    def retrieve(self):
        return self.repo.retrieve()

    def filter(self, value):
        expenses = self.repo.retrieve()
        filtered_expenses = list(filter(lambda expense: expense.get_amount_of_money() > value, expenses))
        self.repo.set_expenses(filtered_expenses)
        self.add_to_list_of_undos()

    def undo(self):
        if len(self.list_of_undos) <=1:
            raise ValueError("no more undos!")
        self.list_of_undos.pop()
        self.repo.set_expenses(self.list_of_undos[-1])

    def set_repo(self, repo_type):
        repo = REPO_CHOICES[repo_type]()
        expenses = self.repo.retrieve()
        repo.set_expenses(expenses)
        self.repo = repo
