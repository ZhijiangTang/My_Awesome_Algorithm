

if __name__ == '__main__':
    A,B,C,K = list(map(int,input().split()))
    K -= A
    if K <=0 :
        print(A+K)
    else:
        K -= B
        if K <= 0:
            print(A)
        else:
            print(A-K)