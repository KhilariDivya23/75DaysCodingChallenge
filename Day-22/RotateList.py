class Solution:
    def length(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        k = k % self.length(head)
        if k == 0:
            return head
        else:
            n, count = self.length(head) - k, 1
            curr = head
            temp = curr.next
            while count < n:
                curr = curr.next
                temp = curr.next
                count += 1
            curr.next = None
            new_head = temp
            while temp.next:
                temp = temp.next
            temp.next = head
            return new_head
