class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        i, n = 0, len(digits)
        while i < n:
            if i == 0:
                digits[i] += 1
            if digits[i] > 9:
                if i == n-1:                
                    digits[i] = 0
                    digits.append(1)
                else:
                    digits[i] %= 10
                    digits[i+1] += 1
            else:
                digits[i] += (digits[i-1] // 10)
            i += 1
        return reversed(digits)
