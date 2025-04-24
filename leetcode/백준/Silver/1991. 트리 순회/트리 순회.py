def pre_order(node_key):
    if node_key == '.':
        return
    
    pre_order_list.append(node_key)
    pre_order(tree[node_key][0])
    pre_order(tree[node_key][1])

def in_order(node_key):
    if node_key == '.':
        return
    
    in_order(tree[node_key][0])
    in_order_list.append(node_key)
    in_order(tree[node_key][1])

def post_order(node_key):
    if node_key == '.':
        return
    
    post_order(tree[node_key][0])
    post_order(tree[node_key][1])
    post_order_list.append(node_key)

n = int(input())
tree = {}

pre_order_list = []
in_order_list = []
post_order_list = []

for i in range(n):
    key, left, right = input().split()
    tree[key] = [left, right]

pre_order("A")
in_order("A")
post_order("A")

print("".join(pre_order_list))
print("".join(in_order_list))
print("".join(post_order_list))