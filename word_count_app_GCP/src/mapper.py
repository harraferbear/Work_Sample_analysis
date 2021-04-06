#!/usr/bin/env python
import sys
from string import punctuation
import re

num = sys.argv[1]       # number of the Top N words
# Set plain words that are not used
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
"he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
 "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", 
 "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
 "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", 
 "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
 "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
  "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
word_dic = {} # dictionary to store the words

for line in sys.stdin:
    # remove the leading and trailing whitespace
    line = line.strip()
    #split the line into words. Remove punctuation and using lower letters.
    words = re.sub(r'[^\w\s]','',line.lower()).split()
    #increase counters
    for word in words:
        # Here we filter out the words that are not too meaningful by themseleves
        if word not in stopwords:
            word_dic[word] = word_dic.get(word, 0) + 1           #adding value to new key to the dictionary

sorted_dic = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)           # Sort the dictionary based on the value

#Print the top n words in std output
for key,value in sorted_dic[:int(num)]:    
    print ('%s\t%s' % (key, value))