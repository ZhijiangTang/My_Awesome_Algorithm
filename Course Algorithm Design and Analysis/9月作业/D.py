

def dfs(edge,node,pass_nodes,exit_nodes):
    if node in exit_nodes:
        return 1
    
    ans = 0
    # print(node)
    for to_node in edge[node]:
        if to_node not in pass_nodes:
            ans += dfs(edge,to_node,pass_nodes+[node],exit_nodes)
    return ans


if __name__ == '__main__':
    N = int(input())
    edge = {}
    for i in range(N-1):
        node1,node2 = list(map(int,input().split(' ')))
        if node1 not in edge:
            edge[node1] = [node2]
        else:
            edge[node1].append(node2)

        if node2 not in edge:
            edge[node2] = [node1]
        else:
            edge[node2].append(node1)

    exit_nodes = [node for node in edge if len(edge[node])==1]
    for i in range(N):
        ans = dfs(edge,i+1,[],exit_nodes)
        print(ans)