# Завдання 1
# Створіть клас Human, який буде містити інформацію про людину.
# За допомогою механізму успадкування реалізуйте клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot (містить інформацію про льотчика).
# Кожен з класів повинен містити необхідні методи для роботи.

class Human:
    name = "Stas"
    age = 30
    profession = "empty"
    def life(self):
        return "live life"

class Builder (Human):
    profession = "builder"
    def builder(self):
        return "Build house"

class Sailor (Human):
    profession = "sailor"
    def sailor(self):
        return "Go to sea"

class Pilot (Human):
    profession = "pilot"
    def pilot(self):
        return "Aviate"

captain = Sailor()
print(captain.name)
print(captain.profession)
print(captain.sailor())

# Завдання 2
# Створіть клас Passport (паспорт), який буде містити паспортну інформацію про громадянина заданої
# країни. За допомогою механізму успадкування реалізуйте клас ForeignPassport (загр.паспорт),
# що є похідним від Passport. Нагадаємо, що закордонний паспорт містить, крім паспортних даних,
# також інформацію про візи та номер заграничного паспорта. Кожен з класів повинен містити необхідні
# методи.

class Passport:
    name = "Stas"
    s_name = "Stakhovsky"
    country = "Ukraine"
    def identifies(self):
         return (f"{self.name} {self.s_name} lived in {self.country}")

class ForeignPassport (Passport):
    visa = "opened"
    number_pasport = "UK112233"
    def travel(self):
        return (f"{self.name} {self.s_name} lived in {self.country}, number foreign passport {self.number_pasport} and has {self.visa} visa")

person = Passport()

person.identifies()
print(person.identifies())

person_travel = ForeignPassport()
print(person_travel.travel())


# Завдання 3
# Створіть базовий клас "Тварина" і похідні класи "Тигр", "Крокодил", "Кенгуру".
# За допомогою конструктора встановіть ім'я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.

class Animal:
    name = "pet"
    profession = "survive"
    def live(self):
        return "live and eat"

class Tiger (Animal):
    name = "Amur"
    profession = "roar"
    def hunt(self):
        return "hunt to eat"

class Crocodile (Animal):
    name = "Gena"
    profession = "swim"
    def swim(self):
        return "swim to eat"

class Kangaroo (Animal):
    name = "Kango"
    profession = "jump"
    def jump(self):
        return "jump to survive"



tiger = Tiger()
print(tiger.name)
print(tiger.profession)

crokogile = Crocodile()
print(crokogile.name)
print(crokogile.profession)

kangaroo = Kangaroo()
print(kangaroo.name)
print(kangaroo.profession)


#цей варіант не сам робив, але розумію як він працює
# class Animal:
#     def __init__(self, name="pet", profession="survive"):
#         self.name = name
#         self.profession = profession
#
#     def live(self):
#         return "live and eat"
#
# class Tiger(Animal):
#     def __init__(self, name="Amur", profession="roar"):
#         super().__init__(name, profession)
#
#     def hunt(self):
#         return "hunt to eat"
#
# class Crocodile(Animal):
#     def __init__(self, name="Gena", profession="swim"):
#         super().__init__(name, profession)
#
#     def swim(self):
#         return "swim to eat"
#
# class Kangaroo(Animal):
#     def __init__(self, name="Kango", profession="jump"):
#         super().__init__(name, profession)
#
#     def jump(self):
#         return "jump to survive"
#
# # Приклад використання класів:
# tiger = Tiger()
# print(f"Tiger name: {tiger.name}, profession: {tiger.profession}")
# print(tiger.live())
# print(tiger.hunt())
#
# crocodile = Crocodile()
# print(f"Crocodile name: {crocodile.name}, profession: {crocodile.profession}")
# print(crocodile.live())
# print(crocodile.swim())
#
# kangaroo = Kangaroo()
# print(f"Kangaroo name: {kangaroo.name}, profession: {kangaroo.profession}")
# print(kangaroo.live())
# print(kangaroo.jump())