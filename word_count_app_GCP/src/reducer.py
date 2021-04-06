#!/usr/bin/env python

from operator import itemgetter
from string import punctuation
import sys

num = sys.argv[1]           # Number for the TOP N words
current_word = None
current_count = 0
word = None
word_dic1={}             # Dictionary for storing the words

for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t',1)

    # covert count to int
    try:
        count = int(count)
    except ValueError:
        # count was a number
        continue
     
    #this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            word_dic1[word] = count                 # if not shown before, add the word to the dictionary
        current_count = count
        current_word = word

sorted_dic1 = sorted(word_dic1.items(), key=lambda x: x[1], reverse=True)                 # Sort the dictionary based on the value

# Out put top N words in std output
for key,value in sorted_dic1[:int(num)]:
    # Write result to STDOUT     
    print ('%s\t%s' % (key, value))
