# Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer 
# and its reverse, or false otherwise.
# Constraints:
# - 0 <= num <= 105

# Example 1:
# Input: num = 443
# Output: true
# Explanation: 172 + 271 = 443 so we return true.

# Example 2:
# Input: num = 63
# Output: false
# Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            if (i + int(str(i)[::-1])) == num:
                return True
        return False