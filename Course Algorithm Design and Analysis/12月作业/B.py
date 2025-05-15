if __name__ == '__main__':
    N = int(input())  # number of variables
    c = list(map(int, input().split()))  # coefficients
    V = int(input())  # target sum V

    dp = [float('inf')]*(V+1)
    dp[0] = 0
    for i in range(1,V+1):
        dp_j = [dp[i-c_j] for c_j in c if  i-c_j>=0] + [dp[i]]
        dp[i] = min(dp_j)+1
    
    print(dp[V] if dp[V]!=float('inf') else -1 )

