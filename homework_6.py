# exercise 1
class Currency:
    def __init__(self, value, unit="GEL"):
        self.value = float(value)
        self.unit = unit

    dict_ = {"1 USD": "2.54 GEL", "1 EUR": "2.79 GEL"}

    def __str__(self):
        return f"your balance is {self.value} {self.unit}"

    def changeto(self):
        if self.unit == "USD":
            x = float(self.value) * 2.54
            y = Currency(x, "GEL")
            return y.value

        elif self.unit == "EUR":
            x = float(self.value) * 2.79
            y = Currency(x, "GEL")
            return y.value

    def __add__(self, other):
        if self.unit == "GEL":
            inv = self.value + other.value
            return f"your balance is {inv} GEL"

        elif self.unit == "EUR":
            inv = self.changeto() + other.value
            return f"your balance is {inv} GEL"

        elif self.unit == "USD":
            inv = self.changeto() + other.value
            return f"your balance is {inv} GEL"

    def __mul__(self, other):
        try:
            print(self.changeto() * other.value)

        except TypeError:
            print("multiplying operation can be only done with integer or float types")

    def __gt__(self, other):
        if self.changeto() > other.value:
            return f"your savings are greater"
        else:
            return "your saving aren't greater"


ob_1 = Currency(100, "USD")
ob_2 = Currency(100, "EUR")
print(ob_1.__str__(), '\n', ob_1.changeto(),
      '\n', ob_1.__add__(ob_2), '\n', '\n', ob_1.__gt__(ob_2))

# exercise 2
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name} \n deposit: {self.deposit} \n loan: {self.loan}"


class Home:
    def __init__(self, ID, price, owner, status):
        self.ID = ID
        self.price = price
        self.owner = Person(owner)
        self.status = status

    def sell_house(self, buyer=None, amount=None):
        if buyer is not None and amount is None:
            self.owner = Person(buyer)
            inve = self.owner.deposit + self.price
            return f"current deposit is {inve} \n status of the house is sold"

        if amount is not None and buyer is not None:
            self.owner = Person(buyer)
            inve = self.owner.loan + self.price
            return f"current deposit is {inve} \n status of the house is sold with a loan"


per_1 = Person("nana", 290085)
per_2 = Person("nini", 1250, 50)
house = Home(164916, 1600000, per_1, 'on sale')
print(house.sell_house(per_2, 140000))

# exercise 3
class Plane:
    def move(self):
         print("plane can fly")

    def speed(self):
        print("it's speed is up to 900km/h")


class Bus:
    def move(self):
        print("bus can move on roads")

    def speed(self):
        print("it's speed is up to 180km/h")


pl = Plane()
bs = Bus()


def movement(obj):
    obj.move()
    obj.speed()


movement(pl)
movement(bs)
