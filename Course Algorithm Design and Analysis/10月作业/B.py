

if __name__ == '__main__':
    N,M = list(map(int,input().split(' ')[:2]))
    M_i = [int(input()) for i in range(N)]
    
    opt = [M_i[0]+M]
    for i in range(1,N):
        minu_list = [sum(M_i[:(i+1)])+M]
        for j in range(i):
            minu_list.append(opt[j]+sum(M_i[:(i-j)])+M*2)
        opt.append(min(minu_list))
    
    print(opt[N-1])
