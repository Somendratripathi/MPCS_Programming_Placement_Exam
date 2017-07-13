'''
The University of Chicago
Master Program of Computer Science (MPCS)
2015-2016
Programming Placement Exam Problem
Python2 Solution for
"A Winning Strategy?"

Problem Description: https://uchicago.kattis.com/problems/uchicagoplacement.martingale

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''


import sys

fhand = sys.stdin
lines = fhand.readlines()

# The money before the gamble
M = int(lines[0].strip())
# The bid for the first round 
B = int(lines[1].strip())
# The number of the gamble rounds
N = int(lines[2].strip())
# The outcomes of the gambles
# 1: heads (win); 0: tails (lose)
outcomes = list()
for outcome in lines[3].split(' '):
    outcomes.append(int(outcome))

# The money currently at hand
m = M
# The bid for the current round
b = B

# Start gamble
for i in xrange(N):
    if outcomes[i]:
        m = m + b
        b = min(B, m)
    else:
        m = m - b
        b = min(2*b, m)

    # Stop gamble if "BROKE"
    if m == 0:
        break

# Print the money or final state at hand after gamble
if m == 0:
    print("BROKE")
else:
    print(m)
