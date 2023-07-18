# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = input("Enter a word: ")
my_list = {}

for index, letter in enumerate(word):
    if letter not in my_list:
        my_list[letter] = [index]
    else:
        my_list[letter].append(index)

print(my_list)


# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}

wallet = "$500"
wallet_amount = int(wallet[1:])


# !!!!!!!!!!!!
import random
# Get 5 random items from the dictionary
# Get 5 random items from the dictionary along with their prices
random_items = random.sample(list(items_purchase.items()), k=5)
print(random_items)

affordable_items = []

for item, price in random_items:
    item_price = int(price[1:].replace(',', ''))
    if item_price <= wallet_amount:
        affordable_items.append((item, price))


affordable_items.sort()
print(affordable_items)