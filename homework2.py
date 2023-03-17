# exercise 1
class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def Perimeter(self):
        return (self.width + self.length) * 2

    def Area(self):
        return self.width * self.length

obj1 = Rectangle(5, 1, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(7, 3, "purple")
print(obj1.Area())

# exercise 2
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"the car's brand is: {self.brand} the model: {self.model}, the color: {self.color}"

car_1 = Car("Ford", "Mustang", "Red")
car_2 = Car("Toyota", "Prius", "Blue")
car_3 = Car("Volkswagen", "Golf", "Green")

print(car_1,"\n",car_2,"\n",car_3)

# exercise 3
class Dog:
    def __init__(self, breed="japanese hin", size="small", age="2 years", color="black"):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def eat(self, food):
        self.food = food
        return f"eats {self.food},"

    def sleep(self, hours):
        self.hours = hours
        return f"sleeps for {self.hours},"

    def sit(self, ability):
        self.ability = ability
        return f"is {self.ability} to sit,"

    def run(self, activity):
        self.activity = activity
        return f"runs {self.activity}"

dog_1 = Dog("Neapolitan Mastiff", "Large", "5 Years", "Black")
dog_2 = Dog("Maltese", "Small", "2 Years", "White")
dog_3 = Dog("Chow Chow", "Medium", "3 Years", "Brown")
print(dog_1.breed, dog_1.eat("in large amounts"), dog_1.sleep("12-14 hours"),\
      dog_1.sit("able"), dog_1.run("very actively"))
print(dog_2.breed, dog_2.eat("in small amounts"), dog_2.sleep("12-14 hours"),\
      dog_2.sit("unable"), dog_2.run("actively"))
print(dog_3.breed, dog_3.eat("in large amounts"), dog_3.sleep("12-16 hours"),\
      dog_3.sit("able"), dog_3.run("very actively"))