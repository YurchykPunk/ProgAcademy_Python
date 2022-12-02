#=======================================
#===========Task 1======================
#=======================================
print('Hello world')


#=======================================
#===========Task 2======================
#=======================================
print('-Hello Python')
print('-Hello, dear user')
print('-OMG are you alive?')

#=======================================
#===========Task 3======================
#=======================================
lenght = int(input('Input rectangle lenght: '))
width = int(input('Input rectangle width: '))
area = lenght * width
print('The area of your rectangle is:' ,area)

#=======================================
#===========Task 4======================
#=======================================
number_a = int(input('Input any int number a: '))
number_b = int(input('Input any int number b: '))

sum = number_a + number_b
product = number_a * number_b
difference = number_a - number_b
quotient = number_a / number_b

print('Sum (a+b):' , sum)
print('Product (a*b):' , product)
print('Difference (a-b):' , difference)
print('Quotient (a/b):' , quotient)

#=======================================
#===========Task 5======================
#=======================================
#diameter, circumference and area
pi_number = float(3.14159)

radius = int(input('Left the radius of the circle here:'))

diameter = radius * 2
circumference = 2 * pi_number * radius
area = pi_number * (radius ** 2)

print('Diameter:' , diameter)
print('Circumference:' , circumference)
print('Area:' , area)