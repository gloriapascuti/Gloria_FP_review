import unittest

from domain.model import Student, Discipline, Grade
from errors.exceptions import ValidError
from repository.repo import StudentRepository, DisciplineRepository, GradeRepository
from services.service import Service
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


class TestService(unittest.TestCase):

    def test_create_student(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.create_student(6, "Maria")
        students = repo_student.retrieve()
        self.assertEqual(students[-1].get_student_id(), 6)
        self.assertEqual(students[-1].get_name(), "Maria")

    def test_create_discipline(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.create_discipline(5, "Engleza")
        disciplines = repo_discipline.retrieve()
        self.assertEqual(disciplines[-1].get_discipline_id(), 5)
        self.assertEqual(disciplines[-1].get_name(), "Engleza")

    def test_retrieve_students(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        students = repo_student.retrieve()
        self.assertEqual(students[0].get_student_id(), 1)
        self.assertEqual(students[0].get_name(), "Dan")

    def test_retrieve_disciplines(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        disciplines = repo_discipline.retrieve()
        self.assertEqual(disciplines[0].get_discipline_id(), 1)
        self.assertEqual(disciplines[0].get_name(), "Mate")

    def test_update_student(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.update_student(5, "Marcus")
        students = service.retrieve_students()
        self.assertEqual(students[-1].get_name(), "Marcus")

    def test_update_discipline(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.update_discipline(4, "Stiinte")
        disciplines = service.retrieve_disciplines()
        self.assertEqual(disciplines[-1].get_name(), "Stiinte")

    def test_delete_student(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.delete_student(5)
        students = service.retrieve_students()
        self.assertEqual(students[-1].get_student_id(), 4)
        self.assertEqual(students[-1].get_name(), "Vlad")

    def test_delete_discipline(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.delete_discipline(4)
        disciplines = service.retrieve_disciplines()
        self.assertEqual(disciplines[-1].get_discipline_id(), 3)
        self.assertEqual(disciplines[-1].get_name(), "Istorie")

    def test_get_student_by_id(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        student = service.get_student_by_id(1)
        self.assertEqual(student.get_student_id(), 1)
        self.assertEqual(student.get_name(), "Dan")

    def test_get_discipline_by_id(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        discipline = service.get_discipline_by_id(1)
        self.assertEqual(discipline.get_discipline_id(), 1)
        self.assertEqual(discipline.get_name(), "Mate")

    def test_get_student_by_name(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        student = service.get_student_by_name("Dan")
        self.assertEqual(student[0].get_student_id(), 1)
        self.assertEqual(student[0].get_name(), "Dan")

    def test_get_discipline_by_name(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        discipline = service.get_discipline_by_name("Mate")
        self.assertEqual(discipline[0].get_discipline_id(), 1)
        self.assertEqual(discipline[0].get_name(), "Mate")

    def test_create_grade(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.create_grade(4, 5, 9)
        grades = service.repo_grade.retrieve()
        added_grade = grades[-1]
        self.assertEqual(len(grades), 17)

    def test_retrieve_grades(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        grades = service.retrieve_grades()
        self.assertEqual(grades[0].get_student_id(), 1)
        self.assertEqual(grades[0].get_discipline_id(), 1)
        self.assertEqual(grades[0].get_grade_value(), 6)

    def test_delete_grade_if_student_deleted(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.delete_student(2)
        grades = repo_grade.retrieve()
        self.assertEqual(grades[-1].get_student_id(), 4)
        self.assertEqual(grades[-1].get_discipline_id(), 4)
        self.assertEqual(grades[-1].get_grade_value(), 9)

    def test_delete_grades_if_discipline_deleted(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        service.delete_discipline(4)
        grades = repo_grade.retrieve()
        self.assertEqual(grades[-1].get_discipline_id(), 3)
        self.assertEqual(grades[-1].get_student_id(), 2)
        self.assertEqual(grades[-1].get_grade_value(), 6)

    def test_get_student_discipline_average_pairs(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        pairs = service.get_student_discipline_average_pairs()
        pair = pairs[0]
        self.assertEqual(pair[0].get_student_id(), 1)
        self.assertEqual(pair[0].get_name(), "Dan")
        self.assertEqual(pair[1].get_discipline_id(), 1)
        self.assertEqual(pair[1].get_name(), "Mate")
        self.assertEqual(pair[2], 7.5)

    def test_desc_stud(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        stud = service.desc_stud()
        pair = stud[0]
        self.assertEqual(pair[1], 8.5)
        self.assertEqual(pair[0].get_student_id(), 1)
        self.assertEqual(pair[0].get_name(), "Dan")

    def test_failing_students(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        students_failing = service.failing_students()
        self.assertEqual(students_failing[0].get_name(), "Maria")
        self.assertEqual(students_failing[0].get_student_id(), 2)

    def test_desc_disciplines(self):
        repo_student = StudentRepository(default_students)
        repo_discipline = DisciplineRepository(default_disciplines)
        repo_grade = GradeRepository(default_grades)
        validator = ValidationService()
        service = Service(repo_student, repo_discipline, repo_grade, validator)
        desc_disciplines = service.desc_disciplines()
        discip = desc_disciplines[0]
        self.assertEqual(discip[0].get_name(), "Romana")
        self.assertEqual(discip[0].get_discipline_id(), 2)
        self.assertEqual(discip[1], 9.5)






if __name__ == "__main__":
    unittest.main()
