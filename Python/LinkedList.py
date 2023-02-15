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

    #swap nodes in pairs
    #key is to exchange values!
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head

        while curr != None and curr.next != None:
            first_val = curr.val
            after  = curr.next
            after_val = after.val
            after.val = first_val
            curr.val = after_val
            curr = curr.next.next
        return head

#swap nodes at kth from the head and kth from the tail
#key point is that it only needs to iterate k-1 times 
#if you assign it to be the head at first!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = slow = head
        for i in range(k-1):
            fast = fast.next
        
        swap1 = fast

        while swap1.next:
            slow = slow.next
            swap1 = swap1.next
        
        val1 = fast.val
        print(val1)
        print(slow.val)
        fast.val = slow.val
        slow.val = val1
        return head
