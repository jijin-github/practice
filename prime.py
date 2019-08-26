term = input("Enter terms:-")
for i in range(term):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                # print str(i)+" is not prime number"
                break
        else:
            print str(i)+"is prime number"