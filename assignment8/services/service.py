from random import random
import statistics

import repository.repo
from domain.model import Student, Discipline, Grade
from repository.repo import Repository, StudentRepository, DisciplineRepository, GradeRepository
from services.validate import ValidationService




class Service:

     def __init__(self, repo_student: StudentRepository, repo_discipline: DisciplineRepository, repo_grade: GradeRepository, validator: ValidationService):
          self.repo_student  = repo_student
          self.validator = validator
          self.repo_discipline = repo_discipline
          self.repo_grade = repo_grade
          self.repo_grade.initial_grades_list(self.repo_discipline.retrieve(), self.repo_student.retrieve())

     def create_student(self, id, name):
          student = Student(id, name)
          self.validator.validate_student(student)
          self.repo_student.create(student)

     def create_discipline(self, id, name):
          discipline = Discipline(id, name)
          self.validator.validate_discipline(discipline)
          self.repo_discipline.create(discipline)

     def retrieve_students(self):
          return self.repo_student.retrieve()

     def retrieve_disciplines(self):
          return self.repo_discipline.retrieve()

     def update_student(self, id, name):
          student = Student(id, name)
          self.repo_student.update(student)

     def update_discipline(self, id, name):
          discipline = Discipline(id, name)
          self.repo_discipline.update(discipline)

     def delete_student(self, id):
          self.repo_student.delete(id)
          self.delete_grades_if_student_deleted(id)

     def delete_discipline(self, id):
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
               raise ValueError("student not found!")
          if discipline not in disciplines:
               raise ValueError("discipline not found!")
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


     def get_average(self, student_id):
          grades = self.repo_grade.retrieve()
          counter = 0
          average = 0
          for grade in grades:
               if grade.get_student_id() == student_id:
                    counter += 1
                    average += grade.get_grade_value()
          return average//counter

     def get_average_discipline(self, discipline_id):
          grades = self.repo_grade.retrieve()
          counter = 0
          average = 0
          for grade in grades:
               if grade.get_discipline_id() == discipline_id:
                    counter += 1
                    average += grade.get_grade_value()
          return average // counter

     def failing_students(self):
          failing = []
          students = self.repo_student.retrieve()
          for student in students:
               if self.get_average(student.get_student_id()) < 5:
                    if student not in failing:
                         failing.append(student)
          return failing

     def get_student_discipline_average_pairs(self):
          pairs = []
          for student in self.repo_student.retrieve():
               for discipline in self.repo_discipline.retrieve():
                    grades = self.repo_grade.get_grades_for_student_at_discipline(student.get_student_id(), discipline.get_discipline_id())
                    if len(grades) < 1:
                         continue
                    average = statistics.mean(map(lambda grade: grade.get_grade_value(), grades))
                    pairs.append([student, discipline, average])
          return pairs

     def desc_stud(self, student_id):
          student_average_pair = []
          pairs = self.get_student_discipline_average_pairs()
          for student in self.repo_student.retrieve():
               student_averages = filter(lambda pair: pair[0] == student, pairs)
               overall_average = statistics.mean(map(lambda pair: pair[2], student_averages))
               student_average_pair.append([student, overall_average])
          return sorted(student_average_pair, key=lambda pair: pair[1], reverse=True)



     def sort_disciplines(self):
          grades = self.repo_grade.retrieve()
          disciplines = self.repo_discipline.retrieve()
          max_grade = -1










          for discipline in disciplines:
               for grade in grades:
                    if grade.get_discipline_id() == discipline.get_discipline_id():
                        if grade.get_grade_value() > max_grade:
                              max_grade = grade.get_grade_value()












          grades = self.repo_grade.retrieve()
          disciplines = self.repo_discipline.retrieve()
          new_list = [[]]
          sorted_list = [[]]
          for grade in grades:
               if grade.get_grade_value() != 0:
                    if grade.get_discipline_id() not in new_list[0]:
                         new_list.append([self.get_discipline_by_id(grade.get_discipline_id()), grade.get_grade_value()])
          sorted_list = sorted(new_list, key = lambda grade: grade.get_discipline_id(), reverse = True)
          return sorted_list


def pretty_print(lista):
     for item in lista:
          print(item)

if __name__ == "__main__":
     repo_student = StudentRepository()
     repo_discipline = DisciplineRepository()
     repo_grade = GradeRepository()
     repo_student.create(Student(-1, "John Doe"))
     repo_student.create(Student(-2, "Ioani"))
     repo_discipline.create(Discipline(-1, "Mate"))
     repo_discipline.create(Discipline(-2, "Roma"))

     validator = ValidationService()
     service = Service(repo_student, repo_discipline, repo_grade, validator)
     pretty_print(repo_grade.retrieve())
     print()
     pretty_print(service.get_student_discipline_average_pairs())






