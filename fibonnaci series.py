n1,n2=0,1
n=int(input("enter the number"))
count=0
print("fibonacci sequence")
while count < n:
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    count += 1

