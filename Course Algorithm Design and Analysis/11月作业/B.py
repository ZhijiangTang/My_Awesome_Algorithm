

if __name__ == '__main__':
    N = int(input())
    cows_lists_len = input().split()[0]
    cows = [cows_lists_len[0], cows_lists_len[-1]]
    cows_lists_len = [len(l) for l in cows_lists_len.replace('0',' ').split()]
    
    if len(cows_lists_len)==0:
        print(0)
    else:
        if (cows[0] == '1') & (cows[-1] == '1'):
            max_day_spread = min([(cows_lists_len[0]-1)*2+1] + cows_lists_len[1:-1] + [(cows_lists_len[-1]-1)*2+1])
        elif cows[0] == '1':
            max_day_spread = min([(cows_lists_len[0]-1)*2+1] + cows_lists_len[1:])
        elif cows[-1] == '1':
            max_day_spread = min([(cows_lists_len[-1]-1)*2+1] + cows_lists_len[:-1])
        else:
            max_day_spread = min(cows_lists_len)

        max_day_spread = (max_day_spread-1)/2
        res = 0
        for l in cows_lists_len:
            res += l //(2*max_day_spread+1) 
            if l%(2*max_day_spread+1)!=0:
                res+=1

        print(int(res))


