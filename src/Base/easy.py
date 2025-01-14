#Covering the easy challenges of python
import math

def t01helloWorld (str):
    return "Hellow world: " + str

'''
 Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
def t02ifElse (number):
    if(number % 2 != 0):
        return "Weird - it's odd"
    else:
        if(number in range(2,6)):
            return "Not weird - in range 2-5"
        elif(number in range(6,21)):
            return "Weird in range of 6-20"
        elif( number > 20):
            return "Not weird  n > 20"

'''
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''       
def t03arithmeticOperators(inputA, inputB):
    a, b = int(inputA), int(inputB)
    if(a < 1 or a > 10000 or b < 1 or b > 10000):
        return "out of range" 
    return a+b, a-b, a*b

def t04division(inputA, inputB):
    a, b = int(inputA), int(inputB)
    if( a == 0 or b == 0):
        return "divied by 0"
    return a//b, a/b
