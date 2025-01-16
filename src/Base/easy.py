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

def t05loops(input):
    n = int(input)
    if(n <= 1 or n >= 20):
        return "out of range"
    list = [] 
    for i in range(0,n):
        list.append(i**2)
    return list

def t06function(year):
    if year <= 1900 or year >= 10**5:
        return False
    if year%400 == 0:
        return True
    if year%4 == 0 and year%100 != 0:
        return True
    return False

def t07printFunction(input):
    n = int(input)
    if(n <= 1 or n >= 150):
        return "out of range"
    list = []
    for i in range(1, n+1):
        #print(i, end='')
        list.append(i)
    return list
