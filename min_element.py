element_list = [3,4,5,1,6,68,7]
min_element = element_list[0]
for i in element_list:
    if min_element > i:
        min_element = i

print min_element,"Min element"