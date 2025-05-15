from math import sqrt


def cal_distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        stations = [list(map(int,input().split(' '))) for n in range(N)]
        agent = [list(map(int,input().split(' '))) for n in range(N)]
        
        min_distances = []
        for n in  range(N):
            distances = [cal_distance(stations[n],agent[i]) for i in range(N)]
            min_distances.append(min(distances))
        
        # print(round(min(min_distances),3))
        # print(f'{min(min_distances):.3f}')
        print('%.3f' % min(min_distances))



