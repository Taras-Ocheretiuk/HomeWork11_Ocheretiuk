# Lesson 1 Automation Python
# name_Dog = input("Enter name your dog: ")
# name_Cat = input("Enter name your cat: ")
# name_parrot = input("Enter name your parrot: ")
#
# print(f"I have a dog. His name is: {name_Dog}. I heve a cat, his name: {name_Cat}. I heve a parrot, his name: {name_parrot}")

# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) # Цілочислове ділення
# print(a % b) # Остача від ділення
# print(a ** b) # Виведемо число а в степені
# #Lesson 2 Automation Python
# age = 18
#
# if age < 18:
#     print("You are a child")
# else:
#     print("You are a adult")
#
# height = 150
# if height < 120:
#     print("Прохід заборонено")
# elif height < 140:
#     print("Прохід обмежено")
# else:
#     print("Прохід дозволено")

# a = 0
# while a < 10: # while для роботи має отримати True
#     print(a)
#     a=a+1 # інкремент

# a = 1
# b = 36
# while a <= b:
#     if a % 2 != 0:
#         print(a)
#     a+=1

# for i in 1, 2, 3, 4, 5, 6:
#     print(i)
#
# a = 1
# b = 36
# for i in range (a, b+1):
#     if a % 2 != 0:
#         print(i)

# a = 1
# b = 36
# for i in range (a, b+1):
#     if a % 2 != 0:
#         print(i)


#Домашка №2

# Завдання 1
# Користувач вводить три цифри з клавіатури. Залежно від вибору користувача, програма виводить на екран суму трьох
# чисел або добуток трьох чисел.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 31: "))
summa=input("You want to add numbers (Yes or No): ")

if summa == "Yes":
    print(a+b+c)
else:
    print(a*b*c)

# Завдання 2
# Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середнеарифметичне трьох чисел.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
math_func = input("Do you want to see the maximum number, the minimum minimum number or the arithmetic mean? (Max or Min or Аrithmetic mean): ")

if math_func == "Max":
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

elif math_func == "Min":
    if a<b and a<c:
        print(a)
    elif b<a and a<c:
        print(b)
    else:
        print(c)
else:
    print((a+b+c)/3)

#Завдання 3
# Користувач вводить з клавіатури номер дня тижня
# (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, то на екрані напис понеділок, 2 - вівторок і т.д.

number_of_week = int(input("Enter the number of the day of the week, from 1 to 7: "))

if number_of_week == 1:
    print("Monday")
elif number_of_week == 2:
    print("Tuesday")
elif number_of_week == 3:
    print("Wednesday")
elif number_of_week == 4:
    print("Thursday")
elif number_of_week == 5:
    print("Friday")
elif number_of_week == 6:
    print("Saturday")
elif number_of_week == 7:
    print("Sunday")
else:
    print("You entered an incorrect number")

# Завдання 4
# Користувач вводить з клавіатури номер місяця (1-12). Необхідно вивести на екран назву місяця.
# Наприклад, якщо 1, то на екрані напис січень, 2 - лютий і т.д.

number_of_month = int(input("Enter the number of the month, from 1 to 12: "))

if number_of_month == 1:
    print("January")
elif number_of_month ==2:
    print("February")
elif number_of_month ==3:
    print("March")
elif number_of_month ==4:
    print("April")
elif number_of_month ==5:
    print("May")
elif number_of_month ==6:
    print("June")
elif number_of_month ==7:
    print("July")
elif number_of_month ==8:
    print("August")
elif number_of_month ==9:
    print("September")
elif number_of_month ==10:
    print("October")
elif number_of_month ==11:
    print("November")
elif number_of_month ==12:
    print("December")
else:
    print("You entered an incorrect number")

# Завдання 5
# Користувач вводить із клавіатури число. Якщо число
# більше нуля потрібно вивести напис "Number is positive", якщо менше нуля "Number is negative", якщо дорівнює нулю
# «Number is equal to zero»

number = int(input("Enter the number: "))

if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is equal to zero")
else:
    print("Number is negative")

# Завдання 6
# Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання.

number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))

if number1 != number2:
    if number1 > number2:
        print(number1, number2)
    else:
        print(number2, number1)
else:
    print("The numbers are equal!")

# Завдання 7
# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати всі числа в цьому
# діапазоні за таким правилом: якщо число кратно 7 його треба виводити на екран.

start_range = int(input("Start of range: "))
finish_range = int(input("Finish of range: "))

while start_range <= finish_range:
    if start_range % 7 == 0:
        print(start_range)
    start_range = start_range + 1

# Завдання 8

# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати все числа у цьому діапазоні.
# Потрібно вивести на екран:
# 1. Усі числа діапазону;
# 2. Усі числа діапазону у спадному порядку;
# 3. Усі числа, кратні 7;
# 4. Кількість чисел, кратних 5.

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

# 1. Усі числа діапазону
print("Усі числа діапазону:")
for i in range(start, end + 1):
    print(i, end=" ")
print()

# 2. Усі числа діапазону у спадному порядку
print("Усі числа діапазону у спадному порядку:")
for i in range(end, start - 1, -1):
    print(i, end=" ")
print()

# 3. Усі числа, кратні 7
print("Усі числа, кратні 7:")
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

 # 4. Кількість чисел, кратних 5
count_multiples_of_5 = 0
for i in range(start, end + 1):
    if i % 5 == 0:
        count_multiples_of_5 += 1

print(f"Кількість чисел, кратних 5: {count_multiples_of_5}")

# Завдання 9
# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати усі числа у цьому діапазоні.
# Виведення на екран має відбуватися за правилами, наведеними нижче. Якщо число кратне 3 (ділиться на 3 без залишку),
# потрібно вивести слово Fizz. Якщо число разів 5 потрібно вивести слово Buzz. Якщо число кратно 3 та 5 потрібно вивести
# Fizz Buzz. Якщо число не раз не 3 і 5 потрібно вивести саме число.

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
