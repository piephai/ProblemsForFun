# Two sums look for two numbers that equals the target in a list of numbers

class Solution:
    def twoSum(self, nums, target):
            h = {}
            for i, num in enumerate(nums):
                counterval = target - num
                if counterval in h:
                        return h[counterval], i
                else: 
                    h[num] = i

sol = Solution()    
ans = sol.twoSum([2, 3, 7, 9, 8, 6, 5, 4, 11], 13)
print(f"answer is {ans}")

