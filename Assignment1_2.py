''' Write a program which contains one function named as ChkNum() which accept one
 parameter as number. If number is even then it should display “Even number” otherwise
 display “Odd number” on console...'''

def ChkNum(value):
    if(value%2==0):
        print("number is even")
    else:
        print("number is odd")
    

def main():
    value= int(input("enter the number"))
    ChkNum(value) 

if __name__ =="__main__":
    main()  