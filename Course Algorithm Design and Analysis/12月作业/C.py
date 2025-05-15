if __name__ == '__main__':
    n,p,m = list(map(int,input().split()))
    costs = []
    items = []
    for _ in range(p):
        cost, item = list(map(int,input().split()))
        costs.append(cost)
        items.append(item)

    M = max(items)*n
    if M < m:
        print('-1')
    else:
        dp = [[float('inf')]*(M+1) for i in range(n+1)]
        dp[0][0] = 0
        for i in range(p):
            dp[1][items[i]] = costs[i]

        for day in range(2,n+1):
            for m_i in range(1,M+1):
                dp_tmp = [dp[day-1][m_i-items[j]]+costs[j] for j in range(p) if m_i-items[j]>=0]+[dp[day][m_i],dp[day-1][m_i]]
                dp[day][m_i] = min(dp_tmp)
        # print(dp[])
        result = min(dp[n][m:])
        print(result if result!=float('inf') else -1 )

