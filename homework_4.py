# exercise 1
class People:
    """this class contains information regarding persons names and surnames
    and generates their respective email addresses"""

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_mail(self):
        return f"{self.firstname}.{self.lastname}.school@edu.ge"


class Lecturer(People):
    """this class contains information regarding lecturers' names,
   lastname and salaries and generates their respective email addresses """

    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_mail(self):
        return f"{self.firstname}.{self.lastname}@edu.ge"


class Student(People):
    """this class contains information regarding students' names, lastnames
    and courses and generates their respective email addresses"""

    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_mail(self):
        return f"{self.firstname}.{self.lastname}.1@edu.ge"


person_1 = People("nino", "jinjolava")
person_2 = Lecturer("nini", "kvinikadze", 1000)
person_3 = Student("nana", "jinjolava", ['mathematics', 'literature', 'foreign language'])
print(person_1.get_mail(), '\n', person_2.get_mail(), '\n', person_3.get_mail())


# exercise 2
class Libraryitem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == 'available':
            return "the booking of the item has been completed"
        elif self.status == 'occupied':
            return "the item has already been occupied"


class Book(Libraryitem):
    def __init__(self, title, subject, status, ISBN, authors):
        super().__init__(title, subject, status)
        self.ISBN = ISBN
        self.authors = authors

    def booking(self):
        if self.status == 'available':
            return "the booking of this book has been completed"
        elif self.status == 'occupied':
            return "this book has already been occupied"


class Magazine(Libraryitem):
    def __init__(self, status, journalname, volume, subject=None, title=None):
        super().__init__(title, subject, status)
        self.journalname = journalname
        self.volume = volume

    def booking(self):
        if self.status == "available":
            return "the booking of this magazine has been completed"
        elif self.status == "occupied":
            return "this magazine has already been occupied"


class CD(Libraryitem):
    def __init__(self, title, status, subject=None):
        super().__init__(title, status, subject)

    def booking(self):
        return "booking is impossible"


item1 = Magazine("occupied", "vogue", 15)
item2 = CD("elvis presley", "occupied")
item3 = Book("mo dao zhu shi", "historical fantasy world", "available", 1442324, "Mo Xiang Tong Xiu")
print(item1.booking(), '\n', item2.booking(), '\n', item3.booking())


# exercise 3
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"individual {self.firstname} {self.lastname}'s age is {self.age}"


class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def hourly_salary(self):
        return self.monthly_salary / self.working_hours

    def perform_operation(self, ability):
        if ability == 'able':
            return "is able to perform operations"
        elif ability == 'unable':
            return "is unable to perform operation"


class Doctor(Employee, Person):
    pass


proffesional_1 = Doctor('neurosurgeon', 10000, 16)
print(proffesional_1.hourly_salary())
print(proffesional_1.working_hours, '\n', proffesional_1.monthly_salary)
