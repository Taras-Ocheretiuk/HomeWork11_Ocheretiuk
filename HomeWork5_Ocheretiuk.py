### Задача 1:
# **Умова:**
# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12. Необхідно
# вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз може
# складатися лише з трьох частин: число, операція, число. Можливі операції: +, -, *, /
# **Вхідні дані:**
# - Користувач вводить арифметичний вираз.
# **Вихідні дані:**
# - Вивести на екран результат обчислення виразу

# input_string = input("Введіть арифметичний вираз, наприклад 23+12: ")
#
# if "+" in input_string:
#     my_list = input_string.split("+")
#     сума = int(my_list[0]) + int (my_list[1])
#     print("Результат у вигляді списку:", сума)
# elif "-" in input_string:
#     my_list = input_string.split("-")
#     різниця = int(my_list[0]) - int(my_list[1])
#     print("Результат у вигляді списку:", різниця)
# elif "/" in input_string:
#     my_list = input_string.split("/")
#     частка = int(my_list[0]) / int(my_list[1])
#     print("Результат у вигляді списку:", частка)
# elif "*" in input_string:
#     my_list = input_string.split("*")
#     добуток = int(my_list[0]) * int(my_list[1])
#     print("Результат у вигляді списку:", добуток)

### Задача 2:
# **Умова:**
# У списку цілих чисел, заповненому випадковими числами, визначити мінімальний і
# максимальний елементи, порахувати кількість від'ємних елементів, порахувати кількість
# додатних елементів, порахувати кількість нулів. Результати вивести на екран.
# **Вхідні дані:**
# - Список цілих чисел, заповнений випадковими числами.
# **Вихідні дані:**
# - Мінімальний та максимальний елементи.
# - Кількість від'ємних, додатних та нульових елементів.

# list_integers = [15, 11, 44, -13]
#
# min_number = min(list_integers)
# max_number = max(list_integers)
#
# negative_count = 0
# positive_count = 0
# zero_count = 0
#
# for num in list_integers:
#     if num < 0:
#         negative_count += 1
#     elif num > 0:
#         positive_count += 1
#     else:
#         zero_count += 1
#
# print(f"Мінімальний елемент: {min_number}")
# print(f"Максимальний елемент: {max_number}")
# print(f"Кількість від'ємних елементів: {negative_count}")
# print(f"Кількість додатних елементів: {positive_count}")
# print(f"Кількість нульових елементів: {zero_count}")

### Задача 3:
# **Умова:**
# Два списки цілих чисел заповнюються випадковими числами. Необхідно:
# 1. Сформувати третій список, що містить елементи обох списків.
# 2. Сформувати третій список, що містить елементи обох списків без повторень.
# 3. Сформувати третій список, що містить елементи, спільні для двох списків.
# 4. Сформувати третій список, що містить лише унікальні елементи кожного зі списків.
# 5. Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків.
# **Вхідні дані:**
# - Два списки цілих чисел, заповнені випадковими числами.
# **Вихідні дані:**
# 1. **Сформувати третій список, що містить елементи обох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [4, 5, 6]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5, 6]`
# 2. **Сформувати третій список, що містить елементи обох списків без повторень:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`
# 3. **Сформувати третій список, що містить елементи, спільні для двох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[3]`
# 4. **Сформувати третій список, що містить лише унікальні елементи кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`
# 5. **Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 3, 4], [5, 6, 7, 8]`
# - Приклад вихідних даних: `[1, 4, 5, 8]`

# 1
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = list_1 + list_2
# print(list_3)
#
# list_1.extend(list_2)
# print(list_1)

# 2
# list_1 = [1, 2, 2, 3]
# list_2 = [3, 4, 5]
#
# set_3 = set(list_1 + list_2) # Обєднання списку в множину та відфільтруванна його
#
# list_3 = list(set_3) # Перетворення множини назад у список
#
# print(list_3)

# 3
# list_1 = [1, 2, 3]
# list_2 = [3, 4, 5]
#
# set_1 = set(list_1) # Перетворюємо список в множуну
# set_2 = set(list_2)
#
# list_3 = list(set_1.intersection(set_2)) # Метод для отримання перетину двох множин
#
# print(list_3)

# 4
# list_1 = [1, 2, 2, 3]
# list_2 = [3, 4, 5, 5]
#
# list_3 = []
#
# for item in list_1:
#     if item not in list_2 and item not in list_3: # Спочатку бере елемент із першого списку і перевіряє чи його немає у другому списку і в третьому і записує в третій список
#         list_3.append(item) # Метод append() використовується для додавання одного елемента в кінець списку іншого
#
# for item in list_2:
#     if item not in list_1 and item not in list_3:
#         list_3.append(item)
#
# print(list_3)

