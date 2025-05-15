# def f(result,rest,D):
#     if sum(result+[0]) == D:
#         return [result]
#     if len(rest) == 0:
#         return []

#     ans = []
#     for i in range(len(rest)):
#         if sum(result+[0]) + rest[i] <= D:
#             rest_copy = rest.copy()
#             res = f(result+[rest_copy.pop(i)],rest_copy,D)
#             ans += res

#     return ans


# def dfs():
#     def f(result,i,W, D):
#         if i == len(W):
#             return []
#         ans = set()
#         if sum(result)+W[i] == D:
#             ans.add(len(result)+1)

#             if 0 in W:
#                 ans.add(len(result)+2)
#             if len(ans) >= 2:
#                 return ans

#         if (sum(result)+W[i] < D):
#             res = f(result+[W[i]],i+1,W,D)
#             ans = ans.union(res)
#             if len(ans) >= 2:
#                 return ans

#         if sum(W[i:]+result)-W[i] >= D:
#             res = f(result,i+1,W,D)
#             ans = ans.union(res)
#             if len(ans) >= 2:
#                 return ans

#         return ans

#     T = int(input())
#     for t in range(T):
#         N,D = list(map(int,input().split(' ')))
#         w = list(map(int,input().split(' ')))
#         ans = list(f([],0,w,D))
#         if D == 0:
#             ans.append(0)
#         # print(ans)
#         if len(ans)==1:
#             print(f"Case #{t+1}: {ans[0]}")
#         elif len(ans)>1:
#             print(f"Case #{t+1}: AMBIGIOUS")
#         else:
#             print(f"Case #{t+1}: IMPOSSIBLE")


def f(W,n):
    if len(W)==1:
        if W[0]==0:
            return {0:{0,1}}
        return {0:{0},W[0]:{1}}

    left = f(W[:n//2],n//2)
    right = f(W[n//2:],n-n//2)

    result = {}
    for i in right:
        for j in left:
            if i+j not in result:
                result[i+j] = set()

            result[i+j] = result[i+j].union([((k<<(n//2))+l) for k in right[i] for l in left[j]])
    return result


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N,D = list(map(int,input().split(' ')))
        W = list(map(int,input().split(' ')))
        left = f(W[:N//2],N//2)
        right = f(W[N//2:],N-N//2)

        ans = set()
        for weight in left:
            if D-weight in right:
                ans = ans.union([bin(i).count('1')+bin(j).count('1') for i in right[D-weight] for j in left[weight]])
            if len(ans)>1:
                break
            
        if len(ans)==1:
            print(f"Case #{t+1}: {list(ans)[0]}")
        elif len(ans)>1:
            print(f"Case #{t+1}: AMBIGIOUS")
        else:
            print(f"Case #{t+1}: IMPOSSIBLE")

