m1=int(input("enter the marks of first subject"))
m2=int(input("enter the marks of the second subject"))
m3=int(input("enter the marks of the third subject"))
m4=int(input("enter the marks of the fourth subject"))
m5=int(input("enter the marks of the fifth subject"))
total=(m1+m2+m3+m4+m5);
percentage=(total)/5;
if(percentage>=60):
    print("result of the student is first devision ",firstdevision)
if(percentage>45 & percentage<59):
    print("result of the student is second division ",seconddivision)
if(percentage>33 & percentage<45):
    print("result of the student is third division",thirddivision)
elif(percentage<33):
    print("result of the student is fail",fail);
