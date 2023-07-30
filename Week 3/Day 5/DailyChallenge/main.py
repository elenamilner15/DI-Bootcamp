# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.


import random
import requests
import time


def find_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        load_time = end_time - start_time
        return load_time
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the page: {e}")
        return None


websites = ["https://www.google.com",
            "https://www.ynet.co.il", "https://www.imdb.com"]

for url in websites:
    load_time = find_load_time(url)
    if load_time is not None:
        print(f"{url} loaded in {load_time:.2f} seconds")

# Daily Challenge: OOP Quizz
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# Class is a template definition of the methods and variables in a particular kind of object. Where an object is a specific instance of a class; it contains real values instead of variables. The class is one of the defining ideas of object-oriented programming.

# What is an instance?
# An instance is realization of the object, it is a concrete occurrence of a class.

# What is encapsulation?
# Encapsulation refers to the packaging of data and functions that represent an embodiable (real world) entity into a programmable enclosure (commonly classes/objects). By encapsulating data, you can control its access and modification through methods, which helps in hiding the internal implementation details and preventing unauthorized access to the data.


# What is abstraction?
# Abstraction is a concept to describe things in simple terms.
# Abstraction displaying essential information and hiding unnecessary implementation details.

# What is inheritance?
# It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.

# What is multiple inheritance?
# Multiple inheritance means that  a subclass can inherit from two or more classes (superclasses)

# What is polymorphism?
# Polymorphism is the ability of a class or method to take on multiple forms. It allows objects of different classes to be treated as objects of a common superclass, thus enabling a single interface to represent various types.

# What is method resolution order or MRO?
# Method Resolution Order (MRO) is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.

#!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print("Something is missing")

    def deal(self):
        card = self.cards.pop()
        return card


deck = Deck()
deck.shuffle()


my_card = deck.deal()
print(f"Dealt: {my_card}")
