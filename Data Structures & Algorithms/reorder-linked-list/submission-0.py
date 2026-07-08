# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr,l1,l2 = head,head,head
        while curr and curr.next:
            curr = curr.next.next
            l2 = l2.next
        curr = l2.next
        prev = None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        l2.next = None
        l2 = prev
        while l1 and l2:
            l1_nxt = l1.next
            l2_nxt = l2.next
            l1.next = l2
            l2.next = l1_nxt
            l1 = l1_nxt
            l2 = l2_nxt

        

        