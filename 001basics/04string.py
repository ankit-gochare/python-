a = "NATURE"
print(a)
print(type(a)) # <class 'str'>

# print individual elements
# positive indexing starts from 0 
print(a[0]) 
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# negative indexing starts from -1 from back side
print(a[-6]) 
print(a[-5]) 
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])
# space also take 1 index value 

# string slicing
# str[start : stop : steps]
# start is included 
# stop is excluded
# step means characters jump 
s = "I am learning python"
print(s[0:10:1]) # I am learn
print(s[0:10:2]) # Ia er
print(s[0:10:3]) # Imen
print(s[0:10:3]) # Imen
print(s[0:15:1]) # I am learning p
# print(s[0:15:0]) # error - step cannot be zero

print(s[5:13:1]) # learning
print(s[14::1]) # python



# there are default values as well 
# it will print the complete string 
print(s[::]) # I am learning python

# immutable string 
i = "me"
print(i) # me

i = "you"
print(i) # you 
# this is allowed to assign a new value but we can't change single single values

# i[0] = u # error

# Print statement ways
# Using normal variables in print statement (using ,)
age = 21
print("Hello , I am" ,age,"years old")
# we do not need to give extra space it will take itself

# what is formatted string
print(f"Hello , I am {age} years old")

# what are escape sequences
print(f"Hello\nI am {age} years old") # next line

print(f"Hello\tI am {age} years old") # tab 5 space

print(f"Hello\bI am {age} years old") # uses backspaces 
# o willnot print #HellI am 21 years old

# what is raw string
print(r"Hello\bI am {age} years old") # \b will not work now  # Hello\bI am {age} years old



# notes
"""
In Depth string

String Indexing
every string has its index eg - “hello”
0 1 2 3 4               -5 -4 -3 -2 -1
h e l l o                h  e  l  l  o

String slicing
- you can slice the strings as well
a = “yoo brother”
a[start : stop : steps]

Immutable nature
- you cannot change the string.


Print statement ways
Using normal variables in print statement (using ,)

what is formatted string
print(f”hello how are you {name_variable}”)

what are escape sequences - \n, \b, \t etc
\n- ends the line
\b- uses backspace
\t - uses tab 5 spaces


what is raw string
print(r”hello how are you \n”) \n will not work now

"""