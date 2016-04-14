# def longest_sub(arr):
#     temp = [0] * (len(arr))
#     result = 0
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[i]>arr[j] and temp[i]<=temp[j]:
#                 temp[i] = temp[j] + 1
#     return 0
#Need to fix
#
# arr = [20,10,22,12,34,58,62,13]
# print longest_sub(arr)
