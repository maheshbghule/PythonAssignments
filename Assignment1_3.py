'''Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16'''

def Add(value1,value2):
    sum = value1+value2
    return sum

def main():

    x= int(input("enter first number"))
    y= int(input("enter second number"))
    print("addition is :",Add(x,y))
if __name__ =="__main__":
    main()  