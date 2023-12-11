class Student:

    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def __eq__(self, other_student):
        if self.get_student_id() == other_student.get_student_id():
            return True
        return False

    def __str__(self):
        return f"Student: {self.get_name()}, id: {self.get_student_id()}"

    def __repr__(self):
        return str(self)


class Discipline:

    def __init__(self, discipline_id: int, name: str):
        self.discipline_id = discipline_id
        self.name = name

    def get_discipline_id(self):
        return self.discipline_id

    def get_name(self):
        return self.name

    def __eq__(self, other_discipline):
        if self.get_discipline_id() == other_discipline.get_discipline_id():
            return True
        return False

    def __str__(self):
        return f"Discipline: {self.get_name()}, id:{self.get_discipline_id()}"

    def __repr__(self):
        return str(self)


class Grade:

    def __init__(self,  discipline_id: int, student_id: int, grade_value: float):
        self.discipline_id = discipline_id
        self.student_id = student_id
        self.grade_value = grade_value

    def get_student_id(self):
        return self.student_id

    def get_discipline_id(self):
        return self.discipline_id

    def get_grade_value(self):
        return self.grade_value

    def __str__(self):
        return f"id discipline: {self.discipline_id}, id student: {self.student_id}, grade: {self.grade_value}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    pass