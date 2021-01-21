n=int(input("enter a number"))
count=0
sum=0
while(n>0):
    count=count+1
    d=n%10
    sum=sum+d
    n=n//10
print("sum of number of digit of entered number is",sum)
print("the number of digit in the number are",count)    
