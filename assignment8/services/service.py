import statistics

from domain.model import Student, Discipline, Grade
from errors.exceptions import ValidError
from repository.repo import StudentRepository, DisciplineRepository, GradeRepository
from services.validate import ValidationService


class Service:

    def __init__(self, repo_student: StudentRepository, repo_discipline: DisciplineRepository,
                 repo_grade: GradeRepository, validator: ValidationService):
        self.repo_student = repo_student
        self.validator = validator
        self.repo_discipline = repo_discipline
        self.repo_grade = repo_grade
        if not self.repo_grade.retrieve():
            self.repo_grade.initial_grades_list(self.repo_discipline.retrieve(), self.repo_student.retrieve())

    def create_student(self, id, name):
        """
        function that adds to the list a new student, after validating it. The create_student function from Service is "talking" to the create function from StudentRepository.
        :param id: the id as an integer
        :param name: the name as a string
        :return: -
        """
        student = Student(id, name)
        self.validator.validate_student(student)
        self.repo_student.create(student)

    def create_discipline(self, id, name):
        """
        function that adds to the list a new discipline, after validating it. The create_discipline function from Service is "talking" to the create function from DisciplineRepository.
        :param id: the id as an integer
        :param name: the name as a string
        :return: -
        """
        discipline = Discipline(id, name)
        self.validator.validate_discipline(discipline)
        self.repo_discipline.create(discipline)

    def retrieve_students(self):
        """
        function that returns the list of students. The retrieve_students function from Service is "talking" to the retrieve function from StudentRepository.
        :return: the list of students
        """
        return self.repo_student.retrieve()

    def retrieve_disciplines(self):
        """
        function that returns the list of disciplines. The retrieve_disciplines function from Service is "talking" to the retrieve function from DisciplineRepository.
        :return: the list of disciplines
        """
        return self.repo_discipline.retrieve()

    def update_student(self, id, name):
        """
        function that updates a students name. The update_student function from Service is "talking" to the update function from StudentRepository.
        :param id: the id as an integer
        :param name: the name as a string
        :return: -
        """
        student = Student(id, name)
        self.repo_student.update(student)

    def update_discipline(self, id, name):
        """
        function that updates a disciplines name. The update_discipline function from Service is "talking" to the update function from DisciplineRepository.
        :param id: the id as an integer
        :param name: the name as a string
        :return: -
        """
        discipline = Discipline(id, name)
        self.repo_discipline.update(discipline)

    def delete_student(self, id):
        """
        function that deletes the student with the same ID. The delete_student function from Service is "talking" to the delete function from StudentRepository.
        :param id: the id as an integer
        :return: -
        """
        self.repo_student.delete(id)
        self.delete_grades_if_student_deleted(id)

    def delete_discipline(self, id):
        """
        function that deletes the discipline with the same ID. The delete_discipline function from Service is "talking" to the delete function from DisciplineRepository.
        :param id: the id as an integer
        :return: -
        """
        self.repo_discipline.delete(id)
        self.delete_grades_if_discipline_deleted(id)

    def get_student_by_id(self, id):
        return self.repo_student.get_by_id(id)

    def get_discipline_by_id(self, id):
        return self.repo_discipline.get_by_id(id)

    def get_student_by_name(self, name):
        return self.repo_student.get_by_name(name)

    def get_discipline_by_name(self, name):
        return self.repo_discipline.get_by_name(name)

    def create_grade(self, discipline_id, student_id, grade_value):
        discipline = self.repo_discipline.get_by_id(discipline_id)
        student = self.repo_student.get_by_id(student_id)
        students = self.retrieve_students()
        disciplines = self.retrieve_disciplines()
        if student not in students:
            raise ValidError("student not found!")
        if discipline not in disciplines:
            raise ValidError("discipline not found!")
        grade = Grade(discipline_id, student_id, grade_value)
        self.validator.validate_grade(grade)
        self.repo_grade.create(grade)

    def retrieve_grades(self):
        return self.repo_grade.retrieve()

    def delete_grades_if_student_deleted(self, id):
        i = 0
        while i < len(self.repo_grade.retrieve()):
            if self.repo_grade.grades[i].get_student_id() == id:
                self.repo_grade.grades.pop(i)
            else:
                i += 1

    def delete_grades_if_discipline_deleted(self, id):
        i = 0
        while i < len(self.repo_grade.retrieve()):
            if self.repo_grade.grades[i].get_discipline_id() == id:
                self.repo_grade.grades.pop(i)
            else:
                i += 1

    # def get_average(self, student_id):
    #     grades = self.repo_grade.retrieve()
    #     counter = 0
    #     average = 0
    #     for grade in grades:
    #         if grade.get_student_id() == student_id:
    #             counter += 1
    #             average += grade.get_grade_value()
    #     return average // counter
    #
    # def get_average_discipline(self, discipline_id):
    #     grades = self.repo_grade.retrieve()
    #     counter = 0
    #     average = 0
    #     for grade in grades:
    #         if grade.get_discipline_id() == discipline_id:
    #             counter += 1
    #             average += grade.get_grade_value()
    #     return average // counter

    def get_student_discipline_average_pairs(self):
        pairs = []
        for student in self.repo_student.retrieve():
            for discipline in self.repo_discipline.retrieve():
                grades = self.repo_grade.get_grades_for_student_at_discipline(student.get_student_id(),
                                                                              discipline.get_discipline_id())
                if len(grades) < 1:
                    continue
                average = statistics.mean(map(lambda grade: grade.get_grade_value(), grades))
                pairs.append([student, discipline, average])
        return pairs

    def desc_stud(self):
        student_average_pair = []
        pairs = self.get_student_discipline_average_pairs()
        for student in self.repo_student.retrieve():
            student_averages = list(filter(lambda pair: pair[0] == student, pairs))
            if len(student_averages)<1:
                continue
            overall_average = statistics.mean(map(lambda pair: pair[2], student_averages))
            if overall_average >= 5:
                student_average_pair.append([student, overall_average])
        return sorted(student_average_pair, key=lambda pair: pair[1], reverse=True)

    def failing_students(self):
        student_failing_pair = []
        # print(self.get_student_discipline_average_pairs())
        # print()
        for student, _, average in self.get_student_discipline_average_pairs():
            if average < 5 and student not in student_failing_pair:
                student_failing_pair.append(student)
        return student_failing_pair

    def desc_disciplines(self):
        discipline_average_pairs = []
        for discipline in self.repo_discipline.retrieve():
            grades = self.repo_grade.get_grades_for_discipline(discipline.get_discipline_id())
            if len(grades) < 1:
                continue
            discipline_average = statistics.mean(map(lambda grade: grade.get_grade_value(), grades))
            discipline_average_pairs.append([discipline, discipline_average])

        return sorted(discipline_average_pairs, key=lambda pair: pair[1], reverse=True)


if __name__ == "__main__":
    pass
# repo_student = StudentRepository()
# repo_discipline = DisciplineRepository()
# repo_grade = GradeRepository()
# repo_student.create(Student(-1, "John Doe"))
# repo_student.create(Student(-2, "Ioani"))
# repo_discipline.create(Discipline(-1, "Mate"))
# repo_discipline.create(Discipline(-2, "Roma"))
#
# validator = ValidationService()
# service = Service(repo_student, repo_discipline, repo_grade, validator)
# pretty_print(repo_grade.retrieve())
# print()
# pretty_print(service.get_student_discipline_average_pairs())
