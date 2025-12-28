# in python3 all strings are unicode strings
# String literals can be enclosed in single quotes ('...') or double quotes ("...")
# Triple quotes ('''...''' or """...""") can be used for multi-line strings
# Strings are immutable in Python
# String concatenation can be done using the + operator
# String repetition can be done using the * operator
# Strings can be indexed and sliced
# Common string methods include lower(), upper(), find(), replace(), split(), strip(), etc.


st = "hello brother"
x = 'll' in st
print(x)  # Output: True

y = 'ab' in st
print(y)  # Output: False

greet = "  hello, welcome to the world of Python."
print(greet.lower())  # Output: hello, welcome to the world of python.
print(greet.upper())  # Output: HELLO, WELCOME TO THE WORLD OF PYTHON.
print(dir(greet))  # Lists all the methods available for string objects
print(greet.capitalize())  # Output: Hello, welcome to the world of python.
print(greet.center(50))  # Centers the string in a field of width 50
print(greet.count('o'))  # Output: 5

print(greet.find('welcome'))  # Output: 7

print(greet.replace('Python', 'Java'))  # Output: hello, welcome to the world of Java.
print(greet.split(','))  # Output: ['hello', ' welcome to the world of Python.']
print(greet.strip())  # Removes leading and trailing whitespace
print(greet.replace(' ', '_'))  # Replaces spaces with underscores
print(greet.title())  # Output: Hello, Welcome To The World Of Python.
print(greet.join(['Hello', 'World']))  # Output: HelloWorld
print(len(greet))  # Output: 39
pos1 = greet.rfind(' ')
print('======>',greet[pos1:len(greet)])  # Output: ' Python.  '
print('======>',greet[pos1:])  # Output: ' Python.  '


# Extracting domain name from an email address
msg = "sachinklocham@gmail.com Sat JAN 01 2026 09:14:14 GMT+0530 (India Standard Time)"
atpos = msg.find('@')
#find space after atpos
spacepos = msg.find(' ', atpos)
domain = msg[atpos + 1:spacepos]
print(domain)  # Output: gmail.com

print(type(st))  # Output: <class 'str'>   in python2 it will be <type 'unicode'>

str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)  # Output: HelloWorld
print(str1 * 3)  # Output: HelloHelloHello
print(str1[0])  # Output: H 
print(str1[1:4])  # Output: ell
print(str1[-1])  # Output last char: o
y =  10;
z = 10;
print(type(z))  # Output: <class 'int'>

eq = y is z # is    - identity operator
print(eq)  # Output: True
eq1 = y == z # ==   - equality operator
print(eq1)  # Output: True

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Case 1: x and y
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object") #

# Case 2: x and z
if x is z:
    print("x and z are the same object") #
else:
    print("x and z are not the same object")


for letter in 'banana' :
    print(letter)




# Reverse a string
print(st[::-1])  # Output: rehbroh olleh
#list of numbers  as int reverse
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1]
