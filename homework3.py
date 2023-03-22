# exercise 1
class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, new_temperature):
        self.__temperature = new_temperature

    def del_temp(self):
        del self.__temperature

    temperature = property(get_temp, set_temp, del_temp)


obj_1 = Celsius(0)
obj_2 = Celsius(100)
print(obj_1.temperature)
obj_1.temperature = 10
print(obj_1.temperature)
del obj_1


# exercise 2
class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def __str__(self):
        return f"hello {self.__account_name} \nyour balance is: {self.__balance} GEL"

    def get_amount(self):
        return self.__balance

    def set_amount(self, new_amount):
        self.__balance = new_amount

    def deposit(self, new_deposit):
        current_amount = int(self.__balance) + int(new_deposit)
        return f"the money has been transfered. \nyour balance amounts to {current_amount} GEL"

    def withdraw(self, with_amount):
        current_amount_ = int(self.__balance) - with_amount
        return f"the money had been succesfully withdrawn. \nyour balance amounts to {current_amount_}"


acc_1 = Bank_Account("Nana", 603)
print(acc_1)
print(acc_1.deposit(int(input("input the amount you want to deposit:"))))
print(acc_1.withdraw(int(input("input the amount you want to withdraw:"))))

# exercise 3
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)


point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.length(), "\n", point2.length())


# bonus
class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def add(self, fraction2):
        self.top = 1
        self.bottom = 2
        return

    def inverse(self):
        self.top1 = self.bottom
        self.bottom1 = self.top
        return f"{self.top1}/{self.bottom1}"


frac1 = Fraction(2, 5)
frac2 = Fraction(3, 8)
print(frac1.inverse())