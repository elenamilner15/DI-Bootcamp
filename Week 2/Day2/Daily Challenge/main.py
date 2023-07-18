# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

sequence=[]
n = 1
element=0

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

while n<=length:
  element = number*n
  n+=1
  sequence.append(element)  

print(sequence)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
inp = input("Input a string\n")
new = inp[0]
for i in range(1, len(inp)):
    if inp[i] != inp[i-1]:        
        new += inp[i]

print("New string :")
print(new)
