#functions:
#syntax:
#def function_name(parameters):
    #code to execute when the function is called
    #return value (optional)

#parts of a function:
#1) Function Declaration: This is where you define the function and its parameters.
#2) Function Definition: This is the block of code that performs the task defined by the function.
#3) Function Call: This is where you invoke the function to execute its code.

def greet():
    pass

def greet():
    print("Good Morning!")

greet()
greet()
greet()

#function with parameters
#variable within parantheses are called parameters and they act as placeholders for the values that will be passed to the function when it is called.
#name is a parameter
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Soumya")
say_hello("Alice")
say_hello("Bob")




def printDetails(name, company="Parvam"):
    print(f"I'm {name} and I work at {company}.")
printDetails("Soumya")
printDetails("Alice", "Google")

# *args - Variable Positional Arguments

def findSum(*args):
    sum = 0
    for num in args:
        sum += num
    print(f"Sum of given numbers: {sum}")

# Function calls
findSum(20, 30)
findSum(20, 30, 50)
findSum(20, 30, 50, 60, 80)
findSum(20, 30, 50, 60, 80, 95, 100)

def findEvenOdd(*args):
    print("The given numbers are as follows:")
    for num in args:
        print(num)

    print("Even numbers out of given numbers are as follows:")
    for num in args:
        if num % 2 == 0:
            print(num)

    print("Odd numbers out of given numbers are as follows:")
    for num in args:
        if num % 2 != 0:
            print(num)


# Function calls
findEvenOdd(2, 4, 7, 9, 11)
findEvenOdd(1, 3, 6, 8, 11, 14, 16, 19)

# Function calls for even/odd
findEvenOdd(2, 4, 7, 9, 11)
findEvenOdd(1, 3, 6, 8, 11, 14, 16, 19)
findEvenOdd(5, 8, 11, 12, 18, 22, 23)


# **kwargs - Variable length keyword arguments
def printInfo(**person):
    print(f"He is {person['name']}, he is working at {person['company']}")


# Function calls
printInfo(name="Akshay Rao", age=24, company="Parvah", address="Bengaluru")

printInfo(name="Varun", company="Infosys", address="Bengaluru", pincode=560090)

# Function call from previous part
printInfo(name="Varun", company="Infosys", address="Bengaluru", pincode=560090)


# Function using **kwargs
def userInfo(**user):
    print("User Details are as follows:")
    print(f"Name: {user['name']}")
    print(f"Email ID: {user['email']}")
    print(f"Phone Number: {user['phone']}")


# Function calls
userInfo(
    name="Akshay",
    id=123,
    email="akshay@gmail.com",
    company="Parvah",
    phone="9623145123",
    mode_of_transport="Bus"
)

userInfo(
    name="Ajay",
    usn="AJ456",
    email="akshay@gmail.com",
    college="RVCE",
    phone="9623145123")