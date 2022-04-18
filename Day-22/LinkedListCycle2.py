class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        count = 0
        while fast and fast.next:
            if slow == fast and count != 0:
                break
            else:
                slow = slow.next
                fast = fast.next.next
                count += 1
        entry = head
        while entry and slow:
            if entry == slow and count != 0:
                return entry
            slow = slow.next
            entry = entry.next
        return None
