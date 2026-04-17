# DataTypes in Python:

name = "Soumya"
age = 21
height = 5.1
IsTrainer = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Trainer:", IsTrainer)

#NON-PRIMITIVE DATA TYPES:List, Tuple, Set, Dictionary
languages_known = ["Python", "Java", "C++"]
print("Languages Known:", languages_known)

# Tuple is representudiing '()' and is immutable
#tuple is ordered and allows duplicate values
even_numbers = (0,2,4,5,6,8,10,12)
print("Even Numbers:", even_numbers)

#set is representing '{}' and is mutable
#Set is unordered and does not allow duplicate values
odd_numbers = {1,3,5,7,9}
print("Odd Numbers:", odd_numbers)

#Dictionary is representing '{}' and is mutable
#Dictionary is unordered and does not allow duplicate keys
profile = {
    "name": "Soumya",
    "age": 21,
    "company": "Google",
    "role": "Software Engineer"
}
print("Profile:", profile)