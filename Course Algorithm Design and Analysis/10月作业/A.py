

if __name__ == '__main__':
    n = int(input())
    s = list(map(int,input().split(' ')))
    c = list(map(int,input().split(' ')))
    max_c = sum(c)+1

    c_i_j_k = [max_c]*n
    c_j_k = [max_c]*n
    
    for i in range(n-1,-1,-1):
        c_j_k_temp = []
        c_k_temp = []
        for k in range(i+1,n):
            if s[k]<=s[i]:
                continue
            c_j_k_temp.append(c_j_k[k])
            c_k_temp.append(c[k])
        if len(c_j_k_temp)==0:
            continue
        c_j_k[i] = c[i]+min(c_k_temp)
        c_i_j_k[i] = c[i]+min(c_j_k_temp)
    
    ans = min(c_i_j_k)
    if ans == max_c:
        print(-1)
    else:
        print(ans)