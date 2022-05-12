# String
Python Strings
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

Example
print("Hello")
print('Hello')
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Example
a = "Hello"
print(a)
Multiline Strings
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
Or three single quotes:

Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
Note: in the result, the line breaks are inserted at the same position as in the code.

Python - Slicing Strings
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
Note: The first character has index 0.

Slice From the Start
By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])
ADVERTISEMENT

Slice To the End
By leaving out the end index, the range will go to the end:

Example
Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

Upper Case
Example
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
Lower Case
Example
The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

String Concatenation
To concatenate, or combine, two strings you can use the + operator.

Example
Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)
Example
To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

