class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_in_window = {}

        for j in range(len(nums)):
            if nums[j] in seen_in_window:
                return True

            seen_in_window[nums[j]] = j
            
            # we delete here since next iteration will be new window of size k
            if j >= k:
                del seen_in_window[nums[j - k]]

        return False