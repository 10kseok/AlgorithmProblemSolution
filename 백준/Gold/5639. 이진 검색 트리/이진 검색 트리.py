import sys        
sys.setrecursionlimit(10 ** 6)

pre_order = []
post_order_route = []

while True:
    try:
        node = int(sys.stdin.readline())
        pre_order.append(node)  
    except:
        break

def post_order(start, end):
    if start >= end:
        return
    mid = start + 1

    for i in range(start + 1, end):
        if pre_order[start] < pre_order[i]:
            # 루트보다 큰 값은 오른쪽 서브트리에 해당한다.
            mid = i
            break

    post_order(start + 1, mid) # 다음 인덱스를 루트로 보고 다시 왼쪽 서브트리를 찾는다.
    post_order(mid, end) # 오른쪽 서브트리로 나눈다.
    post_order_route.append(f'{pre_order[start]}') # 루트 값을 경로에 저장한다.

post_order(0, len(pre_order))
print("\n".join(post_order_route))