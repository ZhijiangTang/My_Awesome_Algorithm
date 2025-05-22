from typing import List


def quick_sort(arr:List):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [arr[i] for i in range(len(arr)) if arr[i] < pivot]
    right = [arr[i] for i in range(len(arr)) if arr[i] > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right) 

if __name__ == "__main__":
    print(quick_sort([9,1,2,5,8,7,6,3,2,0]))
    print("end")