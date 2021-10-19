# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev_word(word):
            data = deque([])
            cnt = 0
            while word:
                data.appendleft(word.val)
                word = word.next
                cnt += 1
            return data, cnt

        def convertNum(num, l):
            tmp = 0
            while num:
                tmp += num.popleft()*(10**(l-1))
                l -= 1
            return tmp

        tmp1, length1 = rev_word(l1)
        tmp2, length2 = rev_word(l2)
        num1, num2 = convertNum(tmp1, length1), convertNum(tmp2, length2)
        res = list(str(num1+num2))
        head_ans = ListNode()
        l3 = head_ans
        while res:
            tmp = int(res.pop())
            l3.val = tmp
            if res:
                l3.next = ListNode(0, None)
                l3 = l3.next
            else:
                l3.next = None
                break
        return head_ans
