
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "[":
                stack.append(i)
            if s[i] == "]":
                start = stack.pop()
                j  = start - 1
                num = ""
                while s[j] in ["0","1","2","3","4","5","6","7","8","9"]:
                    num = s[j] + num
                    j -= 1
                num = int(num)
                sub_str = s[start + 1:i]
                tmp = s[:j+1] + num * sub_str
                s = tmp + s[i+1:]
                i = len(tmp)
                continue
                
            i += 1
        return s

if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
