# Iterative Implementation
def search_number(arr, x):
    arr.sort()
    checking_pos = 0
    last_pos = len(arr)-1

    while checking_pos <= last_pos:
        mid = checking_pos + (last_pos - checking_pos) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            checking_pos = mid + 1
        else:
            last_pos = mid - 1
    return -1


arr = [2, 3, 4, 10, 40, 50]

result = search_number(arr, 10)
print result
