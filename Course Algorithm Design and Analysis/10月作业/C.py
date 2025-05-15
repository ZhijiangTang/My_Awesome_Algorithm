

if __name__ == '__main__':
    m,n = list(map(int,input().split()))
    food = [list(map(int,input().split())) for i in range(m)]

    if m==1 or n==1:
        print(0)
    else:
        opt = [[[0 for i in range(m)] for j in range(n)] for k in range(m)]
        opt[1][0][0] = food[0][1]+food[1][0]
        opt[0][1][1] = food[0][1]+food[1][0]

        for step in range(2,m+n-2):
            x_1 = min(step,m-1)
            y_1 = step - x_1
            while((x_1>=0) & (y_1<n)):
                for x_2 in range(min(step+1, m)):
                    if (x_1 == x_2) or (step-x_2>=n):
                        continue
                    opt_tmp = []
                    if x_1-1>=0:
                        opt_tmp.append(opt[x_1-1][y_1][x_2])
                        if x_2-1>=0:
                            opt_tmp.append(opt[x_1-1][y_1][x_2-1])
                    if y_1-1>=0:
                        opt_tmp.append(opt[x_1][y_1-1][x_2])
                        if x_2-1>=0:
                            opt_tmp.append(opt[x_1][y_1-1][x_2-1])
                    if 0 <= x_1 < m and 0 <= y_1 < n:
                        opt[x_1][y_1][x_2] = max(opt_tmp)+food[x_1][y_1]+food[x_2][x_1+y_1-x_2]

                x_1 -= 1
                y_1 += 1
        
        print(max(opt[m-2][n-1][m-1],opt[m-1][n-2][m-2]))

