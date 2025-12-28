fhand = open('test.txt')

count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

#file pointer has reached very end of file, so to read again we need to reset pointer to starting
fhand.seek(0)

data = fhand.read()
print(fhand)  # Output: <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(data[:17]) # 17 chars from starting
print(data) # counting lines or printing data together does not work , need to do fhand.seek(0)
print(len(data))  # Output: total number of characters in file  

fhand.seek(0)
for line in fhand:
    line = line.rstrip()  # to remove trailing new line char
    if not '@google.com' in line:
        continue
    if line.startswith('From:'):
        print(line)
    print(line)

fhand.close()

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit() #quit() also can be used
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
fhand.close()

#with is helpful to auto close the file after its usage even if exception occurs in between
with open('test.txt') as fd:
    data1 = fd.read()
    print("opening file with with ",data1[:20])  # Output: first 20 characters from file