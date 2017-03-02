from math import sqrt


class Triangle():

    def len_side(self, point1, point2):
        return sqrt((point1.x-point2.x)**2 + (point1.y - point2.y)**2)

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.a = float(self.len_side(self.p1, self.p2))
        self.b = float(self.len_side(self.p1, self.p3))
        self.c = float(self.len_side(self.p2, self.p3))

    def len_triangle_side(self):
        return self.a + self.b + self.c

    def half_len_triangle_side(self):
        return self.len_triangle_side()/2

    def square_triangle(self):
        p = self.half_len_triangle_side()
        return sqrt(p * (p - self.a)*(p-self.b)*(p-self.c))

    def get_height_is_a(self):
        return 2*self.square_triangle() / self.a

    def get_height_is_b(self):
        return 2 * self.square_triangle() / self.b

    def get_height_is_c(self):
        return 2 * self.square_triangle() / self.c











