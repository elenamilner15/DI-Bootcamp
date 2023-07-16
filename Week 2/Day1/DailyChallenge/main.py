# 1. Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

string= input("enter a string 10 characters long\n")
if len(string)<10:
    print("string not long enough")
elif len(string)>10:
    print("string too long")
else:
    print("perfect string")
    

# 2. Then, print the first and last characters of the given text.

print("first character is: ",string[0],"\n" "last character is:", string[len(string)-1])


#3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

for n in range(0, len(string)):  
    print(string[:n+1])
    

# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:   
    

import random
list = list(string)
random.shuffle(list)
new_string=''.join(list)
print(new_string)
