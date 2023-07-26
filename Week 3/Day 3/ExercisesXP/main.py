# Exercise 1: Currencies
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
        
    def __int__(self):
        return self.amount
        
    def __repr__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"        

    def __add__(self, other):
        if type(other) ==int:
            return self.amount+other
        else:
            if other.currency ==self.currency:
                return self.amount + other.amount
            else:
                message = f"TypeError Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                return(message)
            
            
    def __iadd__(self, other):
        if type(other) ==int:
            return Currency(self.currency, self.amount + other)
        else:
            if other.currency ==self.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                message = f"TypeError Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                return(message)
                 

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))

print(c1 + 5)
print(c1 + c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)


# Exercise 3: Random Module
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random
def random_number():
    random_number = random.randint(1,100)
    my_number=int(input("Enter number 1..100\n"))
    if 1> my_number >100:
        print("Incorrect number") 
    else:
        if my_number == random_number:
            print("We have the same number! Gongrats!")
        else:
            print("You do not guessed, maybe next time!")            
            pass         
  
random_number()  
 
# Exercise 4: String Module
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string

def random_string(lenght):    
    random_string =''.join(random.choices(string.ascii_letters, k=lenght))    
    return random_string

random_string = random_string(5)
print(random_string)


# Exercise 5 : Current Date
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime

def current_date():
    current_date = datetime.date.today()
    print("Current date:", current_date)

current_date()


# Exercise 6 : Amount Of Time Left Until January 1st
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def hny_datetime():
    
    # hny_datetime = 
    current_datetime = datetime.datetime.now()
    target_datetime = datetime.datetime(2024, 1, 1)
    # print(current_datetime)
    # print(target_datetime)
    
    time_left = target_datetime - current_datetime
    print(time_left)
    
    
    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)    
  
    
  

    time_left_str = f"{days_left} days and {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d} hours"
    print("The 1st of January is in", time_left_str)

# Exercise 7 : Birthday And Minutes
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

    
hny_datetime()

def minutes ():
    print("Enter your Birthday")
    year=int(input("Enter the year  "))
    month=int(input("Enter the month  "))
    day=int(input("Enter the day  "))
    birthday = datetime.datetime(year, month, day)
       
    current_datetime = datetime.datetime.now()

    time_lived = current_datetime - birthday
    print(time_lived)
    minutes_lived = time_lived.total_seconds() / 60
    return int(minutes_lived)

minutes = minutes()
print(f"You have lived {minutes} minutes.")

# Exercise 8 : Faker Module
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker
fake = Faker()
users = []

# Function to add new dictionaries to the users list with fake data
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code(),
    }
    users.append(user)
for _ in range(10):
    add_user()

print(users)