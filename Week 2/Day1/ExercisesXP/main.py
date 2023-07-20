# Exercise 1 : Hello World
print("Hello world \n" * 5)

# Exercise 2 : Some Math
# (99^3)*8 (meaning 99 to the power of 3, times 8).
calc = (99 ** 3) * 8
print(calc)




# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3
#       False
# >>> 3 == 3
#       True
# >>> 3 == "3"
#       False
# >>> "3" > 3
#       Error
# >>> "Hello" == "hello"
#       False


# Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand="FUTJITSU"
print(f"I have a {computer_brand} computer")

# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name="Elena"
age=36
shoe_size=37
info = f"I am {name} and in {age} years my foot has grown to {shoe_size} size"
print(info)

# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a=15
b=10
if a>b:
    print("Hello World")
    

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input("enter a number\n"))
if number%2==0:
    print ("The number is even")
else:
    print ("The number is odd")



# Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name = "elena"
user_name = input("What’s Your Name ?\n")
if user_name.lower()==my_name:
    print("What a coincedence we have a same name!")
else:
    print(f"Nice to meet you, {user_name}")
    
# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height_inch = float(input("Write your height in inches\n"))
height_cm_rnd=round(height_inch*2.54)
height_cm_diff=round(145- height_inch*2.54)
if height_cm_rnd >=145:
    print("You are tall enough to ride a Roller Coster")
else:    
    print (f"Sorry, you need to grow {height_cm_diff} cm to ride")
    
    


