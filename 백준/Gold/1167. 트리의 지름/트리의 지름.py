import sys
input = sys.stdin.readline

def solution():
    global longest_node, max_length
    V = int(input())
    tree = [[] for _ in range(V + 1)]
    for _ in range(V):
        graph = list(map(int, input().split()))
        node_num = graph[0]
        for i in range(1, len(graph) - 1, 2):
            tree[node_num].append((graph[i], graph[i + 1]))
    
    longest_node, max_length = 0, 0
    visited = [False] * (V + 1)
    def dfs_tree(i, length):
        global max_length, longest_node
        if visited[i]:
            return
        if max_length < length:
            max_length = length
            longest_node = i
            
        visited[i] = True
        for next_node in tree[i]:
            vertex, edge = next_node
            if not visited[vertex]:
                dfs_tree(vertex, length + edge)
    
    dfs_tree(1, 0)
    visited, max_length = [False] * (V + 1), 0
    dfs_tree(longest_node, 0)
    print(max_length)
            
    
if __name__=="__main__":
    solution() 

