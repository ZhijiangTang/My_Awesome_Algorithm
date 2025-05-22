


# 给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。

from typing import List
import bisect

# sum的计算复杂度比较高
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        reverse_nums = [1-i for i in nums]
        acc_reverse_nums = [0] + []
        for i in range(len(reverse_nums)):
            acc_reverse_nums.append(acc_reverse_nums[-1] + reverse_nums[i])
        # print(acc_reverse_nums)
        result = []
        for left in range(1,len(nums)+1):
            right = bisect.bisect_right(acc_reverse_nums[left:], acc_reverse_nums[left-1]+k) 
            # print(right
            result.append(right)
            
        return max(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
    print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))

    pass
 