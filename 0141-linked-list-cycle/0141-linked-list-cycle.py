# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 연결 리스트의 사이클 판단

        # 제약 조건
        # 1. 노드의 갯수는 0 ~ 10_000개
        # 2. 노드의 값은 -100_000 이상 100_000 이하
        # 3. tail의 다음 포인터는 사이클이면 정수, 사이클이 아니면 -1

        # 문제
        # 1. 각 노드는 값과 다음 노드에 대한 포인터를 가진다
        # 2. 연결 리스트므로 인덱스를 가지지 않아 별도 계산이 필요하다
        # 3. 사이클을 판단하기 위한 각 노드의 방문 여부 확인이 필요하다

        # 풀이 1
        # 1. 노드를 탐색할 때마다 노드의 값을 변경하여 방문 여부를 표시한다
        #  1-1. 최대값이 100_000이므로 방문시 값을 1_000_000 + 인덱스로 바꾼다
        # 2. 방문했던 곳을 탐색하거나 다음 포인터가 None일 때까지 탐색을 이어간다.
        # 3. 다음 포인터가 None 이면 False 반환
        # 4. 방문했던 곳이라면 True 반환한다.

        # idx = 0
        # node = head
        # while node and node.next:
        #     if not node.next:
        #         return False
        #     if node.val >= 1_000_000:
        #         return True
        #     node.val = 1_000_000 + idx
        #     idx += 1
        #     node = node.next

        # return False

        # 풀이 2
        # 1. 한칸씩 이동하는 탐색자(slow)를 둔다
        # 2. 두칸씩 이동하는 탐색자(fast)를 둔다
        # 3. 두칸 탐색자가 탐색을 이어나가다 보면 사이클인 경우 한칸 탐색자를 만난다
        # 4. 해당 경우에는 사이클이 존재함을 알 수 있다

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False