list_elements = [1, 2, 1, 3, 4, 3]
total_count = 0
for i in list_elements:
    element_count = 0
    for j in list_elements:
        if i==j:
            element_count += 1
    if not element_count > 1:
        total_count += i

print total_count,"IIII"