import sys

input = sys.stdin.readline

def inorder_traverse(nodes, k):
    global tree, K
    if k == K or not nodes:
        return
    
    mid = len(nodes) // 2
    tree[k].append(nodes[mid])
    inorder_traverse(nodes[:mid], k + 1)
    inorder_traverse(nodes[mid + 1:], k +1)

def solution():
    global tree, K
    K = int(input())
    nodes = input().split()
    # 중위 순회한 결과를 가지고 트리 재구성
    tree =  [[] for _ in range(K)]
    inorder_traverse(nodes, 0)
    for t in tree:
        print(" ".join(t))
    
if __name__=="__main__":
    solution()