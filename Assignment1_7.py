''' Write a program which contains one function that accept one number from user and returns 
true if number is divisible by 5 otherwise return false. 
Input : 8    Output : False 
Input : 25    Output : True '''

def Divisible(x):
    if(x%5==0):
        print("number is divisiable by 5")
    else:
        print("number is not Divisiable by 5")
   
def main():
   x=(int(input("enter the number")))
   Divisible(x)
     
if __name__ =="__main__":
    main()  
