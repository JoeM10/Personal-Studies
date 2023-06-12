'''
#this will allow you to count how many of something there are in a given variable
str = "testing for loops"
count = 0

for x in str:
    if x == 't' :
        count += 1

print(count)

#

#this will stop the function when it reaches a given variable. Can be used to stop the loop or jump to the next iteration.
text = "some text"
for x in text :
    if x == 'e' :
        break
    print(x)

#

list = [2, 3, 4, 5, 6, 7]
# -EXAMPLE- The % does two things, depending on its arguments. In this case, it acts as the modulo operator,
# meaning when its arguments are numbers, it divides the first by the second and returns the remainder. 
# 34 % 10 == 4 since 34 divided by 10 is three, with a remainder of four.
for x in list :
    if(x%2==1 and x>4) :
        print(x)
        break

#

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum = 0

for num in x :
    sum += num

print(sum)

#

#Can be used to find variables that start with a specific character via input.
words = ["cat", "car", "code", "home", "learn", "fun", "job", "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]

letter = input()

for i in words :
    if letter in i:
        print(i)

#

#How to make a range list.
numbers = list(range(2, 10)) #remember that the second argument isnt included in the range, so 10 wont be included.
print(numbers)

#You can put the range list into a step. You can make the step go backwards if you use a negative step.
numbers = list(range(2, 21, 2))
print(numbers)

#You can use ranges in for loops to repeat some code a number of times
for i in range(5):
    print("Hello!")

#

#date picker
a = int(input())
b = int(input())

date = list(range(a, b)) :
print(date)

#

floors = int(input())

for i in range(1, floors):
    if i%5 == 0:
        print(i)

#

#List slices allow you to get a part of the list using two colon-seperated indices.
#This returns a new list containing all the values between the indices.
#Doesnt show the last value unless you do +1.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#If the first number in the list is ommited, its taken to be the start of the list.
print(squares[:5])

#If the second number is ommited, its taken to be the end of the list.
print(squares[2:])

#You can use a third value to include only alternate values in the slice.
print(squares[1:5:2])

#Negative values can also be used in list slicing(as well as normal list indexing).
#Which means that when negative values are used for the first and second values in a slice(or a normal index),
#they count from the end of the list.
#If a negative value is used for the step, the slice will be done backwards.
print(squares[1:-1])
print(squares[7:5:-1])

#Using [::-1] as a slice is a common way to reverse a list.
print(squares[::-1])

#

#Will print only the last letter of the input.
a = str(input())
b = a[::-1]
print(b[0])

#

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

#

##### THIS TOO #####
for i in range(10):
    if not i % 2 == 0:
        print(i + 1)

#

#Take a number N as input and output the sum of all numbers from 1 to N (including N)
N = int(input())
a = int(1)
b = list(range(a, N+1))
c = sum(b)
print(c)

# LIST FUNCTIONS -----------------------------------------

#len() lets you get the number of items in a list
nums = [1, 3, 5, 2, 4]
print(len(nums))

#You can also use len() on strings to return their length(character count)
str = "some text"
x = len(str)
print(x)

x = "abc"
x *= 2
print(len(x))

#

#The append() function is used to add an item to the end of the list
nums = [1, 2, 3]
nums.append(4)
print(nums)

#

#insert() inserts a new item at the given position in the list
words = ["Python", "fun"]
words.insert(1, "is")
print(words)

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

#

#index() finds the first occurance of a list item and returns its index.
letters = ['p', 'q', 'r', 's', 'p,' 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

#

#max(list) Returns the maximum value.
#min(list) Returns the minimum value.
x = [1, 8, 42, 3]
print(min(x))
print(max(x))

#

#list.count(ITEM) Returns a count of how many times an item occurs in a list.
#list.remove(ITEM) Removes an item from a list.
#list.reverse() Reverses items in a list.
x = [2, 4, 6, 7, 2, 9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)

#

#You are working on a queue management program.
#The queue is represented by a list.
#Write a program to take an input, add it to the end of the queue, and output the resulting list.

queue = ['John', 'Amy', 'Bob', 'Adam']
new = str(input())

queue.append(new)
print(queue)

#----------------------------------------------------

#You are analyzing a data set and need to remove the outliers (the smallest and largest values)
#The data is stored in a list.
#Complete the code to remove the smallest and largest elements from the list.
#Then output the sum of the remaining numbers.

data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 9, 100, 444, 78]

data.remove(min(data))
data.remove(max(data))

print(sum(data))

#- STRING FORMATTING ----------------------------------------

#Strings have a format() function, which enables values to be embedded in it, using placeholders.
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra","cad"))

#You can also name the placeholders instead of the index numbers.
a = "{x}, {y}".format(x = 5, y = 12)
print(a)

#

#join() joins a list of strings with another string as a seperator.
x = ", ".join(["spam", "eggs", "ham"])
print(x)

#

#split() is the opposite of join().
#It turns a string with a certain seperator into a list.
str = "some text goes here"
x = str.split(' ')
print(x)

#

#replace() replaces one substring in a string with another.
x = "Hello ME"
print(x.replace("ME", "world"))

#

#lower() and upper() change the case of a string to lowercase and uppercase.
print("This is a sentance.".upper())

print("AN ALL CAPS SENTANCE.".lower())

#

#Your friend sent you a message, howver his keyboard is broken and types a # instead of a space.
#Replace all of the # characters in the given input with spaces and output the result.
msg = input()
print(msg.replace("#", " "))

#------------------------

#You are making a word counter program.
#Given text as input, output the number of words it contains in the format given below.
# Input Example: Never give up
# Output Example: Number of words:3
text = input()

words = text.split(" ")
print("Number of words:", len(words))

#- FUNCTIONS ----------------------------

#You can create your own functions by using the def statement.
#Here's an example of a function named my_func. It takes no aruments, and prints "spam" three times.
def my_func():
    print("spam")
    print("spam")
    print("spam")
my_func()

#

#We have a function that outputs "Welcome, user" as it is called. 
#We want to make it more personalized, so redesign the given function so that it will take the name of the user as input and output the welcome message with it.
def welcome():
    print("Welcome, " + input())
welcome()

#

#A coffee vending machine makes 3 types of coffee:
#   1 - Americano
#   2 - Espresso
#   3 - Cappuccino
#Define the coffee() function to take the number from the customer as input and serve the corresponding coffee type.
#It should output Unknown if there is no match.
def coffee():
    choice = int(input())
    if choice == 1 :
        print("Americano")
    elif choice == 2:
        print("Espresso")
    elif choice == 3:
        print("Cappuccino")
    else :
        print("Unknown")
coffee()

#- ARGUMENTS -------------------------

#Functions can take arguments, which can be used to generate the function output.
def exclamation(word):
    print(word + "!")

exclamation("spam")

#You can call the same function with different arguments.
def exclamation(word):
    print(word + "!")
exclamation("spam")
exclamation("eggs")
exclamation("python")

#You can define functions with more than one argument; seperate them with commas.
def print_sum_twice(x, y):
    print(x +y)
    print(x + y)
print_sum_twice(5, 8)

#

#The given program defines a function printBill(),
#which takes one string argument and outputs formatted text.
#You need to take the user input and call the function by passing the input as its argument.
def printBill(text):
    print("======")
    print(text)
    print("======")

text = input()
printBill(text)

#

#A game machine has 5 games installed on it.
#Define the run() function that will take the given list of games and the N number as arguments,
# and output the corresponding game with the N index from the list.
#If the user enters a invalid number that is out of the list range, the program should output "Unknown".
games = ["Alien Shooter", "Tic Tac Toe", "Snake", "Puzzle", "Football"]

choice = int(input())

def run(games, choice) :
    if choice >= 0 and choice <=4 :
        print(games[choice])
    else :
        print("Unknown")
run(games, choice)

#- RETURNING FROM FUNCTIONS ---------------

def max(x, y):
    if x >= y:
        return x
    else:
        return y
    
if max(6, 4) > 10:
    print("Yes")
else:
    print("Nope")

#Once you return a value from a function, it immediately stops being executed.
#Any code placed after the return statement wont be executed.

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")
print(add_numbers(4, 5))

#A function can only return once, thus if you need to return miltiple values, you can use a list.

def double(a, b):
    return [a*2, b*2]

x = double(6, 9)
print(x)

#

#We need to calculate the area of a given rectangle. Your program needs to take the width and length as input and output the area of the rectangle.
#Complete the area function, which takes the length and width as arguments, to calculate and return the area.
#Then call the function for the given inputs.

def area(x, y):
    return x*y

w = int(input())
h = int(input())

print(area(w, h))

#

#You are creating your own social network application and need to write a hashtag generator program.
#Complete the given hashtag() function to return the input text starting with the hashtag(#)
#Also, if the user entered several words, the program should delete the spaces between them.
userText = input()

def hashtag(userText):
    text = userText.replace(" ", "")
    return "#" + text
print(hashtag(userText))

#

#You're working on a search engine. The given code takes a text and a word as input and passes them into a function called search().
#The search() function should return "Word found" if the word is present in the text, or "Word not found", if its not.

text = input()
word = input()

def search(text, word):
    for word in text :
        if word in text:
            print("Word found")
        else:
            print("Word not found")
search(text, word)

#

n = [2, 4, 6, 8]
res = 1
for x in n[1:3]
    res *= x
print(res)

#- DICTIONARIES --------------------------

#Dictionaries are another collection type and allow you to map arbitrary keys  to values.
#Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
ages = {
    "Dave" : 24,
    "Mary" : 42,
    "John" : 58
}
print(ages["Dave"])
print(ages["Mary"])

#

#You are working at a car dealership and store the car data in a dictionary.
#Your program needs to take the key as input and output the corresponding value.
car = {
    "brand" : "BMW",
    "year" : "2018",
    "color" : "red",
    "mileage" : 15000
}
print(car[input()])

#

#To determine whether a key ins in a dictionary, you can use in and not in, just as you can for a list.
nums = {
    1 : "one",
    2 : "two",
    3 : "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#

#A useful dictionary function is get, it does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead.
#You can determine how many items a dictionary has by using the len() function.
pairs = {
    1 : "apple",
    "orange" : [2, 3, 4],
    True : False,
    12 : "True"
}
print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

#

#You are working on data that represents the economic freedom rank by country.
#Each country name and rank are stored in a dictionary, with the key being the country name.
#Complete the program to take the country name as input and output its corresponding economic freedom rank.
#In case the provided country name is not present in the data, output "Not found".

data = {
    'Singapore' : 1,
    'Ireland' : 6,
    'United Kingdom' : 7,
    'Germany' : 27,
    'Armenia' : 34,
    'United States' : 17,
    'Canada' : 9,
    'Italy' : 74
}
print(data.get(input(), "Not found"))

#- TUPLES --------------------------

#Tuples are very similar to lists, except the are immutable (they cannot be changed).
#Also, they are created using parentheses, rather than square brackets.
words = ("spam", "eggs", "sausages")

#You can access the values in the tuple with their index, just as you did with lists.
print(words[0])

#Trying to reassign a value in a tuple causes an error.
#Like lists and dictionaries, tuples can be nested within each other.

#Tuples can be created without the parentheses by just seperating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0])

#

#You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.
#Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below.
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name = input()

for x in contacts :
    if name in x :
        print(str(x[0]) + "is" + str(x[1]))
        break
else :
    print("Not found")

#- TUPLE UNPACKING -------------------------

#Tuple unpacking allows you to assign each item in a collection to a variable.
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
#They can also be used to swap variables by doing a, b = b, a since b, a on the right hand side forms the tuple (b, a) which is then unpacked.

#A variable that is prefaced with an asterisk * takes all values from the collection that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

#

#Tuples can be used to output multiple values from a function.
#You need to make a function called calc() that will take the side length of a square as its argument and return the perimeter and area using a tuple.
#The perimeter is the sum of all sides, while the area is the square of the side length.

def calc(x) :
    #your code goes here
    return(x*4, x*x)


side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))

#- SETS -----------------------

#Sets are similar to lists or dictionaries.
#They are created using curly braces, and are unordered, which means that they cant be indexed.
#Due to the way they're stored, its faster to check whether an item is part of a set using the in operator, rather than part of a list.
#Sets cannot contain duplicate elements.
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)

#You can use the add() function to add new items to the set, and remove() to delete a specific item.
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
#Duplicate items will automatically get removed from the set.
#The len() function can be used to return the number of items in a set.

#Sets can be combined using mathematical operations.
#The union operator | combines two sets to form a new one containing items in either.
#The intersection operator & gets items only in both.
#The difference operator - gets items in the first set but not in the second.
#The symmetric difference operator ^ gets items in either set, but not both.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

#

#You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
#The skills required for the job, and the candidates skills are stored in sets.
#Complete the program to output the matched skill.
#!You can use the intersect operator to get the value in both sets!#

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills & job_skills)[0])
#Putting it into list and printing position 0 prints it nice and neat without the '' or {}

#- LIST COMPREHENSIONS --------------------- ASK JACOB

#List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
cubes = [i**3 for i in range(5)]
print(cubes)

#ASK JACOB
#A list comrehension can also contain an if statement to enforce a condition on values in the list.
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#ASK JACOB

#Given a word as input, output a list containing only the letters of the word that are not vowels (a, e, i, o, u).
#!Use a list comprehension to create the required list of letters and output it.!#
word = input()
vowels = {'a', 'e', 'i', 'o', 'u'}

a = [i for i in word if i not in vowels]
print(a)

#- SUMMARY OF CHAPTER ----------------
'''
'''
list[] = mutable, can be modified
dictionary{} = (represented as {key:value})mutable, can be modified
set{} = immutable, cannot be modified 
tuple() = immutable, cannot be modified
'''
'''
When to use dictionary:
-When you need a logical association between a key:value pair.
-When you need fast lookup for your data, based on a custom key.
-When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
-Use lists if you have a collection of data that does not need random access.
Try to choose lists when you need a simple, iterable collection that is modified frequently.
-Use a set if you need uniqueness for the elements.
-Use tuples when your data cannot/should not change.
#!Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because its immutable.!#


nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
#BREAKDOWN#
#We will start with nums[:2] which is asking for every item in the set nums, up to the second index; because, nums[start:stop:step]
#We are now left with a shortened list of (55, 44)
#Next we are asking for the minimum of our new set, writen now as min(55, 44), which is 44.
#Our print statement would read print(max(44, abs(-42))), they did not mention the abs() function but it does mean absolute.
#The absolute of -42 is 42, our print statement now calls for print(max(44, 42)) with an output of 44.

#- FUNCTIONAL PROGRAMMING -------------------

#Functional programming is a style of programming that (as the name suggests) is based around functions.
#A key part of functional programming is higher-order functions.
#Higher-order functions take other functions as arguments, or return them as results.

def apply_twice(func, arg) :
    return func(func(arg))

def add_five(x) :
    return x + 5

print(apply_twice(add_five, 10))
#! The function apply_twice(func, arg) takes another function as its argument, and calls it twice inside its body. !#

def test(func, arg) :
    return func(func(arg))

def mult(x) :
    return x * x

print(test(mult, 2))

#! BREAKDOWN !#
#test and mult - are function names.
#func, arg - are the names of the arguments.

#print function asks us to output test function with the given arguments: mult, 2
#If we do this we get:
#   def test(mult,  2):
#       return mult(mult(2))
#This now asks us to do the mult function twice, since there are 2 names of the second function present.
#If we do this we get:
#   1. 2 * 2 = 4
#   2. 4 * 4 = 16
#Therefore, the answer is 16.

#Functional programming seeks to use pure functions.
#Pure functions have no side effects, and return a value that depends only on their arguments.
#This is how functions in math work: EXAMPLE, the cos(x) will for the same value of x, always return the same result.

#PURE FUNCTION:
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

#IMPURE FUNCTION:
some_list = []

def impure(arg) :
    some_list.append(arg)
#! The function above is impure, because it changed the state of some_list. !#

#Using pure functions has both advantages and disadvantages.
#Pure functions are:
#-Easier to reason about and test.
#-More efficient, since once the function has been evaluated for an input, the result can be stored and referred to the next time that input is needed.
#Reducing the number of times the function is called. This is called memorization.
#-Easier to run in parallel.

#- LAMBDAS -----------------

# Creating a function normally using def assigns it to a variable with its name automatically.
#Python allows us to create functions on the fly, provided that they are created using lambda.
#This approach is most commonly used when passing a simple function as an argument to another function.
#The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.

def my_func(f, arg) :
    return f(arg)

my_func(lambda x: 2*x*x, 5)
#! Functions created using the lambda syntax are known as annonymous. !#

#Lambda functions arent as powerful as named functions.
#They can only do things that require a single expression - usually equivalent to a single line of code.

#

#You are given code that should calculate the corresponding percentage of a price.
#Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
#Fix the code to output the given percentage of the price.

price = int(input())
perc = int(input())

res = (lambda x,y:x*y/100)(price, perc)

print(res)

#- MAPS -------------------------------

#The built in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
#The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.
def add_five(x) :
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#You can achieve the same result by using lambda syntax.
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#

#You work on a payroll program. Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
#Output the resulting list.
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
salaries = list(map(lambda x : x + bonus, salaries))
print(salaries)

#The function filter filters an iterable by leaving only the items that match a condition (also called a predicate).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x : x%2==0, nums))
print(res)
#! Like map, the result has to be explicitly converted to a list if you want to print it. !#

#Extract all items less than 5 from the list.
nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x : x < 5, nums))
print(res)

#- GENERATORS ------------------------

#Generators are a type of iterable, like lists or tuples.
#Unlike lists, they dont allow indexing with arbitrary indices, but they can still be iterated through for loops.
#They can be created using functions and the yield statement.

def countdown() :
    i = 5
    while i > 0 :
        yield i
        i -= 1

for i in countdown() :
    print(i)
#! The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying variables. !#

#

#Finding prime numbers is a common coding interview task.
#The given code defines  a function isPrime(x), which returns True if x is prime.
#You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the isPrime() function
# to output the prime numbers in the given range (between the two arguments).

# ASK JACOB #

def isPrime(x) :
    if x < 2 :
        return False
    elif x == 2 :
        return True
    for n in range(2, x) :
        if x % n == 0 :
            return False
    return True

def primeGenerator(a, b) :
    #Your code goes here
    for number in range(a, b) :
        if isPrime(number) :
            yield number

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

for i in range(10):
    if not i % 2 == 0:
        print(i + 1)

#- DECORATORS ------------------------ ASK JACOB

#Decorators provide a way to modify functions using other functions.
#This is ideal when you need to extend the functionality of functions that you dont want to modify.

def decor(func) :
    def wrap() :
        print("======")
        func()
        print("======")
    return wrap

def print_text() :
    print("Hello World!")

decorated = decor(print_text)
decorated()

#We defined a function named decor that has a single parameter func.
#Inside decor, we defined a nested function named wrap.
#The wrap function will print a string, then call func(), and print another string.
#The decor function returns the wrap function as its result.

#
'''
#You are working on an invoice system.
#The system has an already defined invoice() function, which takes the invoice number as an argument and outputs it.
#You need to add a decorator for the invoice() function that will print the invoice in the following format:
#Sample input: 42
#
#Sample output:
#***
#INVOICE #42
#***
#END OF PAGE

def decor(func):
    def wrap(num):
        print('***')
        func(num)
        print('***')
        print('END OF PAGE')
    return wrap

@decor
def invoice(num):
    print('INVOICE #' + num)

invoice(input())