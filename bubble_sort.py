items = [6,44,1,2,3,47]
for i in range(len(items)):
    for j in range(len(items)-i-1):
        if items[j+1] > items[j]:
            items[j], items[j+1] = items[j+1], items[j]

print(items)



I want you to create a method to increment a number. The number can be any number, but it will be given as an array of digits. The output also should be an array, which is the number incremented. I want to see array handling logic, so don’t do x*100 + y*10 - or converting to string (and then to number) etc

Def incr([2,3,4]) =>as good as incr(234) => 235 => [2,3,5]
Def incr([3,4,2,5]) =>as good as incr(3425) => Result: 3426 => [3,4,2,6]

Q3
----
Create
a
random
number
generator
which
also
has
an
exclude
list in it.How
would
you
implement
it? You
can
use
Math.random
internally.Also, it
should
be
done in a
minimal
time
duration
Every
time
the
method is called, it
returns
a
value, which is not in the
list
random_with_exclusion(0, 10, [3, 7]) = > 4
random_with_exclusion(0, 10, [3, 7]) = > 9
random_with_exclusion(0, 10, [3, 7]) = > 1
etc

Math.random(start, end) = > gives
a
value

Def
get_random_number(start, end, list_values):
Yield[i
for i in range(start, end) if i not in list_values]

# New_num = Math.random(start, end)

# If New_num  in list_values:
#	get_random_number(start, end, list_values)
# Else:
# Return New_num