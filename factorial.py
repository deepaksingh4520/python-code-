n=int(input("enter a number"))
fact=1
i=1
for i in range(1,n+1):
    fact=fact*i
    i=i+1
    print("factorial of",n,"is",fact)
