#Q1
name = input("Enter your name")
age = input("Enter your age")

print(f"Hello {name}, your are {age} years old!")

#Q2
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter the 2nd number"))

#the sum of two value
sum = num1 + num2
#difference of two value
difference = num2 - num1
#product of two value
product = num1 * num2
#quetient of two value
qeutient = num2 / num1

#Q3
num1 = float(input("Enter the integer number"))
num2 = float(input("Enter the integer number"))
num3 = float(input("Enter the float number"))

average = (num1 + num2 + num3) / 3

#Q4
usr_input = input("Enter the number 45")

integer = int(usr_input)
float_ = float(usr_input)
string = str(usr_input)

print(type(integer))
print(type(float_))
print(type(string))

#Q5
x = 10 + 3 * 2 ** 2

'''Ther result depend on the priority list of the operator. In python priority list
**(power) is higest priority
then
*(multiplication) priority
then
+(addition) priority
'''

#Q6
num1 = input("Enter the 1st number")
num2 = input("Enter the 2nd number")
temp = num1
num1 = num2
num2 = temp
print(f"the first number {num1}, the second number {num2}")

#Q7
tem_cel = input("Enter the the temperature in Celcius")

tem_cel = float(tem_cel)
f_ren_heit_temp = (tem_cel * (9 / 5)) / 32
print(f_ren_heit_temp)

#Q8
radius = float(input("Enter the radius of area"))
Area = 3.1416 * (radius ** 2)
print(Area)

#Q9
Principle = float(input("Enter the principle"))
Rate = float(input("Enter the rate"))
Time = float(input("Enter the time"))

SI = (Principle * Rate * Time) / 100

#Q10
numeber = input("Enter the decimal number like 45.48")

int_part = int(number)
frac_part = number - int_part