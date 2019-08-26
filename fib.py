end = input("Enter last number:- ")
a,b = 0,1
for i in range(end):
    a,b = b,a+b
    print a,b