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

# Part II
# Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
# Now, use the provided the_stranger.txt file and try using the class you created above.


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
        for word, count in my_list.items():
            if count==1:
                unique_list.append(word)
                
            else:
                pass
        
        print ("The unique words are: " + ", ".join(unique_list)) 
        return unique_list  
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)   
    
class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
        self.stop_words = set(['a', 'an', 'the', 'in', 'on', 'of', 'and', 'to', 'for', 'with', 'is', 'it', 'as', 'at'])

    def remove_stop_words(self):
        words_list = self.text.split()
        filtered_text = ' '.join(word for word in words_list if word.lower() not in self.stop_words)
        return filtered_text
    
#!!!!!!!!!   PART1      !!!!!!!!!!!!!!!!!   
example_text = "A good, good, book book  cost as much as a good house."
new_text = Text(example_text).change_text()
my_list=Text(new_text).word_frequency()

Text(new_text).most_common_word(my_list) #'any_text' could be here.
#Function only uses my_list 
Text(new_text).unique_words(my_list)

#!!!!!!!!!   PART2      !!!!!!!!!!!!!!!!!   
strange_path = r"C:\Users\elena\Desktop\6TTA\DI-Bootcamp\Week 3\Day 4\DailyChallenge\the_stranger.txt"

stranger_text = Text.from_file(strange_path)
new_text = stranger_text.change_text()
my_list=Text(new_text).word_frequency()
Text(new_text).unique_words(my_list)
Text(new_text).most_common_word(my_list) #'any_text' could be here.

#!!!!!!!!!   BONUS ()   !!!!!!!!!!!!!!!!! 

# method text without (!!!!!!!!) PUNCTUATION and SPECIAL CHARACTERS (!!!!!!!!) was applied in partI as def change_text(self). Before Bonus task was read


the_stranger_mod = TextModification.from_file(strange_path)
filtered_text = the_stranger_mod.remove_stop_words()
print("Text without stop words:")
print(filtered_text)
