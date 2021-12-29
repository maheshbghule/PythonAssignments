'''
10.1) Write a program which accept name from user and display length of its name. 
Input : Marvellous    Output : 10 
'''
def CheckLength():
    x=(input("Enter string"))
    print("total length of string",len(x))

def main(): 
    CheckLength()

if __name__ =="__main__":
     main()  
#in above program are same output ...both :
# 10.2) Write a program which accept name from user and display length of its name. 
# Input : Marvellous    Output : 10 

'''
def String_Length(x):
          j=0
          for i in x:
                    j=j+1
          print("Length of stirng=",+j)

x=input("Enter  string ")
String_Length(x)
'''      

