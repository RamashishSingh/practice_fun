my_file = open('test.txt')

print(my_file.read()) # it will read all file at once and it is like cursour like reading so we seek to 0 line to read again

my_file.seek(0)

print(my_file.readline()) # it will read line by line
print(my_file.readline())

# if we want all lines details in list so used name.readlines()
my_file.seek(0)
print(my_file.readlines())

# when your work is done then close the opened file to free up the space
my_file.close() # this is a problem we have to close the file when using so lets so it in simple way


# with this we can rid of closing file again and again
# with open('test.txt',mode='a') as my_file: # but with this append i cann't read the file data it only append and in mode we have r+ = read + write , w = write,a = append
#     # in w =write it rewrite the file as new every time
#     # in r+  it overwrite because every time it read file cursour at starting and overwrite the text
#     # in a it append the text in file
# #    my_file.write('he i am writing from the python ide not from txt ')
#     #print(my_file.read())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# excercise make a translator
from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./test.txt',mode = 'r') as translator1:
        text = translator1.read()
        translation = translator.translate(text)
        print(translation)
except :
    print('check the path')


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# REGULAR EXPRESSION - matching the pattern

import  re

string = 'this is a string which we are going to to test in re to find string'

a = re.search('this',string)
print(a)
print(a.span()) # .span will return the starting and ending index what you search
print(a.start()) # it will show the starting index of searched word
print(a.end()) # it will shoe what is the serached word end index
print(a.group()) # it will show the word what we searched and it matched

# another method to search the word first compile then search
pattern = re.compile('string')
b = pattern.search(string)
print(b.group())
c = pattern.findall(string) # it will print the word how many times it is in the string
print(c)
d = pattern.fullmatch(string) # it will check that the whole string is same as written then it will return true
print(d)
e = pattern.match(string) # it will just check that from begining it is matching or not
print(e)

# In REGULAR EXPRESSION we have some extra features to check the pattern matcching lets check for above one

pattern1 = re.compile(r'.*')
f = pattern1.search(string)
print(pattern1.fullmatch(string)) # and we have checked that .* means accept all things

#--------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise make a program that check that given email format is correct or not

email = input('enter your email \n')

matching = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$')
matched = matching.search(email)
if matched:
    print('correct eamil format')
else:
    print('wrong email format')


#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exercise make a password checked that it should be minimum 8 character

password = input('enter password \n')

try_match = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[/]:;<>,.?/~_+-=|]).{8,32}$')
success_match = try_match.search(password)
if success_match:
    print(' fullfill password crieteria')
else:
    print('enter a valid password')