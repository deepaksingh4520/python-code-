 n=int(input("enter the for finding the reverse"))
reverse=0
while n>0:
    d=n%10
    reverse=(reverse*10)+d
    n=n//10
print("reverse of entered number is",reverse) 
