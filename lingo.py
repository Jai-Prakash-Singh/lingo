#!/usr/bin/env python 

'''

In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the following wa>>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]

'''


def lingo(s1,s2):
    s3 = s2[ : ]
    lst = []
    for ch in s1:
        if ch in s3:
	    lst.append(ch)
	    s3.remove(ch)
    return lst


if __name__ == "__main__":

    s1 = str(raw_input("enter the first string of length 5: "))
    #s2 = str(raw_input("enter the second string of length 5: "))
    s2 = "snake"

    s1 = list(s1)
    s2 = list(s2)
    lst = lingo(s1, s2)
    #print s1, s2
    for ch in lst:
        if s1.index(ch) == s2.index(ch):
    	    s2[s2.index(ch)] = "["+ch+"]"
    	else:
    	    s2[s2.index(ch)] = "("+ch+")"
    print "".join(s2)


