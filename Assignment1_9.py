'''
9. Write a program which display first 10 even numbers on screen. 
Output :  2 4 6 8 10 12 14 16 18 20
'''
def CheckEven(x):
    i=j=1
    while j<=x:
            if i%2==0:
                print(i,end=" ")
                j=j+1
            i=i+1


def main():
   
   x=(int(input("enter the number")))
   CheckEven(x)
  
if __name__ =="__main__":
    main()  
    