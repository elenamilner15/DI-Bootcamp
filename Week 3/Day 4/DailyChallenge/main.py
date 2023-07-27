# Daily Challenge : Text Analysis
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
# import string
import re

class Text:
    def __init__(self, text):
        self.text = text
        
    def change_text(self):
        lowercase_text = self.text.lower()
        new_text = re.sub(r'[^\w\s]', '', lowercase_text)
        return new_text   

    def word_frequency(self):        
        my_list={}
      
        words_list = self.text.split()            
        for word in words_list:            
            count = words_list.count(word) 
            my_list[word] =count
        for word, count in my_list.items():
            print(f"The frequency of '{word}' is {count}")         
        return my_list                        
    
    def most_common_word(self, my_list):
        most_common_word = max(my_list, key=my_list.get)
        print(f"The most frequent word is '{most_common_word}' with a frequency of {my_list[most_common_word]}")
        
    def unique_words(self, my_list):
        unique_list=[]
        # for word in my_list:            
        #     count = my_list.count(word) 
        #     my_list[word] =count
        for word, count in my_list.items():
            if count==1:
                unique_list.append(word)
                
            else:
                pass
        
        print ("The unique words are: " + ", ".join(unique_list)) 
        return unique_list     
   
example_text = "A good, good, book book  cost as much as a good house."
new_text = Text(example_text).change_text()
my_list=Text(new_text).word_frequency()

Text(new_text).most_common_word(my_list) #'any_text' could be here.
#Function only uses my_list 
Text(new_text).unique_words(my_list)

