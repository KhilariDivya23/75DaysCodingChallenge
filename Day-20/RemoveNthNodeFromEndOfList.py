class Solution:
    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n, curr, count = self.length(head) - n, head, 1
        if n == 0:
            return head.next
        while count != n:
            count += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
