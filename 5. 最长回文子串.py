

# 给你一个字符串 s，找到 s 中最长的 回文 子串。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start,end = 0,0
        for i in range(len(s)-1):
            j = 1
            while i-j >= 0 and i + j < len(s):
                if s[i-j] == s[i+j]:
                    j += 1
                else:
                    break
            if 2*(j-1)+1 > end - start:
                start = i - j + 1 
                end = i + j

            if s[i] == s[i+1]:
                j = 1
                while i-j >= 0 and i + j + 1 < len(s):
                    if s[i-j] == s[i+j+1]:
                        j += 1
                    else:
                        break
                if 2*(j-1)+2 > end - start:
                    start = i - j + 1
                    end = i + j + 1

        return s[start:end]
            

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))