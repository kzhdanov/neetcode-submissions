"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        curr = head
        curr2 = head

        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        while curr2:
            clone = hashMap[curr2]
            clone.next = hashMap.get(curr2.next)
            clone.random = hashMap.get(curr2.random)

            curr2 = curr2.next

        return hashMap.get(head)



          