
from typing import List

def merge_sort(arr:List):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr = sorted_arr + left[i:]
    sorted_arr = sorted_arr + right[j:]

    return sorted_arr

if __name__ == "__main__":
    print(merge_sort([9,1,2,5,8,7,6,3,2,0]))
    print("end")