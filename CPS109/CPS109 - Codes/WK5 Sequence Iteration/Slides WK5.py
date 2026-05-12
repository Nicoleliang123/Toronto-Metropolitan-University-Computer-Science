#WEEK 5
#Create a list of squares

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#Using map & lambda function
#map(function, iterable), show process of list
#list actually creates it
#lambda x, is variable you name

squares = list(map(lambda x:x**2, range(10)))
print(squares)

#List comprehension 
squares = [x**2 for x in range(10)]
print(squares)

#----------------------------------------------
#Create a new list with values doubled
a = [1,2,3,-4] 
a = [x*2 for x in a]
print(a)

#Filter list to exclude negative numbers
b = [x for x in a if x >= 0]
print(b)

#Apply function to all elements
c = [abs(x) for x in a]
print(c)

#Call a method on each element
Days = [' Sunday', 'Monday  ', 'Tuesday']
d = [blank.strip() for blank in Days]
print(d)

#Create list of 2-tuples like(number, square)
e = [(x,x**2) for x in range(6)]

#Flatten list using listcomp with two 'for'
f = [[1,2,3], [4,5,6], [7,8,9]]
f = [num for element in f for num in element]
print(f)

#Extract vowels from sentence
sentence = 'this is a sample sentence'
vowels = [v for v in sentence if v in 'aeiou']
print(vowels)

#Show first letter of each word
words = ["this", "is", "a", "list", "of", "words"]
items = [word[0] for word in words]
print(items)

#Lower/upper case converter
low = [x.lower() for x in ["A","B","C"]]
up = [x.upper() for x in ["a","b","c"]]
print(low)
print(up)

#Print numbers only from string
string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)

#Finding matching elements in two list
list1 = [1,2,3,4,5,6,6,5]
list2 = [3,5,7,9]

#set takes out repetitive away, so its comparable to list2
print(list(set(list1).intersection(list2)))

#Print odd numbers from the list
list3 = [1,2,3,4,5,6,7,8,9,10]
newlist = [x for x in list3 if x%2 != 0]
print(newlist)

#Print multiplation table
table = [[x*y for y in range(1,11)] for x in range(4,7)]
print(table)

