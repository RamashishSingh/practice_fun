import sys
import random
while True:
    try:
        no = int(input('enter your guess   : '))
        ans = random.randint(int(sys.argv[1]), int(sys.argv[2]))
        if int(sys.argv[1]) <= no <= int(sys.argv[2]):
            if no == ans:
                print('you are good')
                break
            else:
                print('try again')
                continue
        else:
            print(f'enter a number between {int(sys.argv[1])} to {int(sys.argv[2])}')
    except ValueError:
        print('enter a number')