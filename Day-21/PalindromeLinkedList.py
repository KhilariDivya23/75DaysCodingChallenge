class Solution:
    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = self.length(head)
        n = l // 2
        first_half, count, curr = [], 1, head
        while count <= n:
            count += 1
            first_half.append(curr.val)
            curr = curr.next
        if l % 2 != 0:
            curr = curr.next
        while curr:
            if curr.val != first_half[-1]:
                return False
            first_half.pop()
            curr = curr.next
        return True
