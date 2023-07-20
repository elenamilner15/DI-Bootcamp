# Challenge 1 : Sorting
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
words_list =[]
words_input=input("Input a comma separated sequence of words: ")
words_list=[word.strip() for word in words_input.split(',')]
   
ordered_words = sorted(words_list)
ordered_sequence = ", ".join(ordered_words)
print("Ordered sequence of words:", ordered_sequence)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Challenge 2 : Longest Word
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).


words_list =[]
all_lengths = []
sent=input("Input a sentence: ")
words_list=[word.strip() for word in sent.split(' ')]
for word in words_list:
    word_lenghts = [len(word), word]
    all_lengths.append(word_lenghts)     
max_lenght_word=max(all_lengths, key=lambda x: x[0])[1]
print(max_lenght_word)

       
