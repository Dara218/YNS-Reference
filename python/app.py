from math import *

channel = 'test LAng Po'
channelNum = 35

is_active = False
average = 3.5

# PRINT
# print('hello this is ' + channel + " in channel " + str(channelNum))
# print(channel.upper().isupper())
# print(len(channel))

# INPUT
# num1 = input('enter a number: ')
# num2 = input('enter a number: ')
# print(float(num1) + float(num2))


# price = [10, 5, 12, 20]
# fruits = ['mangga', 'santol', 'buko', 'apple', 'buko']
# fruits.extend(price)
# fruits.remove('santol')
# fruits.clear()
# fruits.reverse()
# fruits2 = fruits.copy()
# print(len(channel))


# TUPLE
# coordinates = (3, 5)
# coordinates[0] = 10
# print(testName)


# FUNCTION
# def hi():
#     print('hello world')

# hi()

# def cube(num):
#     # print(num * num * num)
#     return num * num * num

# print(cube(5))


# IF STATEMENT
# is_yellow = True
# is_soft = False

# if is_yellow and is_soft:
#     print('Hinog na')
# elif is_yellow and not(is_soft):
#     print('pahinog na')
# else:
#     print('hilaw pa')


# dictionaries (OBJECT)
# person = {
#     'fname': 'John',
#     'lname': 'paolo',
#     'age': 22
# }

# print(person)


# LOOPS
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# fruits = ['mangga', 'santol', 'buko', 'apple', 'buko']

# for fruit in fruits:
#     print(fruit)


# TRY CATCH
# while True:
#     try:
#         number = input('enter a number: ')
#         print(int(number))
#         break
#     except ValueError:
#         print('enter a valid number')



# from StudentClass import Student
# student1 = Student('sydney', 201911143, 'BSIS', False)
# student1.greet()
# student1.greetFromTeacher()


# EXERCISE FROM MOSH

while True: 
    weight = input('Weight: ')
    if weight.isdigit():
        break
    print('Enter a valid number')

weightType = input('(K)g or (L)bs: ').upper()

if weightType == 'L':
    print('Weight in Kg: ' + str(float(weight) * 0.45359237))

elif weightType == 'k':
    print('Weight in lbs: ' + str(float(weight) * 2.2))

else:
    print('Select L/ or K/k only.')