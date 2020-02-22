import random
# Purpose: (What does the function do?) returns a list of the first word in every sentence in that file
# Input Parameter(s): (Each parameter by name and what it represents)fname,file
# Return Value(s): (What gets returned? Possibilities?)returns a list of the first word in every sentence in that file

def first_words(fname):
    ls = []
    try:
        with open(fname,'r') as fo:
            for word in fo:
                words = word.split()
                ls.append(words[0])
        return ls
    except:
        return -1

# Purpose: (What does the function do?)returns a dictionary where the keys are each distinct word in the file (case matters), and the value for any given key is a list of every word that follows that key anywhere in the file, in order, including duplicates. 
# Input Parameter(s): (Each parameter by name and what it represents)fname, file
# Return Value(s): (What gets returned? Possibilities?) returns a dictionary where the keys are each distinct word in the file (case matters), and the value for any given key is a list of every word that follows that key anywhere in the file, 

def next_words(fname):
    dic ={}
    with open(fname,'r') as f:
        for value in f:
            values = value.split()
            for i in range(len(values)-1):
                if values[i] in dic:
                    dic[values[i]].append(values[i+1])
                else:
                    dic[values[i]] = [values[i+1]]
        return dic

## Purpose: (What does the function do?)prints 10 ‘sentences’, one per line
## Input Parameter(s): (Each parameter by name and what it represents)fname, file
## Return Value(s): (What gets returned? Possibilities?)None.

def fanfic(fname):
    with open(fname,'r') as file:
        nex = next_words(fname)
        first = first_words(fname)
        for i in range (10):
            sentence = " "
            word = random.choice(first)
            sentence = sentence + word +" "
            while word != ".":
                word = random.choice(nex[word])
                sentence = sentence+word+" "
            print(sentence)
        



## Purpose: (What does the function do?)returns the total memory in bytes (an integer) being used by ​txt​ files in the directory
## Input Parameter(s): (Each parameter by name and what it represents)directory, dictionary.
## Return Value(s): (What gets returned? Possibilities?)returns the total memory in bytes (an integer) being used by ​txt​ files in the directory



def total_txt_size(directory):
    if type(directory) == int:
        return directory
    elif type(directory) == dict:
        sum_num = 0
        for k, v in directory.items():
            if type(v) == int and '.txt' not in k:
                continue
            sum_num += total_txt_size(v)
        return sum_num

       









