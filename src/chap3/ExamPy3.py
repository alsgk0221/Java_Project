class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getShow(self):
        return [self.__name, self.__age]

    def setShow(self, cname, cage):
        self.__name = cname
        self.__age = cage


man1 = Person("kim", 20)
man1.setShow("cha", 10)
print(man1.getShow())