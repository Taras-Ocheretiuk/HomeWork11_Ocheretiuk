# Завдання 1
# Реалізуйте клас «Людина». Необхідно зберігати в полях класу: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до окремих полів за допомогою методи класу.

class  Human:

    def __init__(self, name_surname="Taras Ocheretiuk", date_of_birth="1.01.1990", phone_number="0674454612",
                 city="Makariv", country="Ukraine", home_address="Shevchenka strit"):
        self.name_surname = name_surname
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def set_human_data (self, new_name_surname, new_date_of_birth, new_phone_number, new_city, new_country, new_home_address):
        self.name_surname = new_name_surname
        self.date_of_birth = new_date_of_birth
        self.phone_number = new_phone_number
        self.city = new_city
        self.country = new_country
        self.home_address = new_home_address

    def get_human_date (self):
        return (f"My name is {self.name_surname} I was born {self.date_of_birth} my phone number {self.phone_number} I live in the country {self.country} in the city {self.city} at the address {self.home_address}")

person = Human()

person.set_human_data(new_name_surname="Peter Jackson", new_date_of_birth="2.02.2000", new_phone_number = '0937744100', new_city = "Kyiv", new_country = "Ukraine", new_home_address="Shevchenka strit 100")

print(person.get_human_date())

# Завдання 2
# Створіть клас "Місто". Необхідно зберігати в полях класу: назва міста, назва регіону, назва країни, кількість жителів у
# місті, поштовий індекс міста, телефонний код міста. Реалізуйте методи класу для введення даних, виведення даних,
# реалізуйте доступ до окремих полів через методи класу.

class City:
    def __init__(self, name_city="Makariv", name_region="Kyiv regine", residents_city=4000000, index="08000", phone_code="027"):
        self.name_city = name_city
        self.name_region = name_region
        self.residents_city = residents_city
        self.index = index
        self.phone_code = phone_code

    def set_your_city (self, new_name_city, new_name_region, new_residents_city, new_index, new_phone_code   ):
        self.name_city = new_name_city
        self.name_region = new_name_region
        self.residents_city = new_residents_city
        self.index = new_index
        self.phone_code = new_phone_code

    def get_your_city (self):
        return (f"I live in the city {self.name_city} this is the {self.name_region} region, in our city live {self.residents_city} residents, index {self.index}, phone code {self.phone_code}")

person = City()
person.set_your_city(new_name_city="Kyiv", new_name_region="Kyiv regine", new_residents_city="5000000", new_index="08001", new_phone_code="045" )

print(person.get_your_city())

# Завдання 3
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назва столиці, назва міст країни. Реалізуйте методи класу для введення
# даних, виведення даних, реалізуйте доступ до окремих полів через методи класу.
class Country:
    def __init__(self, name=True, continent=True, population=True, phone_code=True, capital=True, name_city=True):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.name_city = name_city

    def set_your_country(self, new_name, new_continent, new_population, new_phone_code, new_capital, new_name_city):
        self.name = new_name
        self.continent = new_continent
        self.population = new_population
        self.phone_code = new_phone_code
        self.capital = new_capital
        self.name_city = new_name_city

    def get_your_country(self):
        return (f"I live in a country {self.name}, located on {self.continent} continent, population of my country {self.population}, telephone code {self.phone_code}, capital {self.capital}, city of my country {self.name_city}.")

usa = Country()

# usa.set_your_country(new_name="USA", new_continent="North America", new_population="331 million", new_phone_code="+1", new_capital="Washington D.C.", new_name_city="Washington D.C.")

print(usa.get_your_country())


# Завдання 4
# Створіть клас «Дроб». Необхідно зберігати у полях класу: чисельник та знаменник.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до
# окремим полям через методи класу. Також створіть методи класу для виконання арифметичних операцій(додавання,
# віднімання, множення, розподіл, і т.д.).

class Fraction:
    numerator = True  # чисельник
    denominator = True  # знаменник
    comand = True


    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def addition(self, comand):
        self.comand = comand
        if self.comand == "+":
            result = self.numerator + self.denominator
            return result
        elif self.comand == "-":
            result = self.numerator - self.denominator
            return result
        elif self.comand == "*":
            result = self.numerator * self.denominator
            return result
        elif self.comand == "/":
            result = self.numerator / self.denominator
            return result

example_1 = Fraction(1,9)

result = example_1.addition("+")
print(result)

# class Fraction:
#     numerator = True    # чисельник
#     denominator = True # знаменник
#     comand = True
#
#     def method_fractions (self):
#         self.numerator = int(input("Enter numerate (чисельник): "))
#         self.denominator = int(input("Enter denominator (знаменник): "))
#         self.comand = input("Enter comand: ")
#
#     def addition (self):
#         if self.comand == "+":
#             result = self.numerator + self.denominator
#             return ("Result of addition:", result)
#         elif self.comand == "-":
#             result = self.numerator - self.denominator
#             print("Result of addition:", result)
#         elif self.comand == "*":
#             result = self.numerator * self.denominator
#             print("Result: ", result)
#         elif self.comand == "/":
#             result = self.numerator / self.denominator
#             print("Result: ", result)

# example_1 = Fraction()
#
# example_1.method_fractions()
# example_1.addition()



