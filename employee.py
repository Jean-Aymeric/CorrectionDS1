from person import Person


class Employee(Person):
    __hireDate: str

    def __init__(self, firstname: str, lastname: str, gender: str, hireDate: str):
        Person.__init__(self, firstname, lastname, gender)
        self.__hireDate = hireDate

    def getHireDate(self):
        return self.__hireDate
