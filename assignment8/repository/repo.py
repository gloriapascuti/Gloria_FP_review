import copy
import random

from domain.model import Student, Discipline, Grade
from errors.exceptions import ValidError


def initial_students_list() -> [Student]:
    students = []
    for _ in range(21):
        while True:
            student_id = random.randint(1, 500)
            random_names = ["John", "Alex", "Jonathan", "Anna", "Marie", "Elizabeth"]
            name = random.choice(random_names)
            student = Student(student_id, name)
            if student not in students:
                students.append(student)
                break
    return students


def initial_disciplines_list() -> [Discipline]:
    disciplines = []
    for _ in range(21):
        while True:
            discipline_id = random.randint(1, 500)
            random_names = ["Math", "Computer Science", "Literature", "Music", "PE", ]
            name = random.choice(random_names)
            discipline = Discipline(discipline_id, name)
            if discipline not in disciplines:
                disciplines.append(discipline)
                break
    return disciplines


class Repository:

    def __init__(self):
        pass

    def create(self, other):
        pass

    def retrieve(self):
        pass

    def update(self, other):
        pass

    def delete(self, other):
        pass

    def set_new(self, other):
        pass

    def get_by_id(self, other):
        pass

    def get_by_name(self, other):
        pass


class StudentRepository(Repository):

    def __init__(self, default_students=None):
        super().__init__()
        if default_students is None:
            self.students: [Student] = initial_students_list()
        else:
            self.students = default_students[:]

    def create(self, student):
        if student in self.students:
            raise ValidError("already existing student with same id!")
        self.students.append(student)

    def retrieve(self):
        return copy.deepcopy(self.students)

    def update(self, updated_student):
        stud_index = None
        for index, stud in enumerate(self.students):
            if stud == updated_student:
                stud_index = index
                break
        if stud_index is None:
            raise ValidError("student not found!")
        self.students[stud_index] = updated_student

    def delete(self, removed_student_id):
        # stud_index = None
        # for index, stud in enumerate(self.students):
        #     if stud.get_student_id() == removed_student_id:
        #         stud_index = index
        #         break
        # if stud_index is None:
        #     raise ValueError("student not found!")
        # self.students.pop(stud_index)
        student = self.get_by_id(removed_student_id)
        if student is None:
            raise ValidError("student not found!")
        self.students.remove(student)

    def get_by_id(self, id: int):
        student = None
        for stud in self.students:
            if stud.get_student_id() == id:
                student = stud
                break
        if student is None:
            raise ValidError("student id not found!")
        return student

    def get_by_name(self, name: str):
        students = []
        for stud in self.students:
            to_cmp = stud.get_name()
            if to_cmp.lower() == name.lower() and to_cmp.upper() == name.upper():
                students.append(stud)
        if not students:
            raise ValidError("student name not found!")
        return students


class DisciplineRepository(Repository):

    def __init__(self, default_disciplines=None):
        super().__init__()
        if default_disciplines is None:
            self.disciplines: [Discipline] = initial_disciplines_list()
        else:
            self.disciplines = default_disciplines[:]

    def create(self, discipline):
        if discipline in self.disciplines:
            raise ValidError("already existing discipline!")
        self.disciplines.append(discipline)

    def retrieve(self):
        return copy.deepcopy(self.disciplines)

    def update(self, updated_discipline):
        discip_index = None
        for index, discip in enumerate(self.disciplines):
            if discip == updated_discipline:
                discip_index = index
                break
        if discip_index is None:
            raise ValidError("discipline not found!")
        self.disciplines[discip_index] = updated_discipline

    def delete(self, removed_discipline_id):
        discipline = self.get_by_id(removed_discipline_id)
        if discipline is None:
            raise ValidError("student not found!")
        self.disciplines.remove(discipline)

    def get_by_id(self, id):
        discipline = None
        for discip in self.disciplines:
            if discip.get_discipline_id() == id:
                discipline = discip
                break
        if discipline is None:
            raise ValidError("discipline id not found!")
        return discipline

    def get_by_name(self, name: str):
        disciplines = []
        for discip in self.disciplines:
            name_cmp = discip.get_name()
            if name_cmp.lower() == name.lower() and name_cmp.upper() == name.upper():
                disciplines.append(discip)
        if not disciplines:
            raise ValidError("discipline name not found!")
        return disciplines


class GradeRepository(Repository):

    def __init__(self, default_grades=None):
        super().__init__()
        if default_grades is not None:
            self.grades = default_grades[:]
        else:
            self.grades = []

    def initial_grades_list(self, disciplines, students) -> [Grade]:
        for j in range(21):
            for _ in range(3):
                discipline_id = disciplines[random.randint(1, 20)].get_discipline_id()
                student_id = students[j].get_student_id()
                value_grade = random.randint(1, 10)
                grade = Grade(discipline_id, student_id, value_grade)
                self.grades.append(grade)

    def create(self, grade: Grade):
        # if self.student.get_by_id(student_id) not in self.students:
        #     raise ValueError("student not found!")
        # if self.discipline.get_by_id(discipline_id) not in self.disciplines:
        #     raise ValueError("discipline not found!")
        self.grades.append(grade)

    def retrieve(self):
        return copy.deepcopy(self.grades)

    def get_grades_for_student_at_discipline(self, student_id, discipline_id):
        return list(
            filter(lambda grade: grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id,
                   self.grades))

    def get_grades_for_discipline(self, discipline_id):
        return list(filter(lambda grade: grade.get_discipline_id() == discipline_id, self.grades))


if __name__ == "__main__":
    # students = initial_students_list()
    # disciplines = initial_disciplines_list()
    # grades = initial_grades_list(students, disciplines)
    # print(students, '\n', disciplines, '\n', grades)
    try:
        repo = StudentRepository()
        repo = StudentRepository()
        repod = DisciplineRepository()
        repo.create(Student(23, "John"))
        students = repo.retrieve()
        # students = repo.retrieve()
        # print(students)
        # students.append(Student(2, "John"))
        # print(students)
        print(repo.retrieve(), '\n')
        print(repo.update(Student(23, "Jane")))
        print(repo.retrieve(), '\n')
        repod.create(Discipline(23, "Math"))
        print(repod.retrieve(), '\n')
        # repoo.get_student_by_id()
        # repog = GradeRepository(repo, repod)
        # grades = repog.retrieve()
        # print(grades, '\n')
        # repog.create(Grade(23, 23, 9.5))
        # print(repog.retrieve())
        print(repo.get_by_id(23), '\n')
        print(repo.get_by_name("jane"))
        # repo.delete(Student(23, "John"))
        # print(repo.retrieve(), '\n')
        # repog.delete(23)
        # print(repog.retrieve(), '\n')
        print(repod.get_by_id(23))
        print(repod.get_by_name("Math"))

    except ValidError as ve:
        print(ve)
