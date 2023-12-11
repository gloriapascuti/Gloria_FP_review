import unittest

from domain.model import Student, Discipline, Grade
from errors.exceptions import ValidError
from repository.repo import StudentRepository, DisciplineRepository, GradeRepository
from services.validate import ValidationService


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
        repo = StudentRepository()
        repo.create(Student(501, "John"))
        student = Student(501, "John")
        self.assertEqual(len(str(student)), 22)
        students = repo.retrieve()
        added_student = students[-1]
        self.assertEqual(added_student.get_student_id(), 501)
        self.assertEqual(added_student.get_name(), "John")

    def test_retrieve(self):
        repo = StudentRepository()
        repo.create(Student(501, "John"))
        students = repo.retrieve()
        self.assertEqual(Student(501, "John"), students[-1])

    def test_update(self):
        repo = StudentRepository()
        repo.create(Student(501, "John"))
        repo.update(Student(501, "Jane"))
        students = repo.retrieve()
        student = students[-1]
        self.assertEqual(student.get_name(), "Jane")

    def test_delete(self):
        repo = StudentRepository()
        repo.create(Student(501, "John"))
        repo.create(Student(502, "Jane"))
        repo.delete(502)
        students = repo.retrieve()
        student = students[-1]
        self.assertEqual(student.get_student_id(), 501)

    def test_get_by_id(self):
        repo = StudentRepository()
        repo.create(Student(501, "John"))
        student = repo.get_by_id(501)
        self.assertEqual(student, Student(501, "John"))

    def test_get_by_name(self):
        repo = StudentRepository()
        repo.create(Student(501, "Sonia"))
        student = repo.get_by_name("SONIA")
        self.assertEqual(student, [Student(501, "Sonia")])


class TestDisciplineRepository(unittest.TestCase):

    def test_create(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        discipline = Discipline(501, "Mate")
        self.assertEqual(len(str(discipline)), 24)
        disciplines = repo.retrieve()
        added_discipline = disciplines[-1]
        self.assertEqual(added_discipline.get_discipline_id(), 501)
        self.assertEqual(added_discipline.get_name(), "Mate")

    def test_retrieve(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        disciplines = repo.retrieve()
        self.assertEqual(Discipline(501, "Mate"), disciplines[-1])

    def test_update(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        repo.update(Discipline(501, "Rom"))
        disciplines = repo.retrieve()
        discipline = disciplines[-1]
        self.assertEqual(discipline.get_name(), "Rom")

    def test_delete(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        repo.create(Discipline(502, "Rom"))
        repo.delete(502)
        disciplines = repo.retrieve()
        discipline = disciplines[-1]
        self.assertEqual(discipline.get_discipline_id(), 501)

    def test_get_by_id(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        discipline = repo.get_by_id(501)
        self.assertEqual(discipline, Discipline(501, "Mate"))

    def test_get_by_name(self):
        repo = DisciplineRepository()
        repo.create(Discipline(501, "Mate"))
        discipline = repo.get_by_name("MATE")
        self.assertEqual(discipline, [Discipline(501, "Mate")])


class TestGradeRepository(unittest.TestCase):

    def test_create(self):
        repo = GradeRepository()
        repo.create(Grade(502, 501, 10))
        grade = Grade(502, 501, 10)
        self.assertEqual(len(str(grade)), 46)
        self.assertEqual(grade.get_student_id(), 501)
        self.assertEqual(grade.get_discipline_id(), 502)
        self.assertEqual(grade.get_grade_value(), 10)

    def test_retrieve(self):
        repo = GradeRepository()
        repo.create(Grade(502, 501, 10))
        grades = repo.retrieve()
        self.assertEqual(Grade(502, 501, 10), grades[-1])

    def test_get_grades_for_student_at_discipline(self):
        repo = GradeRepository()
        repo.create(Grade(502, 501, 10))
        grades = repo.retrieve()
        pair = repo.get_grades_for_student_at_discipline(501, 502)
        grade = grades[-1]
        self.assertEqual(grade.get_student_id(), pair[0])


if __name__ == "__main__":
    unittest.main()