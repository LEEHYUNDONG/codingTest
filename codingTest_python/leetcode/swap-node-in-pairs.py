# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4
prev curr
curr prev
1 2 3
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head

        while curr != None and curr.next != None:
            # 현재노드 값, 현재노드 다음 값
            prev, curr = curr, curr.next
            # 값만 swap
            prev.val, curr.val = curr.val, prev.val
            # 현재 포인터 다음 포인터로 이동
            curr = curr.next
        
        return head
        