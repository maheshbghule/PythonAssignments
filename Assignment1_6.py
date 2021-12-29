'''
6.Write a program which accept number from user and check whether that number is positive or 
negative or zero. 
Input : 11    Output : Positive Number 
Input : -8    Output : Negative Number 
Input : 0    Output : Zero 
'''
def CheckNumber(x):
    if x>0:
        print("number is positive")
    elif x<0:
        print("number is negative")
    elif x==0:
        print("number is zero")
def main():
   x=(int(input("enter the number")))
   CheckNumber(x)
     
if __name__ =="__main__":
    main()  
