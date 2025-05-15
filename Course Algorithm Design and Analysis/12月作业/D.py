if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    volunteers_required = list(map(int,input().split()))
    s = []
    t = []
    c = []
    for i in range(m):
        s_i,t_i,c_i = list(map(int,input().split()))
        s.append(s_i)
        t.append(t_i)
        c.append(c_i)
    