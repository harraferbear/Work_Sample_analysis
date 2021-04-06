#!/usr/bin/env python
import re
import sys
from string import punctuation

class SmallDatafile():
    """ This class reads small dataset and counts the words using small dataset algorithm.
        The path and file name are given by the users.

        Instances have several attributes:

        pathname: path to the file given by useds
        num: number of top words users want to show
        wordslist and sorted_word are dictionary and list to store the words
    """

    def __init__(self, path, num):
        """Initialize every variable used in small algorithm"""

        self.pathname = path           # Path + file name
        self.num = num                 # Number of top words users want to show
        self.wordslist = {}            # Dictionary to count the words
        self.sorted_word = []          # List to store the sorted words
         # Words that are gonna be filter out 
        self.stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
"he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
 "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", 
 "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
 "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", 
 "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
 "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
  "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    
    # Read words from each line or the file. Filter the words. And save it in dictionary
    def read_word(self):
        for line in open(self.pathname):
            for word in line.split():
                self.chosenword = word.strip(punctuation).lower()        # Remove the punctuations and make every words lower letters
                if self.chosenword not in self.stopwords:
                    self.wordslist[self.chosenword] = self.wordslist.get(self.chosenword, 0) + 1           # If the word already exists then value +1. If not, add the key and value
         # Sort the dictionary and return the list
        self.sorted_word = sorted(self.wordslist.items(), key=lambda x: x[1], reverse=True)

    # Print the top words in std output
    def print_word(self):
        print("The top", self.num, "words in this file are: ")
        for i in range(self.num):
            print('%s\t%s' % (self.sorted_word[i][0], self.sorted_word[i][1]))