import math
# STRING METHODS
course = "Python Programming"
course_2 = "  Space Before"
print(course.upper())
print(course.lower())
print(course.title())
print(course_2)
print(course_2.strip())  # remove spaces before and after string
print(course.find("Pro"))  # finds the index
print(course.replace("P", "J"))  # replace a char or string
print("pro" in course)  # boolean returning true or false


# NUMBERS
print(10 / 3)  # returns float
print(10 // 3)  # returns integer
print(round(2.8))
print(abs(-2.8))
print(math.ceil(2.2))


# TYPE CONVERSION
x = input("X: ")  # default input is string --> convert to int
print(type(x))
y = int(x) + 1
print(type(x))
print(y)
