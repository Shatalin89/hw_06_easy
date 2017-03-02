from math import sqrt


class Isosceles:
    def len_side(self, point1, point2):
        return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.a = self.len_side(self.p1, self.p2)
        self.b = self.len_side(self.p2, self.p3)
        self.c = self.len_side(self.p3, self.p4)
        self.d = self.len_side(self.p4, self.p1)
        if (self.a == self.c) or (self.b == self.d):
            self.isosceles_check = True
        else:
            self.isosceles_check = False


    def check_isosceles(self):
        return 'Трапеция равнобедренная' if self.isosceles_check else 'Трапеця не равносторонняя'

    def len_trapezioid_side(self):
        return self.a + self.b + self.c + self.d

    def square_trapezioid(self):
        return ((self.a + self.b) / 2) * sqrt(self.c ** 2 - (((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.b - self.a))) ** 2)

