class Solution:
    def rob(self, nums: List[int]) -> int:
        # X1, X2, X3, X4, X5, X6, X7
        """
        we rob either x1 or x2
        then if we rob x1, we can rob either x3 or x4
        """
        dp = [0] * len(nums)
        max_amount = 0
        for idx, amount in enumerate(nums):
            # if i had robbed three houses prior if possible
            if idx - 3 >= 0:
                dp[idx] = max(dp[idx - 2], dp[idx - 3]) + amount
            elif idx - 2 == 0:
                dp[idx] = dp[idx - 2] + amount
            else:
                dp[idx] = amount
            
            max_amount = max(max_amount, dp[idx])

        return max_amount
            

            

