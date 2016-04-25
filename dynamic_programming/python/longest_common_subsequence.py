def longest_common_sub(arr,arr2):
    result = 0
    # temp = [1] * (len(arr))
    # for i in range(1,len(arr)):
    #     for j in range(i):
    #         if arr[i]>arr[j] and temp[i]<=temp[j]:
    #             temp[i] = temp[j] + 1
    #             result = temp[i]
    return result

arr = ["a","b","f","e","k","i"]
arr2 = ["n","e","k","i","c","a","b"]
# result should be 3 due to e, k ,i`

print longest_sub(arr)
