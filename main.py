from coordinates import Coordinates
from triangle import Triangle
from trapezoid import Isosceles
p1 = Coordinates(0, 0)
p2 = Coordinates(3, 0)
p3 = Coordinates(2, 2)


t1 = Triangle(p1, p2, p3)


print('Длинна стороны А', '%.3f' % t1.a)
print('Длинна стороны B', '%.3f' % t1.b)
print('Длинна стороны C', '%.3f' % t1.c)
print('Периметр треугольника:', '%.3f' % t1.len_triangle_side())
print('Площаль треугольника:', '%.3f' % t1.square_triangle())
print('Высота от вершины А:', '%.3f' % t1.get_height_is_a())
print('Высота от вершины B:', '%.3f' % t1.get_height_is_b())
print('Высота от вершины C:', '%.3f' % t1.get_height_is_c())



p1 = Coordinates(0, 0)
p2 = Coordinates(6, 0)
p3 = Coordinates(2, 5)
p4 = Coordinates(2, 1)
trap = Isosceles(p1, p2, p3, p4)


print(trap.a)
print(trap.b)
print(trap.c)
print(trap.d)

print(trap.check_isosceles())

print(trap.len_trapezioid_side())
print(trap.square_trapezioid())