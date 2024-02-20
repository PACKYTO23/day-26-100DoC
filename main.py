# numbers = [1, 2, 3]  # For Loop
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# new_list = [new_item for item in list]  # List Comprehension
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# name = "Francisco"  # String as List
# new_list = [letter for letter in name]
# print(new_list)

# new_range = [n * 2 for n in range(1, 5)]  # Range as List
# print(new_range)

# new_list = [new_item for item in list if test]  # Conditional List Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 55]  # Squaring Numbers
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)

# list_of_strings = input().split(",")  # Filtering Even Numbers
# to_integers = [int(n) for n in list_of_strings]
# result = [n for n in to_integers if n % 2 == 0]
# print(result)

# with open("file1.txt") as file:  # Data Overlap
#     data = file.readlines()
#     contents_1 = [int(n.strip()) for n in data]

# with open("file2.txt") as file:
#     data = file.readlines()
#     contents_2 = [int(n.strip()) for n in data]

# result = [n for n in contents_1 if n in contents_2]
# print(result)

# new_dict = {new_key: new_value for item in list}  # Dictionary Comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}  # Conditional Dictionary Comprehension

# from random import randint
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: randint(1, 100) for student in names}
# print(students_scores)

# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = input()  # Dictionary Comprehension 1
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = eval(input())  # Dictionary Comprehension 2
# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: temp_c * 9/5 + 32 for day, temp_c in weather_c.items()}
# print(weather_f)

# student_dict = {  # Looping through dictionaries.
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98],
# }

# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():  # Loops to iterate in Pandas DataFrame.
#     print(key, value)

# for (index, row) in student_data_frame.iterrows():  # Loop through rows of a data frame.
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key: new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_list = []
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    # letter = row.letter
    # code = row.code
    # nato_list.append((letter, code))

# nato_dict = {letter: code for letter, code in nato_list}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# letters = [letter.upper() for letter in word]
codes = [nato_dict[letter] for letter in word]

print(codes)
