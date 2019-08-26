inputList = [23, 65, 19, 90]
last_pos = len(inputList) - 1
new_list = []
for i in range(len(inputList)):
    inputList[i], inputList[last_pos] = inputList[last_pos], inputList[i]
    last_pos -= 1
    if last_pos == 0:
        break
print inputList
