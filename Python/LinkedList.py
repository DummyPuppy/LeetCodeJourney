# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# to rotate a list by k steps to the right
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        count = 1
        while (temp.next !=None):
            temp = temp.next
            count+=1
        k = k % count
        if k == 0:
            return head 
        move = count - k
        curr = head
        for i in range(move-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        temp.next = head
        return newHead 
