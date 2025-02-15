class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
p1= Person("Abigael", 22)
p1.set_age(20)
print(p1.get_age())
p1.set_name("Abigael")
print(p1.get_name())
p1.__name = "Joy"



