from UI.ui import UI
from repository.repo import StudentRepository, DisciplineRepository, GradeRepository
from services.service import Service
from services.validate import ValidationService


def main():
    repo_student = StudentRepository()
    repo_discipline = DisciplineRepository()
    repo_grade = GradeRepository()
    validator = ValidationService()
    service = Service(repo_student, repo_discipline, repo_grade, validator)
    ui = UI(service)
    ui.run()


if __name__ == "__main__":
    main()
