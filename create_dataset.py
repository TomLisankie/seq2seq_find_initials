from faker import Faker
import csv
from random import random

affixes = set(['Mrs.', 'Ms.', 'Miss', 'Dr.', 'Mr.', 'MD', 'DDS', 'PhD', 'DVM', 'Jr.', 'Sr.', 'I', 'II', 'III',
'IV', 'V'])

"""Gets initials of a human name
"""
def get_initials(name):
    fml = name.split(" ")  #first, middle, last names
    initial_list = [word[0] for word in fml]
    return "".join(initial_list).upper()


"""Changes case of letters in a name probabilistically. This is so the model getting trained later doesn't just learn 
that uppercase letters are always the initials but instead learns that it's the first letters of each of the 
person's names.
"""
def alter_formatting(name):
    chance = 0.4
    char_list = list(name)
    new_char_list = []
    for char in char_list:
        random_number = random()
        if char.isalpha() and random_number <= chance:
            if char.islower():
                new_char_list.append(char.upper())
            else:
                new_char_list.append(char.lower())
        else:
            new_char_list.append(char)
    return "".join(new_char_list)

def remove_affixes(name):
    fml = name.split(" ")  #first, middle, last names
    cleaned_list = []
    for word in fml:
        if word not in affixes:
            cleaned_list.append(word)
            cleaned_list.append(" ")
    return "".join(cleaned_list).strip()

fake = Faker()
names = {}
for i in range(1000000):
    fake_name = remove_affixes(fake.name())
    fake_name = alter_formatting(fake_name)
    names[fake_name] = get_initials(fake_name)

data_path = "data/"
with open(data_path + "names_initials.csv", "w") as data:
    w = csv.writer(data)
    w.writerows(names.items())