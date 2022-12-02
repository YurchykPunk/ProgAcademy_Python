#=======================================
#===========Task 1======================
#=======================================
string = '123'
print(string, type(string))
string = int(string)
print(string, type(string))

#=======================================
#===========Task 2======================
#=======================================
string = '123'
print(string, type(string))
string = float(string)
print(string, type(string))

#=======================================
#===========Task 3======================
#=======================================
float = 12.345
print(float, type(float))
float = int(float)
print(float, type(float))

#=======================================
#===========Task 4======================
#=======================================
ccard_number = input('Input your credit card here:')
last_four = ccard_number[-4:]
print(last_four)
#=======================================
#===========Task 5======================
#=======================================
number = str(input('Input 3-digs number:'))
sum_of_three = int(number[0]) + int(number[1]) + int(number[2])
print(sum_of_three)

#=======================================
#===========Task 6======================
#=======================================
number = int(input('Print number here: '))
sum = int()
for i in str(number):
    sum = sum + int(i)
print(sum)

#=======================================
#===========Task 7======================
#=======================================
number = int(input('Print number here: '))
sum = int()
for i in str(number):
    sum = sum + int(i)
print(sum)

#=======================================
#===========Task 8======================
#=======================================
#Determine the number of digits in a number
number = input('Print number here: ')
print(len(number))


#=======================================
#===========Task 9======================
#=======================================
#Print the digits in reverse order
reversednumber = str(input('Print number here: '))
print(reversednumber[::-1])