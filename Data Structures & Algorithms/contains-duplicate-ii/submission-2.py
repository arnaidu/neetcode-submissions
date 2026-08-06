class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:       
        i = 0
        seen_in_range = {}
        for j in range(len(nums)):
            if j - i > k:
                seen_in_range[nums[i]] -= 1
                if seen_in_range[nums[i]] == 0:
                    del seen_in_range[nums[i]]
                i += 1

            # at this point we are back to the range <= k after removing the nums[i]
            # so if current num seen still, then we good
            if nums[j] in seen_in_range:
                return True
            else:
                seen_in_range[nums[j]] = 1
        return False
                
            

            
            
            

