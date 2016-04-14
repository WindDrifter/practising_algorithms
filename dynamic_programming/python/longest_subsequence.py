def longest_sub(arr):
    temp = [1] * (len(arr))
    result = 0
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j] and temp[i]<=temp[j]:
                temp[i] = temp[j] + 1
                result = temp[i]
    return result

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print longest_sub(arr)
