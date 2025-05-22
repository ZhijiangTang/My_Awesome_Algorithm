# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2] + [0]*(n-2)
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]