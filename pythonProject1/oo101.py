class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def add_one(self, x):
         return x + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.name

    def bark(self):
        print("bark")

d = Dog("Tim", 34)
print(d.get_name())
d2 = Dog("Bill, 12")
print(d2.get_name())