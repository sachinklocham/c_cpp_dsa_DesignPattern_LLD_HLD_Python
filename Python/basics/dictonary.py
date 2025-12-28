# dictionary in python
# key-value pair
# unordered, mutable, indexed
# defined by curly braces { }
# keys must be unique and immutable (string, number, tuple)
# values can be of any data type and can be duplicate
# common methods: keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy(), fromkeys(), setdefault()
# dictionaries support iteration using loops
# dictionaries can be nested to create complex data structures
# dictionaries support membership testing using the in and not in operators
# dictionaries have a length that can be obtained using the len() function
# dictionary comprehensions provide a concise way to create dictionaries
#insertion order is preserved in Python 3.7 and later versions
# creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(my_dict))  # Output: <class 'dict'>
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(len(my_dict))  # Output: 3

cabinet = dict()
cabinet['A101'] = 'Alice'
cabinet['B202'] = 'Bob'
cabinet['C303'] = 'Charlie'
print(cabinet)  # Output: {'A101': 'Alice', 'B202': 'Bob', 'C303': 'Charlie'}
print(cabinet['A101'])  # Output: Alice

#counter with dictionary
text = "hello world hello world world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)  # Output: {'h': 2, 'e': 2, 'l': 7, 'o': 5, ' ': 4, 'w': 3, 'r': 3, 'd': 3}
#similarly we can do word count
words = text.split() # list of words ['hello', 'world', 'hello', 'world', 'world']
word_count = {}   # or use dict()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)  # Output: {'hello': 2, 'world': 3}

# with get function
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {'hello': 2, 'world': 3}


# key doesnot exist then get() returns None or default value if provided
print(my_dict.get('name'))  # Output: Alice or None
print(my_dict.get('country', 'USA'))  # Output: USA  - USA Default value

#without get method
if 'country' in my_dict:
    country = my_dict['country']
else:
    country = 'USA'
print(country)  # Output: USA
#try except block
try:
    country = my_dict['country']
except KeyError:
    country = 'USA'
print(country)  # Output: USA

# iterating through dictionary
for key in my_dict:
    print(key, my_dict[key])
# Output:
# name Alice
# age 25
# city New York 

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])
print(my_dict.items())  # Output list of key value : dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

for key, value in my_dict.items():
    print(key, value)
# Output:
# name Alice
# age 25
# city New York

# updating dictionary
my_dict['age'] = 26  # update existing key
my_dict['country'] = 'USA'  # add new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}    
my_dict.update({'city': 'Los Angeles', 'profession': 'Engineer'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Los Angeles', 'country': 'USA', 'profession': 'Engineer'}   
# removing items
age = my_dict.pop('age')  # removes key 'age' and returns its value
print(age)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice', 'city': 'Los Angeles', 'country': 'USA', 'profession': 'Engineer'}
item = my_dict.popitem()  # removes and returns the last inserted key-value pair
print(item)  # Output: ('profession', 'Engineer')
print(my_dict)  # Output: {'name': 'Alice', 'city': 'Los Angeles', 'country': 'USA'}
# other methods
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'name': 'Alice', 'city': 'Los Angeles', 'country': 'USA'}
my_dict.clear()
print(my_dict)  # Output: {}  Output: {}
# dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}   
# membership testing
print(2 in squares)  # Output: True
print(5 not in squares)  # Output: True 

# nested dictionary
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print(nested_dict['person1']['name'])  # Output: Alice
print(nested_dict['person2']['age'])  # Output: 30
# length of dictionary
print(len(nested_dict))  # Output: 2
# creating dictionary using fromkeys()
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0} 



name  = input("Enter File name: ") # example: test.txt
fhand = open(name)
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word,0) + 1
print(di)
bigcount = None
bigword = None
for word,count in di.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print("Most common word is:", bigword, "with count:", bigcount)