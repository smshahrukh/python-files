
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

s = (a+b+c)/2;
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5;
print('The area of the triangle is %0.2f' %area)
