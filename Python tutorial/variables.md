# Var
```py
2myvar = "John"
my-var = "John"
my var = "John"
# Both of them will cause syntax error, similar as javascript, but the first of them will throw error in python
```
```py
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# legal var
```
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

```py
myVariableName = "John"
```
Pascal Case
Each word starts with a capital letter:
```py
MyVariableName = "John"
```
Snake Case
Each word is separated by an underscore character:
```py
my_variable_name = "John"
```
# Multiple Var
```py
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



x = y = z = "Orange"
print(x)
print(y)
print(z)



# Extract

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

# Output
use `print(x, y, z)` instead of `print(x+y+z)` else it will not show the spaces between them

# Global
```py
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
