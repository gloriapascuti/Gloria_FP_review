from repository.repo import MemoryRepository
from services.service import Service
from services.validate import ValidationService
from ui.ui import UI


def main():
    repo = MemoryRepository()
    validator = ValidationService()
    service = Service(repo, validator)
    ui = UI(service)
    ui.run()


if __name__ == "__main__":
    main()
