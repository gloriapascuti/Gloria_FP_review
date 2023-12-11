from errors.exceptions import ValidError
from services.service import Service


class UI:

    def __init__(self, service: Service):
        self.service = service

    def add_student(self):
        print("Add a new student:")
        student_id = int(input("- give the student's ID: "))
        name = input("- give the student's name: ")
        self.service.create_student(student_id, name)

    def add_discipline(self):
        print("Add a new discipline:")
        discipline_id = int(input("- give the discipline's ID: "))
        name = input("- give the discipline's name: ")
        self.service.create_discipline(discipline_id, name)

    def list_students(self):
        students = self.service.retrieve_students()

        if students is None:
            print("no students found!")

        else:
            for student in students:
                print(f"({student}) ", end="")
            print()


    def list_disciplines(self):
        disciplines = self.service.retrieve_disciplines()

        if disciplines is None:
            print("no disciplines found!")
        else:
            for discipline in disciplines:
                print(f"({discipline}) ", end="")
            print()

    def list_grades(self):
        grades = self.service.retrieve_grades()

        if grades is None:
            print("no grades found!")
        else:
            for grade in grades:
                print(f"({grade}) ", end="")
            print()

    def update_student(self):
        print("Enter the student you want to update: ")
        student_id = int(input("- give the student's ID: "))
        name = input("- give the student's new name: ")
        self.service.update_student(student_id, name)

    def update_discipline(self):
        print("Enter the discipline you want to update: ")
        discipline_id = int(input("- give the discipline's ID: "))
        name = input("- give the discipline's new name: ")
        self.service.update_discipline(discipline_id, name)

    def delete_student(self):
        print("Enter the student you want to delete: ")
        student_id = int(input("- give the student's ID: "))
        self.service.delete_student(student_id)

    def delete_discipline(self):
        print("Enter the discipline you want to delete: ")
        discipline_id = int(input("- give the discipline's ID: "))
        self.service.delete_discipline(discipline_id)

    def get_student_by_id(self):
        print("Enter the ID by which you want to search: ")
        student_id = int(input("- give the student's ID: "))
        print(self.service.get_student_by_id(student_id))

    def get_discipline_by_id(self):
        print("Enter the ID by which you want to search: ")
        id = int(input("- give the discipline's ID: "))
        print(self.service.get_discipline_by_id(id))

    def get_student_by_name(self):
        print("Enter the name by which you want to search: ")
        name = input("- give the student's name: ")
        print(self.service.get_student_by_name(name))

    def get_discipline_by_name(self):
        print("Enter the name by which you want to search: ")
        name = input("- give the discipline's name: ")
        print(self.service.get_discipline_by_name(name))
    def create_grade(self):
        print("Add a new grade:")
        discipline_id = int(input("Enter the discipline's id: "))
        student_id = int(input("Enter the student's id: "))
        grade_value = float(input("Enter the value of the grade: "))
        self.service.create_grade(discipline_id,student_id, grade_value)

    def failing_students(self):
        print(f"List of failing students: {self.service.failing_students()}")



    def run(self):
        print("Students Register Management:\n"
              "1. Manage students and disciplines:\n"
              "~ add: - (s)student\n"
              "       - (d)discipline\n"
              "~ retrieve: - (s)student\n"
              "            - (d)discipline\n"
              "~ update: - (s)student\n"
              "          - (d)discipline\n"
              "~ delete: - (s)student\n"
              "          - (d)discipline\n"
              "2. Manage grades:\n"
              "~ add: add grade to a student at a discipline\n"
              "3. Search for disciplines/students based on ID or name/title\n"
              "~ (s)student: - (id)ID\n"
              "              - (n)name\n"
              "~ (d)discipline: - (id)ID\n"
              "                 - (n)name\n"
              "4. See statistics:\n"
              "~ fail: students failing\n"
              "~ best: students with the best school situation\n"
              "~ all: all disciplines with grades, sorted in descending order based on average\n"
              "5. Exit")
        while True:
            try:
                option = input("Enter you choice: ")
                option = option.strip()
                if option == "1":
                    choice = input("what do you want to do:")
                    choice = choice.strip()
                    if choice == "add" or choice == "a":
                        o = input("students or disciplines? ")
                        o = o.strip()
                        if o == "s":
                            self.add_student()
                        elif o == "d":
                            self.add_discipline()
                        else:
                            print("invalid input!")
                    elif choice == "retrieve" or choice == "r":
                        o = input("students or disciplines? ")
                        o = o.strip()
                        if o == "s":
                            self.list_students()
                        elif o == "d":
                            self.list_disciplines()
                        else:
                            print("invalid input!")
                    elif choice == "update" or choice == "u":
                        o = input("students or disciplines? ")
                        o = o.strip()
                        if o == "s":
                            self.update_student()
                        elif o == "d":
                            self.update_discipline()
                        else:
                            print("invalid input!")
                    elif choice == "delete" or choice == "d":
                        o = input("students or disciplines? ")
                        o = o.strip()
                        if o == "s":
                            self.delete_student()
                        elif o == "d":
                            self.delete_discipline()
                        else:
                            print("invalid input!")
                    elif choice == "x":
                        break
                elif option == "2":
                    choice = input("what do you want to do: ")
                    choice = choice.strip()
                    if choice == "retrieve" or choice == "r":
                        self.list_grades()
                    elif choice == "add" or choice == "a":
                        self.create_grade()
                    else: print("invalid input!")
                elif option == "3":
                    choice = input("students or disciplines? ")
                    choice = choice.strip()
                    if choice == "s":
                        o = input("ID or name?")
                        o = o.strip()
                        if o == "id":
                            self.get_student_by_id()
                        elif o == "n":
                            self.get_student_by_name()
                        else: print("invalid choice!")
                    elif choice == "d":
                        o = input("ID or name?")
                        o = o.strip()
                        if o == "id":
                            self.get_discipline_by_id()
                        elif o == "n":
                            self.get_discipline_by_name()
                        else:
                            print("invalid choice!")
                    else: print("invalid choice!")
                elif option == "4":
                    choice = input("what do you want to do:")
                    choice = choice.strip()
                    if choice == "fail" or choice == "f":
                        self.failing_students()
                    elif choice == "best" or choice == "b":
                        pass
                    elif choice == "all" or choice == "a":
                        pass
                    else: print("invalid choice!")
                elif option == "5" or option == "x":
                    print("goodbye!")
                    break
                else:
                    print("invalid input!")
            except ValidError as ve:
                print(ve)




