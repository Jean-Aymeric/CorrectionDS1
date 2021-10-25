from hotel import Hotel
from person import Person
from visit import Visit
from employee import Employee

pegasus = Hotel("Pegasus")
print(pegasus.getName())

kara = Person("Kara", "THRACE", "MMe")
gaius = Person("Gaïus", "BALTAR", "M")
pegasus.hireEmployee(Employee("Laura", "ROSLIN", "MMe", "18/10/04"))
print((pegasus.getEmployees())[0].getHireDate())
kara.visitHotel(pegasus, "02/12/05", "17/12/05")
print((kara.getVisit())[0].getEndDate())