# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 이진 트리내에서 k번째 작은 수를 찾아라

        # 제약 조건
        # 1. 노드의 갯수는 1 ~ 10_000개
        # 2. 노드의 값은 0 ~ 10_000

        # 문제
        # 1. 모든 수를 파악해서 k번째 수를 찾아야함
        # 2. 모든 수를 파악하기 위해선 트리를 전부 탐색해야함

        # 풀이
        # 1. 현재 노드의 값을 저장한다.
        # 2. 각 노드(왼쪽, 오른쪽)이 존재하면 탐색을 이어나가면서 1번부터 다시 진행한다. 
        # 3. 다음 노드가 null인 경우에는 탐색을 종료한다.
        # 4. 노드의 값들을 저장한 배열을 정렬한 뒤 k번째 수를 반환한다.
        
        values = []
        def find_value(node: TreeNode | None):
            if node:
                values.append(node.val)
                find_value(node.left)
                find_value(node.right)
        
        find_value(root)

        return sorted(values)[k - 1]