# input() function
name = input("Hey What is your name ?")
print(name)

age = input("Hello What is your age?")
# print(f"after 2 years you will be {age+2} years old") # error because age is stored in string 

age = int(age)
print(f"after 2 years you will be {age+2} years old") # 23

marks = int(input("Enter your marks"))
print(marks)


# notes
"""
Input statement ways
input() function
Default datatype of inputs
Default type is String

Taking custom datatypes input
You can take custom inputs using type conversio

int(input(“tell your age”))
"""