# DEFINING FUNCTIONS
def greet():
    print("Hi there")


greet()


# ARGUMENTS
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("Zaki", "Sediqyar")


# TYPES OF FUNCTIONS
# 1- perform a task, 2 - return a value

def get_greeting(name):
    return f"Hi {name}"


name = get_greeting("Zaki")
file = open("functions.txt", "w") # creates/opens a file with W(write) flag
file.write(name) # writes the name to the created file


# KEYWORD ARGUMENT
def increment(number, by):
    return number + by


result = increment(2, by=1) # by is the keyword argument in this function call
print(result)


# XARGS
# when the number of arguments aren't specifically defined. X number of arguments
def multiply(x, y):
    return x * y


multiply(2, 3)


def mult(*numbers):         # we can add any number of numbers we wish
    total = 1
    for number in numbers:
        total = total * number
        print(number)


mult(2, 3, 4, 5)


# XXARGS
# we use this to call a function with multiple keyword arguments which creates a key value pair


def save_user(**user):
    print(user)


save_user(name="Zaki", last="Sediqyar", id=1234, age=31)


# SCOPE
# block level and global level variables


# EXERCISE
def fizz_buzz(input):
    if input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    elif (input % 3 == 0) and (input % 5 == 0):
        print("FizzBuzz")
    else:
        print(input)


fizz_buzz(7)


# SOLUTION OF EXERCISE
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input



