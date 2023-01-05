import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    result = ''
    if(m==0):
        result += num2Words(h)
        result += ' o\' clock'
    elif(m==1):
        result += num2Words(m) + ' minute past '
        result += num2Words(h)
    elif(m==59):
        result += num2Words(m) + ' minute to '
        if(h+1>12): result += num2Words(1)
        else: result += num2Words(h+1)
    elif(m==15 or m==30):
        result += num2Words(m) + ' past '
        result += num2Words(h)
    elif(m==30):
        result += num2Words(m) + ' past '
        result += num2Words(h)
    elif(m==45):
        result += num2Words(m) + ' to '
        if(h+1>12): result += num2Words(1)
        else: result += num2Words(h+1)
    elif(m<30):
        result += num2Words(m) + ' minutes past '
        result += num2Words(h)
    elif(m<60):
        result += num2Words(60-m) + ' minutes to '
        if(h+1>12): result += num2Words(1)
        else: result += num2Words(h+1)

    print(result)
    return result
def num2Words(num):
    # 15 and 30 is not a numerical words, hour is less than 12
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'quarter', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'half'}
    return num2words[num].lower()

timeInWords(3,0)
timeInWords(5,47)
timeInWords(3,15)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     h = int(input().strip())

#     m = int(input().strip())

#     result = timeInWords(h, m)

#     fptr.write(result + '\n')

#     fptr.close()
