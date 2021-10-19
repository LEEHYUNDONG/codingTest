# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultlist = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1 is not None:
                carry += l1.val1
                l1 = l1.next
            if l2 is not None:
                carry += l2.val2
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry = carry // 10

        return resultlist.next  # 첫번째 제외하고 리턴한다.
