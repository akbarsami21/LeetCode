# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def doubleIt(self, head):
        current = head
        number = 0
        while current:
            number = number * 10 + current.val
            current = current.next
        
        doubled_number = number * 2
        doubled_str = str(doubled_number)[::-1]
        new_head = ListNode(int(doubled_str[0]))
        current = new_head
        for char in doubled_str[1:]:
            new_node = ListNode(int(char))
            current.next = new_node
            current = new_node
        prev = None
        current = new_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        new_head = prev
        
        return new_head
