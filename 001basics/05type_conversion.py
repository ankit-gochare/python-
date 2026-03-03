a = 23
print(type(a)) # <class 'int'>

a = str(a)
print(type(a)) # <class 'str'>

# str cannot be converted to int 
b = "hello"
# b = int(b) # valueError - invalid literal for int() with base 10

# but if a number is stored in str then it can be 
d = "34" 
d = int(d)
print(type(d)) # <class 'int'>

# same for float
d = float(d)
print(type(d)) # <class 'float'>

# conversion in bool
e = 0
e = bool(e)
print(e) # False
print(type(e)) # <class 'bool'>

f = 1
f = bool(f)
print(f) # True
print(type(f)) # <class 'bool'>

# Truthy values - almost everything

# Falsy values - 0, 0.0, False, "", [], {}, ()



# notes
"""
Type conversion
When we have to convert one datatype to another we use type
conversion
int() - Converts the datatype to integer
float() - Converts the datatype to float
str() - Converts the datatype to string
bool() - Converts the data type to Boolean

Truthy values - almost everything
Falsy values - 0, 0.0, False, “”, [], {}, ()

"""