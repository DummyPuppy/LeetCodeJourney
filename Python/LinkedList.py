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

    # to sort two sorted linkedlists
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        curr = dummy = ListNode()

        p1,p2 = list1, list2
        while (p1 and p2):
            if (p1.val < p2.val):
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        while p1:
            curr.next = p1
            curr = curr.next
            p1 = p1.next
        while p2:
            curr.next = p2
            curr = curr.next
            p2 = p2.next
        return dummy.next
