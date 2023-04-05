# exercise 1
class Person:
    def __init__(self, name, gender, age, income):
        self.name = name
        self.gender = gender
        self.age = age
        self.income = income

    def __str__(self):
        return f"name:{self.name} \ngender: {self.gender}" \
               f" \nage: {self.age} \nincome: {self.income}"

    def monthlytax(self):
        tax = self.income * 0.2 + self.income * 0.01
        return f"tax wage is {tax}"

    def retirementmortgage(self):
        if self.gender == "male" and self.age < 30:
            ret_money = (65 - 30) * 12 * (self.income * 0.01)
            return f"retirement mortgage amounts to {ret_money}"

        elif self.gender == 'male' and self.age >= 30:
            ret_money = (65 - self.age) * 12 * (self.income * 0.01)
            return f"retirement mortgage amounts to {ret_money}"
        elif self.gender == "female" and self.age < 30:
            ret_money = (60 - 30) * 12 * (self.income * 0.01)
            return f"retirement mortgage amounts to {ret_money}"

        elif self.gender == 'female' and self.age >= 30:
            ret_money = (60 - self.age) * 12 * (self.income * 0.01)
            return f"retirement mortgage amounts to {ret_money}"


    def retirement_age(self):
        if self.gender == "male":
            return 65 - self.age

        elif self.gender == "female":
            return 60 - self.age


per_1 = Person("Nana", "female", 18, 900)
per_2 = Person("Giorgi", "male", 21, 1000)
print(per_1.__str__(), '\n', per_1.monthlytax(),
      '\n', per_1.retirementmortgage(), '\n', per_1.retirement_age())
print(per_2.__str__(), '\n', per_2.monthlytax(),
      '\n', per_2.retirementmortgage(), '\n', per_2.retirement_age())