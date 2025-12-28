#tuples in python
# tuple is a collection data type in python
# ordered, immutable, indexed
#  NO SORT, NO append NO REVERSE
# once created cannot be altered unlike list

# defined by parentheses ( )

# can contain elements of different data types
# common methods: count(), index()
# tuples support iteration using loops
# tuples can be nested
# tuples support membership testing using the in and not in operators
# tuples have a length that can be obtained using the len() function
# tuple unpacking allows you to assign elements to variables
# creating a tuple
my_tuple = (1, 2, 3)
# my_tuple[1] = 4  # This will raise a TypeError since tuples are immutable
print(type(my_tuple))  # Output: <class 'tuple'>
print(my_tuple)  # Output: (1, 2, 3)
print(len(my_tuple))  # Output: 3

# accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 3

# slicing
print(my_tuple[1:3])  # Output: (2, 3)

# concatenation
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# nested tuples
nested_tuple = (1, 2, (3, 4))
print(nested_tuple[2])  # Output: (3, 4)

# tuple methods
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(3))  # Output: 2

print(dir(my_tuple))  # Output: 'count', 'index' only

(x, y) = (10, 'hello')
print(x)  # Output: 10
print(y)  # Output: hello
# swapping values
a = 5
b = 10
a, b = b, a
print(a)  # Output: 10
print(b)  # Output: 5
# single element tuple
single_element_tuple = (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
not_a_tuple = (42)
print(type(not_a_tuple))  # Output: <class 'int'>

# tuple packing
packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)    
print(type(packed_tuple))  # Output: <class 'tuple'>
# membership testing
print(2 in my_tuple)  # Output: True
print(5 not in my_tuple)  # Output: True    
# iteration
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3     
# tuple comprehension (using generator expression)
squared = tuple(x**2 for x in range(5))
print(squared)  # Output: (0, 1, 4, 9, 16)
# length of tuple
print(len(squared))  # Output: 5
# converting list to tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
print(converted_tuple)  # Output: (1, 2, 3)
# converting string to tuple
my_string = "hello"
string_tuple = tuple(my_string)
print(string_tuple)  # Output: ('h', 'e', 'l', 'l', 'o')
# converting tuple to list
list_from_tuple = list(my_tuple)
print(list_from_tuple)  # Output: [1, 2, 3]
# converting tuple to string
string_from_tuple = ''.join(map(str, my_tuple))
print(string_from_tuple)  # Output: '123'
# min and max
print(min(my_tuple))  # Output: 1
print(max(my_tuple))  # Output: 3
# sum
print(sum(my_tuple))  # Output: 6   
# sorting a tuple (returns a list)
sorted_tuple = tuple(sorted(my_tuple, reverse=True)) # then convert that list into tuple
print(sorted_tuple)  # Output: (3, 2, 1)
# sorted_tuple[1]=5  # This will raise a TypeError since tuples are immutable
# slicing a tuple
sliced_tuple = my_tuple[0:2]
print(sliced_tuple)  # Output: (1, 2)
# reversing a tuple (returns a tuple)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)  # Output: (3, 2, 1)
# tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)
# accessing nested tuple elements
nested = (1, (2, 3), (4, (5, 6)))
print(nested[2][1][0])  # Output: 5
# tuple with different data types
data_tuple = (42, "Python", 3.14, [1, 2, 3], (4, 5))
print(data_tuple)  # Output: (42, 'Python', 3.14, [1, 2, 3], (4, 5))
# accessing elements of different data types
print(data_tuple[1])  # Output: Python
print(data_tuple[3][0])  # Output: 1
print(data_tuple[4][1])  # Output: 5
# tuple with boolean values
bool_tuple = (True, False, True)
print(bool_tuple)  # Output: (True, False, True)
# accessing boolean values
print(bool_tuple[0])  # Output: True
print(bool_tuple[1])  # Output: False
# counting boolean values
print(bool_tuple.count(True))  # Output: 2
print(bool_tuple.count(False))  # Output: 1



# comparison operator works for tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)  # Output: True
print(tuple1 == tuple2)  # Output: False
print(tuple1 > tuple2)  # Output: False

# dictionary items are immutable but dictionary itself is mutable because they are tuples
my_dict = {'a': 1, 'b': 2}
for item in my_dict.items():
    print(item)
# Output:
# ('a', 1)
# ('b', 2)
# item[0] = 'c'  # This will raise a TypeError since dictionary items are immutable
# but we can modify the dictionary itself
my_dict['a'] = 10
print(my_dict)  # Output: {'a': 10, 'b': 2}

# zip function returns an iterator of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(tuple(zipped))  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))  

# namedtuple from collections module
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x)  # Output: 10
print(p.y)  # Output: 20
# unpacking namedtuple
x, y = p    
print(x)  # Output: 10
print(y)  # Output: 20

# swapping using namedtuple
a = Point(1, 2)
b = Point(3, 4)
a, b = b, a
print(a)  # Output: Point(x=3, y=4)
print(b)  # Output: Point(x=1, y=2)


#      3rd operation (  2nd op[eration ([o/p iteration item in dict ]))
# list comprehension to create a list of tuples
c= {'x': 1, 'y': 3, 'z': 2}
tuple_list = sorted([(value, key) for key, value in c.items()]) # sorting based on first element of tuple   
print(tuple_list)  # Output: [(1, 'x'), (2, 'z'), (3, 'y')]
