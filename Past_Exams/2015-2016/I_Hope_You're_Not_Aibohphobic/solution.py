'''
The University of Chicago
Master Program of Computer Science (MPCS)
2015-2016
Programming Placement Exam Problem
Python2 Solution for
"I Hope You're Not Aibohphobic"

Problem Description: https://uchicago.kattis.com/problems/uchicagoplacement.palindrome

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''

import sys

fhand = sys.stdin
line = fhand.readlines()
word = line[0].strip()

def palindrome_check(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        if word[0] == word[-1]:
            return True
        else:
            return False
    else:
        if word[0] == word[-1]:
            return palindrome_check(word = word[1:-1])
        else:
            return False

# Check palindrome using a recursive algorithm
if palindrome_check(word = word):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
