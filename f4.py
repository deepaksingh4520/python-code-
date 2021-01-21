def naturalnumber():
    sum=0
    n=int(input("enter the number"))
    for i in range(1,n):
        sum=sum+i
        print("sum of", n,"natural number is:",sum)

naturalnumber()        
