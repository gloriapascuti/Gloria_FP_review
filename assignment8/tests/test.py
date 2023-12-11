import unittest

from domain.model import Student, Discipline, Grade
from errors.exceptions import ValidError
from repository.repo import StudentRepository, DisciplineRepository, GradeRepository
from services.validate import ValidationService

default_students = [
    Student(1, "Dan"),
    Student(2, "Maria"),
    Student(3, "George"),
    Student(4, "Vlad"),
    Student(5, "Sergiu"),
]

default_disciplines = [
    Discipline(1, "Mate"),
    Discipline(2, "Romana"),
    Discipline(3, "Istorie"),
    Discipline(4, "Geogra"),
]

default_grades = [
    Grade(1, 1, 6),
    Grade(1, 1, 9),
    Grade(1, 2, 2),
    Grade(1, 2, 10),
    Grade(2, 1, 10),
    Grade(2, 1, 9),
    Grade(2, 2, 9),
    Grade(2, 2, 10),
    Grade(3, 3, 3),
    Grade(3, 3, 4),
    Grade(3, 2, 2),
    Grade(3, 2, 6),
    Grade(4, 4, 6),
    Grade(4, 4, 9),
    Grade(4, 2, 7),
    Grade(4, 2, 10),
]


class TestValidation(unittest.TestCase):
    def test_validate_student(self):
        correct_student = Student(501, "John")
        validator = ValidationService()
        validator.validate_student(correct_student)
        bad_student = Student(-1, "")
        with self.assertRaises(ValidError):
            validator.validate_student(bad_student)

    def test_validate_discipline(self):
        correct_discipline = Discipline(502, "Math")
        validator = ValidationService()
        validator.validate_discipline(correct_discipline)
        bad_discipline = Discipline(-1, "")
        with self.assertRaises(ValidError):
            validator.validate_discipline(bad_discipline)

    def test_validate_grade(self):
        correct_grade = Grade(502, 501, 9.2)
        validator = ValidationService()
        validator.validate_grade(correct_grade)
        bad_grade = Grade(-1, -1, 13)
        with self.assertRaises(ValidError):
            validator.validate_grade(bad_grade)


class TestStudentRepository(unittest.TestCase):

    def test_create(self):
        repo = StudentRepository(default_students)
        repo.create(Student(501, "John"))
        students = repo.retrieve()
        added_student = students[-1]
        self.assertEqual(len(students), 6)
        self.assertEqual(added_student.get_student_id(), 501)
        self.assertEqual(added_student.get_name(), "John")

    def test_retrieve(self):
        repo = StudentRepository(default_students)
        repo.create(Student(502, "John"))
        students = repo.retrieve()
        print("------------------")
        print(students)

        self.assertEqual(len(students), 6)
        self.assertEqual(Student(502, "John"), students[-1])

    def test_update(self):
        repo = StudentRepository(default_students)
        repo.create(Student(503, "John"))
        repo.update(Student(503, "Jane"))
        students = repo.retrieve()
        student = students[-1]
        self.assertEqual(student.get_name(), "Jane")

    def test_delete(self):
        repo = StudentRepository(default_students)
        repo.create(Student(504, "John"))
        repo.create(Student(505, "Jane"))
        repo.delete(505)
        students = repo.retrieve()
        student = students[-1]
        self.assertEqual(student.get_student_id(), 504)

    def test_get_by_id(self):
        repo = StudentRepository(default_students)
        repo.create(Student(506, "John"))
        student = repo.get_by_id(506)
        self.assertEqual(student, Student(506, "John"))

    def test_get_by_name(self):
        repo = StudentRepository(default_students)
        repo.create(Student(507, "Sonia"))
        student = repo.get_by_name("SONIA")
        self.assertEqual(student, [Student(507, "Sonia")])


class TestDisciplineRepository(unittest.TestCase):

    def test_create(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Mate"))
        disciplines = repo.retrieve()
        self.assertEqual(len(disciplines), 5)
        added_discipline = disciplines[-1]
        self.assertEqual(added_discipline.get_discipline_id(), 501)
        self.assertEqual(added_discipline.get_name(), "Mate")

    def test_retrieve(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Mate"))
        disciplines = repo.retrieve()
        self.assertEqual(Discipline(501, "Mate"), disciplines[-1])

    def test_update(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Mate"))
        repo.update(Discipline(501, "Rom"))
        disciplines = repo.retrieve()
        discipline = disciplines[-1]
        self.assertEqual(discipline.get_name(), "Rom")

    def test_delete(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Mate"))
        repo.create(Discipline(502, "Rom"))
        repo.delete(502)
        disciplines = repo.retrieve()
        discipline = disciplines[-1]
        self.assertEqual(discipline.get_discipline_id(), 501)

    def test_get_by_id(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Mate"))
        discipline = repo.get_by_id(501)
        self.assertEqual(discipline, Discipline(501, "Mate"))

    def test_get_by_name(self):
        repo = DisciplineRepository(default_disciplines)
        repo.create(Discipline(501, "Matematica"))
        discipline = repo.get_by_name("MATEMATICA")
        self.assertEqual(discipline, [Discipline(501, "Matematica")])


class TestGradeRepository(unittest.TestCase):

    def test_create(self):
        repo = GradeRepository(default_grades)
        repo.create(Grade(502, 501, 10))
        grade = Grade(502, 501, 10)
        self.assertEqual(len(str(grade)), 46)
        self.assertEqual(grade.get_student_id(), 501)
        self.assertEqual(grade.get_discipline_id(), 502)
        self.assertEqual(grade.get_grade_value(), 10)

    def test_retrieve(self):
        repo = GradeRepository(default_grades)
        created_grade = Grade(502, 501, 10)
        repo.create(created_grade)
        grades = repo.retrieve()
        self.assertEqual(grades[-1].get_student_id(), created_grade.get_student_id())
        self.assertEqual(grades[-1].get_discipline_id(), created_grade.get_discipline_id())
        self.assertEqual(grades[-1].get_grade_value(), created_grade.get_grade_value())

    def test_get_grades_for_student_at_discipline(self):
        repo = GradeRepository(default_grades)
        result = repo.get_grades_for_student_at_discipline(1, 1)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].get_student_id(), 1)
        self.assertEqual(result[0].get_discipline_id(), 1)
        self.assertEqual(result[0].get_grade_value(), 6)
        self.assertEqual(result[0].get_student_id(), 1)
        self.assertEqual(result[0].get_discipline_id(), 1)
        self.assertEqual(result[1].get_grade_value(), 9)


if __name__ == "__main__":
    unittest.main()
