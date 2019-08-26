input_value = input("Enter String:- ")
reversed_val = input_value[::-1]
print("reversed value is:- "+reversed_val)
for i in range(len(input_value)//2):
    if input_value[i] != input_value[len(input_value)-i-1]:
        print("Not palindrome")
        break
else:        
    print("String is palindrome")     