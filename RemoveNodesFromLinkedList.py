# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        if not head:
            return None
        self.maxValue = float('-inf')
        def traverse(node):
            if not node:
                return None
            node.next = traverse(node.next)
            if node.val >= self.maxValue:
                self.maxValue = node.val
                return node
            else:
                return node.next
        return traverse(head)
# obj=Solution()
# print(obj.removeNodes([5,2,13,3,8]))