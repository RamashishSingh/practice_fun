a = 'mum sum '
b = 'lum sum'
print(f'it is in rymes {a} and {b}')
print('it is in rymes {} and {}'.format(a,b))
print('it is in rymes {0} and {1}'.format(a,b))
print('it is in rymes {1} and {0}'.format(a,b))

print('it is in rymes {a} and {b}'.format(a= 'hum',b = 'dum')) # in .format we can change or initialise the variable value


# string indexing
a[3]
a[-1]

# String slicing variable[start:stop:step]
print(a[:])

print(a[1:])

print(a[:6])

print(a[0::2])

print(a[:5:2])

print(a[::-1]) # reverse the string

print(a[::-2]) # reverse the string with setp 2

#Built in function & methods
# function are block off code runs when called
# method are the specific function for a object
# lets see on string
c = '100'
d = int(c) # here int() and print() is built in function
print(d)
d = 'lower h upper karna h'
print(d.upper()) # .upper() is a method for string object which is called with '.' operatot
print(d.capitalize())
print(d.find('u'))
# Important note string is imutable so these methods are creating copy and with operation done
print(d) # it is same no changes done by methods


# Exercise on string take input of name and password and show password length and pasword with stars
name = input('enter your name : ')
password = input('enter password : ')
length = len(password)
password_encyp = '*'*length
print(f'your password is {password_encyp} and it is {length} long')