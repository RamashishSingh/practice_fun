def multiply_by2(li):
    new_li =[]
    for i in li:
        new_li.append(i*2)
    return new_li
print(multiply_by2([1,2,4,5]))

#----------------------------------------------------------------------------------------------------------------------
# MAP - map the list and perform the action on iteration

def multiply_by2(li):
    return li*2
print(map(multiply_by2,([1,2,4,5])))

print(list(map(multiply_by2,([3,7,4,9]))))

#-----------------------------------------------------------------------------------------------------------------------

#Filter - check the bool if it is true then it append it to list

def only_odd(li):
    return li%2 != 0

print(list(filter(only_odd,[7,4,3,2,5,43,12])))

#-----------------------------------------------------------------------------------------------------------------------

# ZIP - zip the iterables as their index like zip (0,0) (1,1)

li = [1,2,3,4,5]
names = ['Ram','Shiv','Nik','rik','jik']

print(list(zip(li,names)))

#-----------------------------------------------------------------------------------------------------------------------

# REDUCE - reduce and have to import from functools and used like = reduce(function,iterables,strarting number)

from functools import reduce
my_li = [2,5,6]

def accumlator(acc,item):
    print(acc,item)
    return acc +item

print(reduce(accumlator,my_li,1))

#-----------------------------------------------------------------------------------------------------------------------

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capital(li):
    return li.capitalize()

print(list(map(capital,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_numbers,my_strings)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_score(li):
    return li >50

print(list(filter(filter_score,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
for i in my_numbers:
    scores.append(i)

def total(acc,li):
    print(acc,li)
    return acc+li
print(reduce(total,scores))
print(scores)

#-----------------------------------------------------------------------------------------------------------------------

# LAMBDA FUNCTION - it is like a function which has to run only once so no need to store on memory just take action once
# like you want to multiply a list with 3 only one time so use lambda expression

myls1 = [2,3,5,6,9]

# Map with lambda expression but run only once
print(list(map(lambda item: item*3,myls1))) # see this it didnot take the memory it runs only once

# filter with lambda expression
print(list(filter(lambda item: item%2==0,myls1))) # see this it didnot take the memory it runs only once

# reduce with lambda expression
print(reduce(lambda acc,item: acc+item,myls1)) # see this it didnot take the memory it runs only once

#-----------------------------------------------------------------------------------------------------------------------

# Excercise find square of list using lambda expression

list3 = [3,6,7,3,2]

print(list(map(lambda item:item**2,list3)))

# exercise 2 sort the list with tuple 2nd item

list2 = [(0,2),(4,3),(9,9),(10,-1)]

#list2.sort(reverse=-1)
#print(list2)

#with lambda
list2.sort(key=lambda x:x[1])
print(list2)

#-----------------------------------------------------------------------------------------------------------------------

# COMPREHENSION - EASILY CREATE LIST SET AND DICTIONARY LIKE

list_1 = [char for char in 'hello']
list_2 = [num for num in range(0,100)]
list_3 = [num**2 for num in range(1,50)]
list_4 = [num**2 for num in range(1,50) if num%2 ==0]

# above created list without using more lines of code this is list comprehension and set and dictinary comprehension are same
print(list_1)
print(list_2)
print(list_3)
print(list_4)

# set comprehension are same as list only change the {} brackets
# Dictionary comprehension
simple = { 'a':1 , "b":4}
dict1 = {k:v**2 for k,v in simple.items() }
dict2 = {k:v**2 for k,v in simple.items() if v%2==0}
dict3 = {num:num*3 for num in [1,2,3]}
print(dict1)
print(dict2)
print(dict3)

#-----------------------------------------------------------------------------------------------------------------------

# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
#
# print(duplicates)

# do same with list comprehension
dublicates = list({i for i in some_list if  some_list.count(i)>1 })
print(dublicates)

#-----------------------------------------------------------------------------------------------------------------------

#  DECORATOR - add extra functionality to functions

def my_decorator(func):
    def wrap():
        print('***********')
        func()
        print('***********')
    return wrap

@my_decorator  # it simply means my_decorator(hello)()
def hello():
    print('hellloo')

@my_decorator
def bye():
    print('BYeeeeee')

hello()
bye()

# Basic idea where to use decorators like to calculate time for a calculation
from time import time
def time_taken(func):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'time taken {t2-t1}s')
        return result
    return wrapper

@time_taken
def performance():
    for i in range(1000000000):
        i*5

performance()

# Exercise of decorator
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args,**kwargs):
      if args[0]['valid'] == True:
          return fn(*args,**kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)