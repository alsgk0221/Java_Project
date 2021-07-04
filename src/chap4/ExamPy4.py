class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("%s가 움직인다."%self.name)


class Bird(Animal):
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

    def legsNum(self):
        print("다리 개수", self.legs)


b1 = Bird("참새", 2)
print(b1.name)
