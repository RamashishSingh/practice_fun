n1 = 45
n2 = 63
sum = n1 + n2
mul = n1 * n2
print(f'Sum = {sum} and multiply = {mul}')

#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
prev = 0
print(f'sum of 0 and previous node {prev} = {prev}')
for i in range(1,11):
    print(f'sum of {i} and previous node {prev} = {i+prev}')
    prev = i

# write a fibonaci series
a = 0
b = 1
for i in range(10):
    if i==0:
        sum = 0
        print(f'sum of {i} and {i} = {sum} ')
    else :
        sum = a+b
        a = b
        b = sum
        print(f'sum of {i-1} and {i} = {sum}')

# Write a program to accept a string from the user and display characters that are present at an even index number.
str = input('enter a word  : ')
for i in str:
    if index(i) %2==0:
        print(i)