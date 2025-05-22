

# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

from typing import List



class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1]
        def dfs():
            flag = result[-1]
            if result[-1]*10 <= n:
                result.append(result[-1]*10)
                dfs()
            if flag % 10 < 9 and (flag + 1) <= n:
                result.append(flag + 1)
                dfs()
        dfs()
        return result








if __name__ == "__main__":
    solution = Solution()
    print(solution.lexicalOrder(102))
    pass
