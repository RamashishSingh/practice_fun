number = int(input('enter a number for multiplication table'))
for i in range(1,11):
    print(f'{number} * {i} = {number*i}')

# write a code for print table for a given range of numbers

num1 = int(input('enter a number for multiplication table'))
num2 = int(input('enter a number for multiplication table'))

for i in range(num1,num2):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print('\t')