# Palindrome is an integer that reads the same backward as forward
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

sol = Solution()
nums = [121, -121, 0, 123]
num: int
for num in nums:
    ans = sol.isPalindrome(num)
    print(f"Answer is {ans}")