
# Def incr([2,3,4]) =>as good as incr(234) => 235 => [2,3,5]
# Def incr([3,4,2,5]) =>as good as incr(3425) => Result: 3426 => [3,4,2,6]

# Python3 program to convert a list
# of integers into a single integer
def convert(list):
    # multiply each integer element with its
    # corresponding power and perform summation
    res = sum(d * 10 ** i for i, d in enumerate(list[::-1]))+1

    return (res)


# Driver code
list = [1, 2, 3]
print(convert(list))



# Create a random number generator which also has an exclude list in it. How would you implement it? You can use Math.random internally. Also, it should be done in a minimal time duration
# Every time the method is called, it returns a value, which is not in the list
# random_with_exclusion (0, 10, [3,7]) => 4
# random_with_exclusion (0, 10, [3,7]) => 9
# random_with_exclusion (0, 10, [3,7]) => 1 etc
#
# Math.random(start, end) => gives a value

#
# Def get_random_number(start, end, list_values):
# 	New_list =  [i for i in range(start, end) if i not in list_values]
# 	random_Index = Math.random(0, len(New_list))
# 	Return New_list[random_Index ]