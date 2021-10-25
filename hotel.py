from employee import Employee
from visit import Visit


class Hotel:
    __name: str
    __employees: [Employee]
    __visits: [Visit]

    def __init__(self, name: str):
        self.__name = name
        self.__employees = []
        self.__visits = []

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def hireEmployee(self, employee: Employee):
        self.__employees.append(employee)

    def getEmployees(self) -> [Employee]:
        return self.__employees

    def addVisit(self, visit: Visit) -> None:
        self.__visits.append(visit)