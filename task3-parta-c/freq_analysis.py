#!/bin/env python3

from collections import Counter
import re

TOP_K  = 20
NGRAM_MAX = 3

# Generate all the n-grams for value n:
# This function iterates through the entire text, 
# and each time it is called, it returns a gram 
# (or sequence of characters) of the 
# specified length n. 

#HINT: use if not re.search(r'\s', gram) to ignore
#      white space characters in your grams

def ngrams(n, text):
    for i in range(len(text)-n+1):
        gram = text[i:i+n]
        if not re.search(r'\s', gram):
            yield gram

# Read the data from the ciphertext
with open('ciphertext1.txt') as f:
    text = f.read()

# Count, sort, and print out the n-grams
for N in range(NGRAM_MAX):
   print("-------------------------------------")
   print("{}-gram (top {}):".format(N+1, TOP_K))

   # Call the counter method to count all ngrams of length N
   counts = Counter(ngrams(N+1, text))       
   #TODO: Sort gram counts from most common to least common
   #HINT: See if you can use methods of Counter to sort gram counts..
   # sorted_counts =..FILL CODE HERE. You can use the TOP_K global 
   #                variable as input to your method. 
   sorted_counts = counts.most_common(TOP_K)
   for gram, count in sorted_counts:                  
       print("{}: {}".format(gram, count))   # Print
