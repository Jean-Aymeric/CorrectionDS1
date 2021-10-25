class Visit:
    __startDate: str
    __endDate: str

    def __init__(self, customer, hotel):
        self.__customer = customer
        self.__hotel = hotel

    def getStartDate(self) -> str:
        return self.__startDate

    def setStartDate(self, startDate: str) -> None:
        self.__startDate = startDate

    def getEndDate(self) -> str:
        return self.__endDate

    def setEndDate(self, endDate: str) -> None:
        self.__endDate = endDate

    def getCustomer(self):
        return self.__customer

    def getHotel(self):
        return self.__hotel
