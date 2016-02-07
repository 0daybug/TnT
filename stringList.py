class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
        return head
        
