#Домашня робота №4

# Завдання 1
# Користувач вводить рядок з клавіатури. Перевірте, чи є введений рядок паліндромом. Паліндром - слово або текст,
# яке читається однаково зліва направо та зправа наліво. Наприклад, кок; tenet;
# Sit on a potato pan, Otis.
# Cigar? Toss it in a can. It is so tragic.
# Go hang a salami, I'm a lasagna hog.

# user_input = input("Введіть рядок: ")
#
# cleaned_input = ''  # Змінна для зберігання очищеного рядка
#
# # Цикл для перебору символів у введеному рядку
# for char in user_input:
#     # Перевірка, чи є символ літерою або цифрою
#     if char.isalnum():
#         # Переведення символу у нижній регістр
#         lowercase_char = char.lower()
#         # Додавання символу у нижньому регістрі до змінної cleaned_input
#         cleaned_input = cleaned_input + lowercase_char
#
# reversed_input = ''  # Змінна для зберігання оберненого рядка
#
# # Цикл для створення оберненого рядка
# for char in cleaned_input:
#     reversed_input = char + reversed_input
#
# # Перевірка на паліндром та виведення результату
# if cleaned_input == reversed_input:
#     print("Це паліндром")
# else:
#     print("Це не паліндром")


# Завдання 2
# Користувач вводить із клавіатури деякий текст, після чого користувач вводить перелік зарезервованих слів.
# Необхідно знайти в тексті всі зарезервовані слова та змінити їхній регістр на верхній.
# Вивести на екран змінений текст.

# s = "Hello, this word has many different equivalents in Hello various languages."
# words = "hello this word"#input("Введіть рядок слів через пробіл: ")
# words = words + " "
# start = 0
# modified_text = s
# for i in range(len(words)):
#     if words[i] == ' ':
#         word = words[start:i]
#         start = i + 1
#         modified_text = modified_text.replace(word, word.upper())
# print(modified_text)

# Завдання 3
# Є певний текст. Порахуйте кількість речень у цьому тексті та виведіть на екран отриманий результат.
# Будьте уважні, та не забудьте протестувати на різних текстах.
#Сам придумав додумався ;)

# s = "The sky was clear and the stars twinkled brightly above. I felt a sense of tranquility wash over me! Did you hear that noise coming from the woods? It sounded eerie. The wind howled through the trees, making the branches sway wildly! The anticipation built up in the air. Suddenly, a loud crash echoed in the distance!? Everyone froze in shock. What could that be?! I ran towards the sound, heart pounding, adrenaline rushing through my veins!!?"
#
#
# new1_s = s.replace('!!?', ' ! ')
#
# new2_s = new1_s.replace('!?', ' ! ')
#
# new3_s = new2_s.replace('!!', ' ! ')
#
# new4_s = new3_s.replace('...', ' ! ')
#
# new5_s = new4_s.replace('?!', ' ! ')
#
# count = 0
#
# for elem in new5_s:
#      if elem == ".":
#          count = count + 1
#      elif elem == "!":
#          count = count + 1
#      elif elem == "?":
#          count = count + 1
#
# print(f"В тексті {count} речень.")



