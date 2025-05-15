# from itertools import groupby

# def subtract_min(lst):
#     min_value = min(lst)
#     return [x - min_value for x in lst]

# if __name__ == '__main__':
#     N = int(input())
#     N_cards = [int(input()) for i in range(N)]
#     conti_list = [N_cards.copy()]
    
#     res = 0
#     while(len(conti_list)!=0):
#         conti_list_next = []
#         for l in conti_list:
#             res += min(l)
#             conti_list_next += [list(group) for key, group in groupby(subtract_min(l), lambda x: x == 0) if not key]
#         conti_list = conti_list_next
    
#     print(res)
        

# from itertools import groupby

# def subtract_min(lst):
#     min_value = min(lst)
#     return [x - min_value for x in lst]

# def f(conti_list:list):
#     if len(conti_list)==1:
#         return conti_list[0]
    
#     res = min(conti_list)
#     conti_list_next = [list(group) for key, group in groupby(subtract_min(conti_list), lambda x: x == 0) if not key]
#     for l in conti_list_next:
#         res += f(l)
#     return res


# if __name__ == '__main__':
#     N = int(input())
#     N_cards = [int(input()) for i in range(N)]

#     res = f(N_cards)
#     print(res)


if __name__ == '__main__':
    N = int(input())
    N_cards = [int(input()) for i in range(N)]

    res = N_cards[0]
    for i in range(N-1):
        if N_cards[i+1]>N_cards[i]:
            res += N_cards[i+1] - N_cards[i]
    
    print(res)