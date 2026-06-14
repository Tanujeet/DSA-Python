# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        maxVal = 0


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr,prev = slow,None

        while curr:
           nxt = curr.next
           curr.next = prev
           prev = curr
           curr = nxt

        while prev:
            maxVal = max(maxVal,head.val+prev.val)
            prev = prev.next
            head = head.next
        return maxVal         
            