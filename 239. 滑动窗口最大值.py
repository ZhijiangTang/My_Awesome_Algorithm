# Leetecode
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 。

from typing import List
import heapq

# 学会使用python的优先队列：heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i],i) for i in range(k)]
        heapq.heapify(q)
        window_max = [-q[0][0]]

        for i in range(k,len(nums)):
            heapq.heappush(q,(-nums[i],i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            window_max.append(-q[0][0])
            
        return window_max



if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))