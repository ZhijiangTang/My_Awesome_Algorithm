
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

from typing import List

def quick_sort(nums: List[int]):
    if len(nums) <= 1:
        return nums
    povit = nums[0]
    left = [i for i in nums[1:] if str(i)+str(povit) >= str(povit)+str(i)]
    right  = [i for i in nums[1:] if str(i)+str(povit) < str(povit)+str(i)]
    return quick_sort(left) + [povit] + quick_sort(right)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = quick_sort(nums)
        nums = list(map(str, nums))
        for i in range(len(nums)):
            if nums[i] != "0" or i == len(nums)-1:
                return "".join(nums[i:])
        
        return "0"

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([0,0]))
    print(s.largestNumber([3,30,34,5,9]))