# OOP - Object Oriented Programming
class PlayerCharacter:
    membership = True # Attributes and these are static attribute
    def __init__(self,name,age):
        if self.membership: # here we can use PlayerCharacter.membership because membership is static
            self.name = name # Attribute and these attributes are dynamic
            self.age = age # but here we cannot write as PlayerCharacter.age bcz it is dynamic and age is not PlayerCharacter attribute it is
                           # Constructor or __init__ attribute

    def run(self):
        print(f'run {self.name} and go fast  as you are {self.age} years old')


player1 = PlayerCharacter('Ram',23)
print(player1.age)
print(player1.name)
player1.run()

#------------------------------------------------------------------------------------------------------------------------------------------
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age




# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('catty',3)
cat2 = Cat('fatty',2)
cat3 = Cat('matty',5)

# 2 Create a function that finds the oldest cat
def oldest(*age):
    return max(age)
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is  {oldest(cat1.age,cat2.age,cat3.age)}years old.')

#--------------------------------------------------------------------------------------------------------------------------------------------

# ENCAPTULATION - binding of data in one place like class from where we can use the attributes and method of the class
class PlayerCharacter:
    membership = True # Attributes and these are static attribute
    def __init__(self,name,age):
        if self.membership: # here we can use PlayerCharacter.membership because membership is static
            self.name = name # Attribute and these attributes are dynamic
            self.age = age # but here we cannot write as PlayerCharacter.age bcz it is dynamic and age is not PlayerCharacter attribute it is
                           # Constructor or __init__ attribute

    def run(self):
        print(f'run {self.name} and go fast  as you are {self.age} years old')


    @classmethod   # Here we can see that in class method we can instanciate with class and use its methods
    def summing(cls,n1,n2):
        return cls('manny',n1+n2)

    @staticmethod  # Here in static we cannot use the class method it is only for doing some task as written
    def summing1(n1,n2):
        return n1+n2

player1 = PlayerCharacter('Ram',23)
print(player1.age)
print(player1.name)
player1.run()

player2 = PlayerCharacter.summing(3,5)
player2.run() # it is classmethod and it is running run method from class PlayerCharacter in this it cares about class attributes

player3 = PlayerCharacter.summing1(3,6)
print(player3) # but in this it is static so it cannot use class methods and in this it didnot care about class attributes

#-----------------------------------------------------------------------------------------------------------------------------------------


# ABSTRACTION - hiding the information and getting axis to information which is necessary
# like when we run the code player2.run() we dont need to know what it is doing backside it only shows which is necessary
player2.run()
#it shows output which is needed and abstract which is not asked  "run manny and go fast  as you are 8 years old"


#------------------------------------------------------------------------------------------------------------------------------------------


# INHERITANCE - Parent Child policy
class User(): # Parent class
    def sign_in(self):
        print('logged IN')

class Wizard(User): # Child class as it is using parent class User in it
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with my  {self.power}% power ')


class Archer(User):
    def __init__(self, name, no_bows):
        self.name = name
        self.no_bows = no_bows

    def attack(self):
        print(f'attacking with my bows and  {self.no_bows} bows left ')
        self.no_bows -= 1

wizard1 = Wizard('wizzy',50)
archer1 = Archer('archy',100)

wizard1.attack()
archer1.attack()


#-------------------------------------------------------------------------------------------------------------------------------------------------

# POLYMORPHISM - Many forms

class User():
    def sign_in(self):
        print('logged IN')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with my  {self.power}% power ')


class Archer(User):
    def __init__(self, name, no_bows):
        self.name = name
        self.no_bows = no_bows

    def attack(self):
        print(f'attacking with my bows and  {self.no_bows} bows left ')
        self.no_bows -= 1

wizard1 = Wizard('wizzy',50)
archer1 = Archer('archy',100)

def player_attack(cahr): # here we make a function which take char and run attack with different functions attack
    cahr.attack()

player_attack(wizard1)
player_attack(archer1)


#-----------------------------------------------------------------------------------------------------------------------------------------

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Mally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#2 Create a list of all of the pets (create 3 cat instances from the above)
c1 =Simon('jizy',4)
c2 =Sally('mizzy',2)
c3 = Mally('lozzy',1)
my_cats = [c1,c2,c3]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

#-----------------------------------------------------------------------------------------------------------------------------------

# MULTIPLE INHERITANCE


class User():
    def sign_in(self):
        print('logged IN')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with my  {self.power}% power ')


class Archer(User):
    def __init__(self, name, no_bows):
        self.name = name
        self.no_bows = no_bows

    def no_arrows(self):
        print(f'attacking with my bows and  {self.no_bows} bows left ')
        self.no_bows -= 1

class HyBorg(Wizard,Archer):
    def __init__(self,name,power,no_bows):
        Archer.__init__(self,name,no_bows)
        Wizard.__init__(self,name,power)

hb1 = HyBorg('borgy',50,90)
hb1.attack()
hb1.no_arrows()
hb1.sign_in()