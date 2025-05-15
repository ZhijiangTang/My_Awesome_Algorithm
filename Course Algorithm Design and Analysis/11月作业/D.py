
# class find_stop():


if __name__ == '__main__':
    T = int(input())
    result = []
    for t in range(T):
        N = int(input())
        fuel_stop = [list(map(int,input().split())) for i in range(N)]
        fuel_stop = sorted(fuel_stop, key=lambda x: x[0],reverse=True)
        L,P = list(map(int,input().split()))

        def cal_Available_fuel_stop(flag_i, end):
            Available_fuel_stop = []
            flag_j = flag_i
            for flag in range(flag_i,N):
                if fuel_stop[flag][0]<end:
                    flag_j = flag
                    break
                Available_fuel_stop.append(fuel_stop[flag][1])
            return flag_j,Available_fuel_stop
        
        end = L-P
        flag_i, Available_fuel_stop = cal_Available_fuel_stop(0,end)
        res = 0

        while((end>0) and (len(Available_fuel_stop)>0)):
            Available_fuel_stop.sort(reverse=True)
            end = end-Available_fuel_stop.pop(0)
            flag_i, interval_fuel_stop = cal_Available_fuel_stop(flag_i,end)
            Available_fuel_stop += interval_fuel_stop
            res += 1

        if end>0:
            result.append(-1)
            # print('-1')
        else:
            result.append(res)
            # print(res)
    print('\n'.join(list(map(str,result))))
