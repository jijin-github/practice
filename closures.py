def closure_fun(num):
    def multiply(number):
        return num * number
    return multiply

num_2 = closure_fun(2)
print(num_2(11))
print(num_2(24))

num_6 = closure_fun(6)
print(num_6(1))