#while loop
#syntax
#while condition:
    #code to execute while condition is true

i = 0
while i <= 10:
    print(i)
    i += 1

i = 1
print("Numbers from 1 to 10:")
while i <= 10:
    print(i)
    i += 1

print("Even numbers from 1 to 20:")
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#for loop
#syntax
#for variable in iterable:
    #code to execute for each item in iterable

numbers = [3,7,13,19,23,12]
total = 0
product = 1
print("Printing the list items:")
for num in numbers:
    print(num)
for num in numbers:
    total += num
print("Final Sum of the numbers:", total)

for num in numbers:
    product *= num
print("Final Product of the numbers:", product)

