# 🌟 Exercise 1 – Random Sentence Generator

# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.


# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.



filepath = r"C:\Users\elena\Desktop\6TTA\DI-Bootcamp\Week 3\Day 4\sowpods.txt"


def get_words_from_file(filepath):
    
    with open(filepath, "r") as my_file:
        words = my_file.read().splitlines()  # read the file
        return(words)

words = get_words_from_file(filepath)


import random
import string

def random_string (length): 
    sentence =' '.join(random.choices(words, k=length)).lower()
    print(sentence)      
    return sentence 
    
    
def main():
    print("Function is generating sentence from random words")    
    while True:
        try:
            length = int(input("How long the sentence should be (between 2 and 20)? "))
            if 2 <= length <= 20:
                sentence =' '.join(random.choices(words, k=length)).lower()
                print(sentence)
                return sentence
            else:
                print("Error: Sentence length should be between 2 and 20.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")


random_string = random_string(5)
main()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.


import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "12.12.2002"

updatedJson = json.dumps(data, indent=2)

with open("updated_data.json", "w") as file:
    file.write(updatedJson)

print("saved to 'updated_data.json'")

            
            


