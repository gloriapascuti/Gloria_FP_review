from domain.model import Expense
from repository.repo import MemoryRepository, Repository, TextFileRepository, BinaryFileRepository, JSONFileRepository, \
    XMLFileRepository
import unittest

from services.service import Service
from services.validate import ValidationService
from ui.ui import UI


class TestExpense(unittest.TestCase):

    def test_validation_service(self):
        correct_expense = Expense(1, 10, "apa")
        validator = ValidationService()
        validator.validate_expense(correct_expense)
        bad_expense = Expense(0, -10, 5)
        with self.assertRaises(ValueError):
            validator.validate_expense(bad_expense)

class TestAddExpense(unittest.TestCase):

    def test_add_expense_file_repository(self):

        repos_to_test = [TextFileRepository(file_name= "./test_expenses.txt"),
                      BinaryFileRepository(file_name= "./test_expenses.pkl"),
                      JSONFileRepository(file_name= "./test_expenses.json"),
                      XMLFileRepository(file_name= "./test_expenses.xml")]

        for repo in repos_to_test:
            repo.create(Expense(1, 10, "apa"))
            expenses = repo.retrieve()
            self.assertEqual(len(expenses), 11)
            added_expense = expenses[-1]
            self.assertEqual(added_expense.get_day(), 1)
            self.assertEqual(added_expense.get_amount_of_money(), 10)
            self.assertEqual(added_expense.get_type(), "apa")


    def test_create_expense_memory_repository(self):
        repo = MemoryRepository()
        repo.create(Expense(1, 10, "apa"))
        expenses = repo.retrieve()
        self.assertEqual(len(expenses), 11)
        added_expense = expenses[-1]
        self.assertEqual(added_expense.get_day(), 1)
        self.assertEqual(added_expense.get_amount_of_money(), 10)
        self.assertEqual(added_expense.get_type(), "apa")

    def test_create_expense_service(self):
        repo = MemoryRepository()
        validator = ValidationService()
        service = Service(repo, validator)
        day = 1
        amount_of_money = 10
        type = "apa"
        service.create(day, amount_of_money, type)
        self.assertEqual(len(service.retrieve()), 11)






if __name__ == "__main__":
    unittest.main()