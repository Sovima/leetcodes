# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head == None or head.next is None:
            return head
        end = head
        l = 1
        while end.next is not None:
            l+=1
            end = end.next   
        start = head
        new_head = head
        print(k)
        k = l - k % l
        print(k)
        if k == l:
            return head
        new_end = None
        while k > 0:
            k -= 1
            new_end = new_head
            new_head = new_head.next
        end.next = start
        new_end.next = None
        return new_head
            
        
        
        
