# In python we didn't have switch statement we have use switcher which change number into string using dictionary

my_dict = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four'
}

num = int(input("enter a number between 1-4"))
print('You Enter',my_dict.get(num,"Invalid number enter in between 1-4"))