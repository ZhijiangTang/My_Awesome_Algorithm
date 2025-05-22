

# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。


from typing import List


def rec(arr):
    if len(arr) == 0:
        return -float("inf")
    neg_i = [i for i in range(len(arr)) if arr[i] < 0]
    # print(neg_i)
    zero_i = [i for i in range(len(arr)) if arr[i] == 0]

    ans = []
    if len(neg_i) % 2 == 0 and len(zero_i) == 0:
        ans = arr[0]
        for i in range(1,len(arr)):
            ans *= arr[i]
        return ans
    elif len(zero_i) > 0:
        zero_i = [-1] + zero_i + [len(arr)]
        for i in range(len(zero_i)-1):
            ans.append(rec(arr[zero_i[i]+1:zero_i[i+1]]))
    else :
        for i in range(len(neg_i)):
            ans.append(rec(arr[neg_i[i]+1:]))
            ans.append(rec(arr[:neg_i[i]]))
    return max(ans)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        return max(max(nums),rec(nums))


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2,3,-2,4]))
    print(solution.maxProduct([-2,0,-1]))
    print(solution.maxProduct([-2,-3,-1]))
    pass