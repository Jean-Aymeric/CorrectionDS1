from visit import Visit


class Person:
    __firstname: str
    __lastname: str
    __gender: str
    __visits: [Visit]

    def __init__(self, firstname: str, lastname: str, gender: str):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__gender = gender
        self.__visits = []

    def getFirstname(self) -> str:
        return self.__firstname

    def getLastname(self) -> str:
        return self.__lastname

    def getGender(self) -> str:
        return self.__gender

    def visitHotel(self, hotel, startDate: str, endDate: str):
        visit = Visit(self, hotel)
        visit.setStartDate(startDate)
        visit.setEndDate(endDate)
        self.__visits.append(visit)
        hotel.addVisit(visit)

    def getVisit(self) -> [Visit]:
        return self.__visits
