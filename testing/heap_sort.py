import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))

    return sorted_arr


list = [1,8,9,45,7]
sorted_list = heap_sort(list)
print(sorted_list)
