
def f(permutation:list, rest:list,n):
    if len(rest) == 0:
        return permutation
    result = []
    for i,r in enumerate(rest):
        for p in permutation:
            if (2*r-p) in rest:
                break
        if (2*r-p) not in rest:
            rest_copy = rest.copy()
            result = f(permutation+[rest_copy.pop(i)], rest_copy,n)
            if len(result) == n:
                return result
    return result

def get_n_5():
    n = 5
    rest = list(range(n))
    for i in range(n):
        rest_copy = rest.copy()
        result = f([rest_copy.pop(i)],rest_copy,n)
        if len(result) == n:
            print(f'{n}:{" ".join(map(str,result))}')
            break

def check(l):

    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            if 2*l[j]-l[i] in l[j:]:
                return 0
    return 1


if __name__ == '__main__':

    l = [0 ,4 ,2,1 ,3]
    # 0 8 4 2 1 6 9 5 3 7
    # print(check(l))
    for i in range(11):
        l = [2*j for j in l] + [2*j+1 for j in l]
    # print(check(l))

    while(1):
        n = int(input())
        if n == 0:
            break

        result = [i for i in l if i<n]
        print(f'{n}:{" ".join(map(str,result))}')
