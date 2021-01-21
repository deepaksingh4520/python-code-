n=int(input("enter a number"))
temp=n
reverse=0
while(n>0):
    d=n%10
    reverse=(reverse*10)+d
    n=n//10
    if(temp==reverse):
        print("given number is palindrome")
    
