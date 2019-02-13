# Solve Quadaratic Equation
# ax^2 + bx + c = 0

from cmath import sqrt;

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = (b**2 - 4 * a * c)
sqrtd = sqrt(d)
numerator1 = -b + sqrtd
numerator2 = -b - sqrtd
denomenator = (2*a)
x1 = numerator1 / denomenator
x2 = numerator2 / denomenator

print("X1 = ", x1)
print("X2 = ", x2)
