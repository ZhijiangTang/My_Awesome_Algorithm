

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        arrow = [input(),input()]
        opt = [1,1]+[0]*(n-2)
        for i in range(2,n):
            if arrow[i%2][i-1]=='>':
                if opt[i-1] | opt[i-2]:
                    opt[i] = 1
        
        if opt[n-1]==1:
            print('YES')
        else:
            print('NO')
