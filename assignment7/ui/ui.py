from services.service import Service


class UI:

    def __init__(self, service: Service):
        self.service = service

    def add_expense(self):
        print("Add a new expense:")
        day = int(input("~ day: "))
        amount_of_money = int(input("~ amount of money: "))
        type = input("~ type: ")
        self.service.create(day, amount_of_money, type)

    def list_expenses(self):
        for expense in self.service.retrieve():
            print(f"({expense}), ", end="")
        print()

    def filter_expenses(self):
        amount_of_money = int(input("minimum amount of money: "))
        self.service.filter(amount_of_money)

    def undo(self):
        self.service.undo()

    def change_repo(self):
        repo_type = input("choose a repo type: (memory, text, binary, json or xml)")
        self.service.set_repo(repo_type)

    def run(self):
        print("Manage expenses\n"
              "add: you will be able to add a new expense\n"
              "list: see the list of expenses\n"
              "filter: filter your list of expenses\n"
              "undo\n"
              "repo\n"
              "exit or x: exit the program")
        while True:
            try:
                option = input("Enter your choice:")
                option = option.strip()
                if option == "":
                    continue
                elif option == "add" or option == "1":
                        self.add_expense()
                elif option == "list" or option == "2":
                    self.list_expenses()
                elif option == "filter" or option == "3":
                    self.filter_expenses()
                elif option == "undo" or option == "4":
                    self.undo()
                elif option == "repo":
                    self.change_repo()
                elif option == "exit" or option == "x":
                    print("goodbye!")
                    break
                else:
                    print("invalid input!")
            except ValueError as ve:
                print(ve)




