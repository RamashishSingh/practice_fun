# ERROR HANDLING

# Error - we get so much error when we do something wrong or user input is wrong like
# key error, value error, division error, type error so using error handling we can make error not to stop program using try except
#
# while True:
#     try:
#         age = int(input('enter your age'))
#         print(age)
#         print('thank you')
#         break
#     except:
#         print('enter a number')
#
# # we can make separate error message for different error
# while True:
#     try:
#         age = int(input('enter your age'))
#         print(10/age)
#         break
#     except ValueError:
#         print('enter a number')
#     except ZeroDivisionError:
#         print('number greater than zero 0')
#
# # error handlinng and print error also without stoping program
#
# def sum(n1,n2):
#     try:
#         return n1/n2
#     except (TypeError,ZeroDivisionError) as err:
#         print(f'you have error {err}')
#
# print(sum('1','2'))

# we can use raise for throwing the errors manually

#------------------------------------------------------------------------------------------------------------------------------------------

#GENERATORS - it allow us to generate the sequence of value over time like range is a generator

# note - every generator is iterable but every iterable is not generator
# generator is subset of iterable
# like list is iterable but it is not generator

def generator1(num):
    for i in range(num):
        yield  i*2  # here yield pause the iteration and resume when next is asked or called and it didn't take memory for num as given it
                    # take 1 value memory where yield is paused and when used then memory removed
g = generator1(100)
next(g)
next(g)
next(g)
print(next(g))

for item in generator1(100):
    print(item) # here you see 1 valur at a time and only that memory takes memory

#----------------------------------------------------------------------------------------------------------------------------------------------

# FIBONACI SERIES
a =0
b = 1
n = int(input('enter a number from where you want to find fibonacci \n'))
print(a)
print(b)
for i in range(1,n):
    sum = a+b
    a = b
    b = sum
print(sum)

# FIBONACCI with generator

def fib_generator(num):
    c = 0
    d = 1
    for j in range(num):
        yield c
        sum1 = c
        c = d
        d = sum1 + c

for k in fib_generator(21):
    print(k)
