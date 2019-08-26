# def sockMerchant(n, ar):
#     count = 0
#     ar.sort()
#     i = 0
#     while i<n:
#         if n > i+1:
#             if ar[i]==ar[i+1]:
#                 count = count+1
#                 i+=2
#             else:
#                 i+=1
#         else:
#             i += 1
#     return count

def sockMerchant(n, ar):
    count = 0
    ar.sort()
    for i in range(0, n, 2):
        if n > i+1:
            if ar[i] == ar[i+1]:
                count += 1
    return count
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))