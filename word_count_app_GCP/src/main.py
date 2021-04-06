import subprocess
import re
import sys
from string import punctuation
from normal_module import SmallDatafile


def prompt1():
    """ Promt user to select the algorithm"""
    while True:
        try:
            value = int(input("Do you want to use small dataset algorithm or large dataset algorithm? (1/0): "))
            if value == 1 or value == 0:
                break
            else:
                print("Invalid value. Please try again")
        except ValueError:
        # use the value 1 or 0 as input
            print("Please type 1 or 0")
    return value

def prompt2():
    """ Promt user to type the number they want to use """
    while True:
        try:
            num = int(input("Please tell us the number of most frequent words you want to view: "))
            break
        except ValueError:
            # num is a number
            print("Invalid value. Try again")
    return num

def prompt3():
    """Prompt users for the diretory where the data is stored"""
    path = input("Please type the path to your data directory: ")
    return path

def main():
    """ In the main(), we promt users for 3 inputs. First, the algorithm. Second, the N for the number of words. Third, the path to where the data is stored
        For simple algorithm, we will implement the sorting class listed above. For lager data algorithm, we will use hadoop mapreduce
    """
    value = prompt1() #Read the value
    num = prompt2()   #Read the number of top words
    path = prompt3()  #Read the path


    # Implement the small algorithm 
    if value == 1:
        r1 = SmallDatafile(path, num)
        r1.read_word()
        r1.print_word()

    # Implement the large data algorithm. Using shell script to run on GCP cluster(Linux)
    else:
        print("The top", num, "words in the file(s) are: ")
        # shell script strings
        comd1 = "hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar " 
        comd2 = "-Dmapred.reduce.tasks=1 "
        comd3 = "-file mapper.py -mapper 'python mapper.py " + str(num) + "' "
        comd4 = "-file reducer.py -reducer 'python reducer.py "+ str(num) + "' "
        comd5 = "-input /data/* -output /Outputfolder"+str(num)

        comd_sum = comd1 + comd2 + comd3 + comd4 + comd5
        comd_merge = "hadoop fs -getmerge /Outputfolder"+str(num) + " collectedResults"
        comd_cat = "cat collectedResults"

        # print the results based on the map reduce
        subprocess.getoutput(comd_sum)
        subprocess.getoutput(comd_merge)
        print(subprocess.getoutput(comd_cat))

    # Prompt users to use main() again
    view_again = input("Would you like to read another file? (yes/no) ")
    if view_again == "yes":
        main()

if __name__ == "__main__":
    main()