# Daily Challenge: Solve The Matrix

import re
matrix = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''
    
# Split the matrix into rows
num_rows = 0
num_cols = 0
row_lengths = []
rows = matrix.split("\n")
for row in rows:
    num_rows +=1
    len_row = len(row)
    row_lengths.append(len_row)    
num_cols = max(row_lengths)   
word=""
sent="" #Short for sentence

for i in range(num_cols):
    word = ''.join(item[i] for item in rows)
    sent +=word
# print(sent)

new_sent = re.sub(r'[^a-zA-Z]', ' ', sent)
new_sent = re.sub(r'\s+', ' ', new_sent.strip())

print(new_sent)




