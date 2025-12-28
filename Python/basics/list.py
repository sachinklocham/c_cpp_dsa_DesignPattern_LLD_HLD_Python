#A list  is a kind of collection
#It is a mutable, ordered sequence of elements
l1 = [10, 20, 30, 40, 50]
print(l1)  # Output: [10, 20, 30, 40, 50]
print(type(l1))  # Output: <class 'list'>
print(len(l1))  # Output: 5
l1[1] = 25  # Modifying element at index 1
print(l1)  # Output: [10, 25, 30, 40, 50]

#Lists are defined by having values between square brackets [ ]
#Elements in a list can be of different types   
lst = [1,22,33,'hello',3.14,True]
print(type(lst))  # Output: <class 'list'>
print(lst)  # Output: [1, 22, 33, 'hello', 3.14, True]
print(len(lst))  # Output: 6
#Lists can contain duplicate elements
lst2 = [1, 2, 2, 3, 4, 4, 4]
print(lst2)  # Output: [1, 2, 2, 3, 4, 4, 4]

#Lists can be nested to create multi-dimensional lists
#Common list methods include append(), extend(), insert(), remove(), pop(), sort(), reverse(), etc.
#Lists can be indexed and sliced
#Lists support iteration using loops
#Lists can be concatenated using the + operator and repeated using the * operator
#Lists can be converted to other data types like tuples or sets and vice versa
#List comprehensions provide a concise way to create lists
#Lists support membership testing using the in and not in operators
#Lists have a length that can be obtained using the len() function
#Lists can be nested to create multi-dimensional lists
#nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Accessing elements in a nested list
#nested_list[0][1]  # Output: 2 # Accessing the second element of the first sub-list


friends = ['Alice', 'Bob', 'Charlie']
print(friends)  # Output: ['Alice', 'Bob', 'Charlie']
print(friends[0])  # Output: Alice
print(friends[-1])  # Output: Charlie
print(friends[1:3])  # Output: ['Bob', 'Charlie']

friends.append('David')
print(friends)  # Output: ['Alice', 'Bob', 'Charlie', 'David
friends.remove('Bob')
print(friends)  # Output: ['Alice', 'Charlie', 'David']
friends.sort()
print(friends)  # Output: ['Alice', 'Charlie', 'David']
friends.reverse()
print(friends)  # Output: ['David', 'Charlie', 'Alice']


print(range(5))  # Output: range(0, 5  ) return range upto 5 excluding 5
print(list(range(5)))  # Output: [0, 1, 2, 3, 4] convert range to list
print(list(range(2, 10)))  # Output: [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

for num in squares:
    print(num, end=' ')  # Output: 0 1 4 9 16 25 36 49 64 81

for i in range(len(squares)):
    print(squares[i], end=' ')  # Output: 0 1 4 9 16 25 36 49 64 81

print(squares[1:3] )    # Output: [1, 4]
print(25 in squares)  # Output: True
print(26 not in squares)  # Output: True
print(squares[:4])  # Output: [0, 1, 4, 9]
print(squares[3:])  # Output: [9, 16, 25, 36, 49, 64, 81]
print(squares[:])   # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

combined = squares + friends
print(combined)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 'David', 'Charlie', 'Alice']
repeated = friends * 2
print(repeated)  # Output: ['David', 'Charlie', 'Alice', 'David', 'Charlie', 'Alice']   

x = list()
print(type(x))  # Output: <class 'list'>
print(dir(x))  # Lists all the methods available for list objects

print(squares.count(4))  # Output: 1
print(squares.index(16))  # Output: 4   
squares.insert(2, 5)  # Insert 5 at index 2
print(squares)  # Output: [0, 1, 5, 4, 9, 16, 25, 36, 49, 64, 81]
popped_value = squares.pop()  # Removes and returns the last element
print(popped_value)  # Output: 81
print(squares)  # Output: [0, 1, 5, 4, 9, 16, 25, 36, 49, 64]
squares.extend([100, 121])
print(squares)  # Output: [0, 1, 5, 4, 9, 16, 25, 36, 49, 64, 100, 121] 
squares.sort()
print(squares)  # Output: [0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 100, 121]  
squares.reverse()
print(squares)  # Output: [121, 100, 64, 49, 36, 25, 16, 9, 5, 4, 1, 0] 
squares.remove(25)
print(squares)  # Output: [121, 100, 64, 49, 36, 16, 9, 5, 4, 1, 0]

squares.append(144)
print(squares)  # Output: [121, 100, 64, 49, 36, 16, 9, 5, 4, 1, 0, 144]
print(max(squares))  # Output: 144
print(min(squares))  # Output: 0
print(sum(squares))  # Output: 549

squares.clear()
print(squares)  # Output: []    

#list maintains order of insertion

 # strings and lists together
sent = "Hello world this is a list example"
words = sent.split() # outputs a list of strings
print(words)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'list', 'example']

#when we do not specify delimeter , it considers space, multiple spaces, new line, tab etc as delimeter
csv_sent = "apple,banana,cherry,date"
fruits = csv_sent.split(',') # specify comma as delimeter
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']  
joined_sent = ' '.join(words) # make sentence back with spaces
print(joined_sent)  # Output: "Hello world this is a list example"
csv_joined = ','.join(fruits)# make sentence back with commas
print(csv_joined)  # Output: "apple,banana,cherry,date"

fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split('.')
    print(words[2])  # Print the third word from lines starting with 'From ' => com
fhand.close()
l11 = [1, 2, 3]
l12 = [4, 5, 6]
l13 = l11.append(l12)
print(l11)  # Output: [1, 2, 3, [4, 5, 6]]
print(l13)  # Output: None
l13 = l11 + l12
print(l13)  # Output: [1, 2, 3, 4, 5, 6]

fname = input("Enter file name: ") # test.txt
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
# print(lst.sort())  # Output: None first sort then print
lst.sort()
print(lst)  # Output: Sorted list of unique words from the file



