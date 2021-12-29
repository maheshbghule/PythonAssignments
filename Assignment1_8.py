''' Write a program which accept number from user and print that number of “*” on screen. 
Input : 5    Output : * * * * *'''
def PrintPattern(x):
    for i in range(x):
        print("*",end=" ")
       
def main():
   x=(int(input("enter the number")))
   PrintPattern(x)

if __name__ =="__main__":
    main()  
    