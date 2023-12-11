from domain.model import Student, Discipline, Grade


class ValidationService:

    def validate_student(self, student: Student):
        errors = ""
        if student.get_student_id() < 1:
            errors += "invalid student id!\n"
        if len(student.get_name()) < 2:
            errors += "invalid student name!\n"
        if len(errors) > 0:
            raise ValueError(errors)

    def validate_discipline(self, discipline: Discipline):
        errors = ""
        if discipline.get_discipline_id() < 1:
            errors += "invalid discipline id!\n"
        if len(discipline.get_name()) < 2:
            errors += "invalid discipline name!\n"
        if len(errors) > 0:
            raise ValueError(errors)

    def validate_grade(self, grade: Grade):
        errors = ""
        if grade.get_student_id() < 1:
            errors += "invalid student id!\n"
        if grade.get_discipline_id() < 1:
            errors += "invalid discipline id!\n"
        if grade.get_grade_value() < 1 or grade.get_grade_value() > 10:
            errors += "invalid grade value!\n"
        if len(errors) > 0:
            raise ValueError(errors)


if __name__ == "__main__":
    student: Student = Student(-1, "")
    discipline = Discipline(0, "I")
    grade = Grade(-100, 0, 13)
    validation_service = ValidationService()
    try:
        validation_service.validate_student(student)
        validation_service.validate_discipline(discipline)
        validation_service.validate_grade(grade)
    except ValueError as ve:
        print(ve)
