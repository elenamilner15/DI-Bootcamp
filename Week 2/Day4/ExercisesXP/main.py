# Exercise 1 : What Are You Learning ?

# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def display_message ():
    message = "I am learning HTML, CSS, Python, JavaScript etc.."
    print(message)
    
display_message()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Exercise 2: What’s Your Favorite Book ?

# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def favorite_book(title):
    message = f"One of my favorite books is {title}"
    print(message)

favorite_book("1984")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Exercise 3 : Some Geography

# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def describe_city(city, country):
    message = f"{city} is in the {country}"
    print(message)

describe_city("Bat-Yam", "Israel")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# Exercise 4 : Random

# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import random
def numbers(input_num, gen_num):
    if input_num == gen_num:
        message = f"It is a same number {input_num}"
    else:
        message = f"Numbers are different. Your number is {input_num} and our number is {gen_num}"
    print(message)

input_num = input("Enter a number from 1 to 100\n")
gen_num = random.randint(1, 100)

numbers(input_num, gen_num)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Exercise 5 : Let’s Create Some Personalized Shirts !

# Write a function called make_shirt() 

# that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def make_shirt(size="L", text="I love Python"):
    message = f"The size of the shirt is {size} and the text is {text}"
    print(message)


size = input("Enter your size as XS, S, M, L, XL\n")
text = input("Enter your TEXT\n")
make_shirt(size, text)

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.

make_shirt()

# Make medium shirt with the default message
make_shirt("M",)
# Make a shirt of any size with a different message.
make_shirt("XS","different message")
# Bonus: Call the function make_shirt() using keyword arguments.
make_shirt(text="Developers Institute", size="XL")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Exercise 6 : Magicians …

# Using this list of magician’s names
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians(), which prints the name of each magician in the list.    
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.    

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)
        
print("Original List:")
show_magicians(magician_names)

def make_great(names):
    for i in range(len(names)):
        names[i] += " the Great"
                
make_great(magician_names)
print("\nModified List:")
show_magicians(magician_names)
        
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import random
def get_random_temp(season):    
    if season == 'winter':
        return random.randint(-10, 16)  
    elif season == 'spring' or season == 'fall' or season == 'autumn':
        return random.randint(17, 24)
    elif season == 'summer':
        return random.randint(25, 40)
    else:
        print("There is no such season")

def main():
    season = input("Please enter a season: ")
    var = get_random_temp(season)
    print(f"The temperature is {var} degrees Celsius")
    if var<0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif 0<=var<16:
        print(f"It is still cold outside")
    elif 16<=var<23:
        print(f"It is youe favorite weather today")
    elif 23<=var<32:
        print(f"It is pretty hot today")
    else:
        print(f"Be careful and drink a lot. It is very hot")
    
main()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.
# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.


import random

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def run_quiz(questions):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": question["answer"]
            })

    show_results(correct_answers, incorrect_answers, wrong_answers)


def show_results(correct_answers, incorrect_answers, wrong_answers):
    print("Quiz Results:")
    print("Correct answers:", correct_answers)
    print("Incorrect answers:", incorrect_answers)

    if incorrect_answers > 0:
        print("\nIncorrectly answered questions:")
        for wrong_answer in wrong_answers:
            print("Question:", wrong_answer["question"])
            print("Your answer:", wrong_answer["user_answer"])
            print("Correct answer:", wrong_answer["correct_answer"])
            print("")

    if incorrect_answers > 3:
        print("You had more than 3 wrong answers. Please play again.")
run_quiz(data)
