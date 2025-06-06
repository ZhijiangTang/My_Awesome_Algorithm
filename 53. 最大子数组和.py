# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组是数组中的一个连续部分。

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums = nums + [0]
        result = sum(nums)
        all = sum(nums)
        acc_reverse_max = [nums[-1]] * len(nums)
        tmp = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            tmp += nums[i]
            if tmp < acc_reverse_max[i+1]:
                acc_reverse_max[i] = tmp
            else:
                acc_reverse_max[i] = acc_reverse_max[i+1]
        
        acc = 0
        # print(acc_reverse_max)
        for i in range(len(nums)-1):
            tmp = all - acc - acc_reverse_max[i+1]
            if tmp > result:
                result = tmp
            # for j in range(i,len(nums)):
            #     tmp += nums[j]
            acc += nums[i]
        
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([-2 ,1]))
    print(s.maxSubArray([8,-19,5,-4,20]))