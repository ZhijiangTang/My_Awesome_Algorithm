MOD = 10**9 + 7

def min_steps_to_target(n, s):
    # 目标状态为 t = 111...1，即所有环在剑上
    target = (1 << (n + 1)) - 1
    dp = {0: 0}  # 初始状态，步数为0

    # 遍历所有可能的状态
    for t in range(1 << (n + 1)):
        if t not in dp:
            continue
        # 尝试改变每个环的状态
        for i in range(n + 1):
            if can_change(t, i, s):
                # 计算新的状态 t' 通过异或改变第 i 位的状态
                new_t = t ^ (1 << i)
                dp[new_t] = min(dp.get(new_t, float('inf')), dp[t] + 1)

    # 返回从 000...0 到 111...1 的最小步数
    return dp.get(target, -1) % MOD

def can_change(t, i, s):
    # 检查当前状态 t 中的第 i 位是否可以合法改变
    # 将 t 转为二进制字符串并检查前缀是否满足 s 的后缀
    t_str = bin(t)[2:].zfill(len(s) + 1)  # 补齐长度
    prefix = t_str[:i]
    return s.endswith(prefix)

# 示例输入
n = int(input())
s = input()
print(min_steps_to_target(n, s))
