class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        i, j = 0, 1
        seen_in_window = { nums[i] : i }
        while j < len(nums):
            if abs(i - j) > k:
                del seen_in_window[nums[i]]
                i += 1
                continue

            if nums[j] in seen_in_window:
                return True
            
            seen_in_window[nums[j]] = j
            j += 1
        
        return False