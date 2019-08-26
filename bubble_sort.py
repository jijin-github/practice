items = [6,44,1,2,3,47]
for i in range(len(items)):
    for j in range(len(items)-i-1):
        if items[j+1] > items[j]:
            items[j], items[j+1] = items[j+1], items[j]

print(items)