from domain.model import Expense


class ValidationService:

    def validate_expense(self, expense: Expense):
        """
        function that validates an expense, by checking every single component
        :param expense: an expense of type Expense
        :return: -
        :raises: ValueError is there are any errors:
                    - "invalid day!\n", if the day is not in between 1 and 30
                    - "invalid amount of money!\n", if the amount of money is a negative number
                    - "invalid type!", if the type of the expense is not an integer
        """
        errors = ""
        if expense.get_day() < 1 or expense.get_day() > 30:
            errors += "invalid day!\n"
        if expense.get_amount_of_money() < 0:
            errors += "invalid amount of money!\n"
        if not isinstance(expense.get_type(), str) or expense.get_type() == "":
            errors += "invalid type!"
        if len(errors) > 0:
            raise ValueError(errors)


if __name__ == "__main__":
    expense = Expense(0, -20, 4)
    validation_service = ValidationService()
    try:
        validation_service.validate_expense(expense)
    except ValueError as ve:
        print(ve)