# 5. **Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 3, 4], [5, 6, 7, 8]`
# - Приклад вихідних даних: `[1, 4, 5, 8]`

# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
#
# list_3 = []
#
# min_list_1 = min(list_1)  # Знаходимо мінімальне значення в list_1
# list_3.append(min_list_1)  # Додаємо мінімальне значення до list_3
#
# max_list_1 = max(list_1)
# list_3.append(max_list_1)
#
# min_list_2 = min(list_2)
# list_3.append(min_list_2)
#
# max_list_2 = max(list_2)
# list_3.append(max_list_2)
#
# print(list_3)

### Задача 4:
# **На кортежі:**
# 1. **Створити кортеж:**
# - Створити кортеж, який містить кілька різних типів даних (цілі числа, рядки, дійсні
# числа). Вивести цей кортеж на екран.
# 2. **Зміна кортежу:**
# - Створити кортеж чисел. Змінити один з елементів кортежу та вивести змінений кортеж
# на екран.

# t = 1, 2, 44, "Hello", -9, 1, 2, 3
# print(t)
#
# l_from_t = list(t)
# l_from_t[2] = 55
#
# new_t = tuple(l_from_t)
# print("Змінений кортеж:", new_t)

### Задача 5:
# **На словники:**
# 1. **Операції зі словниками:**
# - Створити словник, що містить дані про деякий товар (наприклад, назва, ціна, кількість).
# Додати новий товар до словника та вивести оновлений словник на екран.
# 2. **Пошук та виведення:**
# - Створити словник, що містить інформацію про книги (назва, автор, рік видання).
# Здійснити пошук за назвою книги та вивести інформацію про неї.
# 3. **Видалення елементу:**
# - Створити словник, що містить дані про студентів (ім'я, прізвище, середній бал).
# Видалити інформацію про одного зі студентів та вивести оновлений словник на екран.

# 1
# product = {'назва': {'ціна':1000, 'кількість':10} }
#
# product['назва2'] = {'ціна': 1800, 'кількість': 25}
#
# print(product)

# 2
# books = {'Назва': ['автор', 2020], 'Назва2': ['автор2', 2022]}
#
# import pprint as p
#
# print(books['Назва'])

# 3

# students = {("Name1", "Sname1"):11, ("Name2", "Sname2"):12}
# del students[("Name2", "Sname2")]
# print(f"Оновлений список студентів: {students}")

### Задача 6:
# **На множини:**
# 1. **Операції з множинами чисел:**
# - Створити дві множини цілих чисел. Знайти їх об'єднання, різницю та перетин. Вивести
# результати на екран.
# 2. **Множина підмножин:**
# - Створити дві множини. Перевірити, чи є одна з них підмножиною іншої, та вивести
# результат.
# 3. **Операції з символами:**
# - Створити дві множини символів (літери алфавіту). Знайти їх об'єднання, різницю та
# перетин. Вивести результати на екран.
# 4. **Додавання та видалення елементів:**
# - Створити множину слів. Додати нове слово та видалити існуюче. Вивести оновлену
# множину на екран.

# 1
# s_1 = { 1, 3, 5, 6}
# s_2 = { 2, 4, 5, 6, 7}
#
# union_set = s_1.union(s_2)
# print("Об'єднання множин: ", union_set)
#
# difference_set = s_1.difference(s_2) # знайти ті, що є в одній, але немає в іншій
# print("Різниця множин: ", difference_set)
#
# intersection_set = s_1.intersection(s_2)
# print("Перетин множин: ", intersection_set)

# 2
# s_11 = {1, 2, 3, 4, 5}
# s_12 = {1, 3, 4}
#
# is_subset = s_12.issubset(s_11)
# if is_subset:
#     print("s_12 є підмножиною s_11")
# else:
#     print("s_12 не є підмножиною s_11")

# 3
#
# s_1 = { 'a', 'c', 'd', 'i'}
# s_2 = { 'b', 'c', 'd', 'f'}
#
# union_set = s_1.union(s_2)
# print("Об'єднання множин: ", union_set)
#
# difference_set = s_1.difference(s_2) # знайти ті, що є в одній, але немає в іншій
# print("Різниця множин: ", difference_set)
#
# intersection_set = s_1.intersection(s_2)
# print("Перетин множин: ", intersection_set)
#
# # 4
# w_s = {'bmw', 'toyota', 'honda', 'mazda'}
#
# w_s.add('nissan')
# print("Множина після додавання слова: ", w_s)
#
# w_s.discard('bmw')
# print("Множина після видалення слова: ", w_s)