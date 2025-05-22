# Leetecode
# 给你两个长度为 n 的整数数组 nums1 和 nums2 ，找出所有满足 i < j 且 nums1[i] + nums1[j] > nums2[i] + nums2[j] 的数对 (i, j) 。

# 返回满足条件数对的 个数 。
from typing import List
import bisect


# def bisect(arr:List,tgt):
#     if len(arr) == 1:
#         if arr[0] == tgt:
#             return 0
#         else:
#             return None
        
#     mid = len(arr)//2
#     if arr[mid] == tgt:
#         return mid
    
#     if tgt < arr[mid] :
#         return bisect(arr[:mid],tgt)
#     else:
#         result = bisect(arr[mid:],tgt)
#         if result is None:
#             return None
#         else:
#             return result + mid


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        diff = [nums1[i]-nums2[i] for i in range(len(nums1))]
        diff.sort()
        result = 0
        for i in range(len(diff)):
            
            result += len(nums1)-bisect.bisect_right(diff, -diff[i])
            if diff[i] > 0:
                result -= 1

        return result//2


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,10,6,2]
    nums2 = [1,4,1,5]
    # 1,-1,1,-1
    # -1,-1,1,1
    # 2+2
    print(solution.countPairs(nums1,nums2))

    # print(bisect([0,1,2,3,4,5,6,8],9))