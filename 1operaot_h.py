# Ternary operator
# condition_if_true if condition else condition_if_false
get = True
min = 'Message me ' if get else 'Dont message'
print(min)

#-______-------------------------------------------------------------------------------------------------------------------
#Sort Curciting
# when we use ' and ' between conditions then it check first condtion if it is false then it is not going to check other
# it simply return false so this is sort curcuiting

#--------------------------------------------------------------------------------------------------------------------------

# Logical operator
# <, >, ==, <=, >=, !=, and , or , not
#--------------------------------------------------------------------------------------------------------------------------

# task small
is_magician = True
is_expert = True

if is_magician and is_expert:
    print('you are trained and expert go onn')
elif is_magician and not is_expert:
    print('atleast you are their')
else :
    print('you need maagic power')

#_------------------------------------------------------------------------------------------------------------------------
# Difference between == and is
# == compare the value if needed type conversion is also done
# but is compare the address of the element if same then True else False

#-------------------------------------------------------------------------------------------------------------------------

# LOOPS
# 1. For Loops
for i in [1,2,3,4,5]:
    for j in ['a','b','c','d','e','f']:
        print(i , j)

#another
user = {
    'name' : 'Golem',
    'age' : 5000,
    'group' : 'adult'
}
for i in user:
    print(i)
for j in user.items():
    print(j)
for k in user.keys():
    print(k)
for key,value in user.items():
    print(key,value)
#-----------------------------------------------------------
#task
# create list of numbers and find sum of all elements
my_list = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in my_list:
    sum = sum + i
print(sum)
#-----------------------------------------------------------------------------------------------------------------------
# enumerate = return value and idex in the itertion
for i,v in enumerate('hello'):
    print(i ,v)

# task find the index of number 50 in range of 100 numbers
for j,l in enumerate(range(1,100)):
    if l ==50:
        print('index of number 50 is : ',j)

#------------------------------------------------------------------------------------------------------------------------
# WHILE LOOPS - it loops over till the given condition get false
i = 0
while i<50:
    print(i)
    i += 1
else: # here we can think why we used else we can simply write print statement outside while loops
    print('all work done') # so we write else because it will run if while loops runs succesfully and then get false if their is break in while
                          # then else is also not run


#--------------------------------------------------------------------------------------------------------------------------
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for image in picture:
    for pixel in image:
        if pixel ==0:
            print(' ',end ='')
        else:
            print('1',end ='')
    print('')
#-----------------------------------------------------------------------------------------------------------------------
# Excerecise
# find and print dublicates from the list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dub =[]
for i in some_list:
    if some_list.count(i) > 1 :
        if i not in dub:
            dub.append(i)
print(dub)
#--------------------------------------------------------------------------------------------------------------------------
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge(age = 0):
    if int(age) < 18:
	    print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
	    print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")




#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


age = input("What is your age?: ")
checkDriverAge()

#------------------------------------------------------------------------------------------------------------------------
#task - find out largest even number from list
def highest_even(li):
    high = 0
    for i in li:
        if i %2==0:
            if i > high:
                high = i
    return high
print(highest_even([10,2,3,11,40,8]))

#------------------------------------------------------------------------------------------------------------------------
# WALRUS OPERATOR  ':=' = assignes values to the variable as part of a larger expression
m = 'hellloooolllooo'
if ((n := len(m)) > 10 ): # we have used walrus operator because now we have to calcuate len() only one times 
    print(f'so it is {n} letters long')


