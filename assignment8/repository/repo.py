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
        """
        we defined create, a CRUD function, which we will override more specific
        :param other: a type, either Student or Discipline
        :return: -
        """
        pass

    def retrieve(self):
        """
        we defined retrieve, a CRUD function, which we will override more specific
        :param other: a type, either Student or Discipline
        :return: -
        """
        pass

    def update(self, other):
        """
        we defined update, a CRUD function, which we will override more specific
        :param other: a type, either Student or Discipline
        :return: -
        """
        pass

    def delete(self, other):
        """
        we defined delete, a CRUD function, which we will override more specific
        :param other: a type, either Student or Discipline
        :return: -
        """
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
        """
        the function defined in the Repository class, we have overridden it here especially for the StudentRepository class
        - it will first check if the student is already existing, if not a new student will be added
        :param student: a student of type Student
        :return: -
        :raises: ValidError as string: - "already existing student with same id!", if the student is already existing
        """
        if student in self.students:
            raise ValidError("already existing student with same id!")
        self.students.append(student)

    def retrieve(self):
        """
        the function defined in the Repository class, we have overridden it here especially for the StudentRepository class
        :return: a deepcopy of the lists of students
        """
        return copy.deepcopy(self.students)

    def update(self, updated_student):
        """
        the function defined in the Repository class, we have overridden it here especially for the StudentRepository class
        - first we find the index on which updated student is situated
        - after finding it, it will be used to update the name of the student by setting the whole student at that index with the updated_student
        - if the index remains none, we will catch that with ValidError and a specific message
        :param updated_student: a student of type Student, with the ID and new name
        :return: -
        :raises: ValidError as a string: -"student not found!", if it doesn't find student with the same ID
        """
        stud_index = None
        for index, stud in enumerate(self.students):
            if stud == updated_student:
                stud_index = index
                break
        if stud_index is None:
            raise ValidError("student not found!")
        self.students[stud_index] = updated_student

    def delete(self, removed_student_id):
        """
        the function defined in the Repository class, we have overridden it here especially for the StudentRepository class
        - it will first check if there exists a student with that ID
        - if it does, the student will be deleted
        - if it doesn't, we will catch that with ValidError, and a specific message
        :param removed_student_id: a student's ID
        :return: -
        :raises: ValidError as string: - "student not found!", if it doesn't find student with the same ID
        """
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
            if name.lower() in to_cmp.lower():
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
        """
        the function defined in the Repository class, we have overridden it here especially for the DisciplineRepository class
        - it will first check if the discipline is already existing, if not a new discipline will be added
        :param discipline: a discipline of type Discipline
        :return: -
        :raises: ValidError as string: - "already existing discipline with same id!", if the discipline is already existing
        """
        if discipline in self.disciplines:
            raise ValidError("already existing discipline with the same id!")
        self.disciplines.append(discipline)

    def retrieve(self):
        """
        the function defined in the Repository class, we have overridden it here especially for the DisciplineRepository class
        :return: a deepcopy of the lists of disciplines
        """
        return copy.deepcopy(self.disciplines)

    def update(self, updated_discipline):
        """
        the function defined in the Repository class, we have overridden it here especially for the DisciplineRepository class
        - first we find the index on which updated discipline is situated
        - after finding it, it will be used to update the name of the discipline by setting the whole discipline at that index with the updated_discipline
        - if the index remains none, we will catch that with ValidError and a specific message
        :param updated_discipline: a discipline of type Discipline, with the ID and new name
        :return: -
        :raises: ValidError as a string: -"discipline not found!", if it doesn't find discipline with the same ID
        """
        discip_index = None
        for index, discip in enumerate(self.disciplines):
            if discip == updated_discipline:
                discip_index = index
                break
        if discip_index is None:
            raise ValidError("discipline not found!")
        self.disciplines[discip_index] = updated_discipline

    def delete(self, removed_discipline_id):
        """
        the function defined in the Repository class, we have overridden it here especially for the DisciplineRepository class
        - it will first check if there exists a discipline with that ID
        - if it does, the discipline will be deleted
        - if it doesn't, we will catch that with ValidError, and a specific message
        :param removed_discipline_id: a student's ID
        :return: -
        :raises: ValidError as string: - "discipline not found!", if it doesn't find discipline with the same ID
        """
        discipline = self.get_by_id(removed_discipline_id)
        if discipline is None:
            raise ValidError("discipline not found!")
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
            if name.lower() in name_cmp.lower():
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
                discipline_id = disciplines[random.randint(1, len(disciplines)-1)].get_discipline_id()
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
