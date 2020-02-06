# COMPARISON OPERATORS


# CONDITIONALS
temp = 15
if temp > 30:
    print("It's warm, drink water!")
elif temp > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# TERNARY OPERATORS
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# LOGICAL OPERATORS (and, or, not)
high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")


# SHORT-CIRCUIT EVALUATION
# In python, logical operators are short-circuit


# CHAINING COMPARISON OPERATORS
age = 22
if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")


# FOR LOOPS
for number in range(1, 3):
    print("Sending a Message...", number + 1, (number + 1) * ".")

# FOR ELSE
successful = False
for num in range(1, 4):
    print("Attempt")
    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")


for x in range(4):
    for y in range(3):
        print("X: ", x, " Y: ", y)


# ITERABLES
print(type(5))
print(type(range(5)))
for x in "Python":
    print(x)
for y in [1, 2, 3, 4]:
    print(y)


# WHILE LOOPS
number = 100
while number > 0:
    print(number)
    number = number // 2


# command = ""
# while command.lower() != "quit":
#     command = input("> ")
#     print("ECHO", command)


# INFINITE LOOPS
# while True:
    # anything here without condition will run indefinitely


# EXERCISE
# display even numbers between 1 to 10
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print("Even Numbers: ", i)
print("There are ", count, " Even numbers")
