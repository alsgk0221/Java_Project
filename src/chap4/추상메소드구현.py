import math


class Shape:
    def __init__(self):
        self.name = "모양"

    def area(self):
        raise NotImplementedError("이것은 추상메소드입니다. ")

    def perimeter(self):
        raise NotImplementedError("이것은 추상메소드입니다. ")


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "사각형"

    def area(self):
        print("넓이 : %s " % self.name)
        return self.w*self.h

    def perimeter(self):
        print("둘레 : %s " % self.name)
        return 2*(self.w+self.h)


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
        self.name = "원"

    def area(self):
        print("넓이 : %s " % self.name)
        return math.pi*self.r*self.r

    def perimeter(self):
        print("둘레 : %s " % self.name)
        return 2*math.pi*self.r


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.name = "삼각형"

    def area(self):
        print("넓이 : %s " % self.name)
        return 0.5*math.fabs((self.x1*self.y2+self.x2*self.y3+self.x3*self.y1)-(self.x1*self.y3+self.x3*self.y2+self.x2*self.y1))

    def perimeter(self):
        print("둘레 : %s " % self.name)
        return math.sqrt((self.x1-self.x2)*(self.x1-self.x2)+(self.y1-self.y2)*(self.y1-self.y2))+math.sqrt((self.x2-self.x3)*(self.x2-self.x3)+(self.y2-self.y3)*(self.y2-self.y3))+math.sqrt((self.x3-self.x1)*(self.x3-self.x1)+(self.y3-self.y1)*(self.y3-self.y1))


r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())

r2 = Circle(10)
print(r2.area())
print(r2.perimeter())

r3 = Triangle(10, 10, 20, 20, 20, 10)
print(r3.area())
print(r3.perimeter())

