class Myclass:
    x=5
    y= 20
c = Myclass()
print(c.x)
print(c.y)

class Person:
    def __init__(self, name, age, height, gender):
        self.fullname = name
        self.age = age
        self.height = height
        self.gender = gender


person1 = Person("bryan", 35, 2, "male")
print(person1.fullname)
print(person1.age)
print(person1.height)
print(person1.gender)