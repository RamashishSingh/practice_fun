num = int(input('enter a number for checing odd and even '))

if num >1:
    if num%2 ==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
else:
    print('please enter number greater than 1')