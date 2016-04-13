# def quick_sort(array):
#     pivot = array[len(array)/2]
#
#
#     if len(array) <= 1:
#         return array
#     smaller = [x for x in array[1:] if x < pivot]
#     larger = [x for x in array[1:] if x > pivot]
#     return quick_sort(smaller) + array[0] + quick_sort(larger)
#
# def partitaion(array):
