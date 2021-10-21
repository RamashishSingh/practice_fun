# list container of objects if different data types
li = [23,5,234,7,3,97,34,87]

li[4]

#List Slicing
print(li[0:3])
print(li[:])
print(li[0::2])
print(li[0:3:1])
print(li[::-1]) #reverse the list

new_list = li # because it is not copy it is doing work on original list
li[0] = 98
print(new_list)
print(li) # here we see that original list is also changed which is done in new list

# for avoiding this type of errors we can make copy of list using [:]
new = li[:]
new[0] = 65
print(new)
print(li) # not changed in original

# Matrix
list = [[1,2,4],
        [3,6,7],
        [56,87,2]]
print(list[1][2]) # like this we can select from matrix

list1 = [[1,0,1],
         [0,1,0],
         [1,0,1]]
for i in list1:
    for j in i:
        if j == 1:
            print('\033[31m0\033[0m',end ='')
        else:
            print(' ',end ='')
    print()


#list methods
list1 = ['hello','kill','dil ','full']
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.pop()
print(list1)
list1.append('gill gill')
print(list1)
list1.remove('dil ')
print(list1)

print('full' in list1)


list2 = '!'
ls1 = list2.join(list1)
print(ls1)

# List Unpacking
a,b,c,*ot,d = [1,2,3,4,6,7,8,9,2,1,324,56,76]
print(a)
print(b)
print(c)
print(ot)
print(d)

#--------------------------------------------------------------------------------
# DICTIONARY DATA TYPE  = it is a unordered key value pair

dictionary  = {
'a' : 'hello',
'b' : 'my numbers',
'c' : [1,2,3,4],
'f' : 32
}
print(dictionary)
print(dictionary['a'])
print(dictionary['c'][2])

# Dictionary methods
print(dictionary.get('d')) # it check is their is d key in dictinory if not return None
print(dictionary.get('e',20))# if e is not their it will return default value
print(dictionary.get('f',54)) # if it has the key f then it didn't return default it will return original value

# Another way to create dict
user = dict(name = 'Ram',country = 'INDIA')
print(user)

print('a' in dictionary)
print('a' in dictionary.keys())
print('hello' in dictionary.values())
print((dictionary.items()))
print(user.clear())
print(user)
print(dictionary.pop('a'))
print(dictionary)
print(dictionary.update({'b' : 'willow'}))
print(dictionary)

#--------------------------------------------------------------------------------------------------------------------
# TUPLES DATA TYPES - It is like list but it is not mutable
tup = (1,2,4,4,4)
print(tup)

# Tuples method
print(tup.count(4))
print(tup.index(2))

print('6' in tup)

#---------------------------------------------------------------------------------------------------------------------
# SETS DATA TYPE - It is unordered unique elements
se = {1,2,3,4,5,5}
se1 = {4,7,8,11,3,443,56}
print(se)
# it is unordered so no indexing
#set methods
print(se.add(8))
print(se.difference(se1))
print(se1.difference(se))
print(se.discard(5))
print(se)
# print(se.difference_update(se1)) # it will remover common elements from set
# print(se)
print(se.intersection(se1)) #printed  intersection value
print(se.isdisjoint(se1)) # retuen false because they have some element are common so their is no disjoint
print(se.issubset(se1)) # se is not a subset of se1
print(se.issuperset(se1)) # se is not superset of se1
print(se.union(se1)) # add all element in se which is not in se
