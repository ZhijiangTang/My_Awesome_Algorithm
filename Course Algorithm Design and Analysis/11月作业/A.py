

if __name__ == '__main__':
    M, S, C = list(map(int, input().split()))
    occupied_stall = [int(input()) for i in range(C)]
    occupied_stall.sort()
    distance_occupied_stall = [occupied_stall[i]-occupied_stall[i-1]-1 for i in range(1, C)]
    
    if M == 1:
        res = occupied_stall[-1]-occupied_stall[0]+1
    else:
        distance_occupied_stall.sort(reverse=True)
        res = sum(distance_occupied_stall[:M-1])
        res += occupied_stall[0]-1+S-occupied_stall[-1]
        res = S-res

    print(res)