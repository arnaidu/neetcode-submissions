from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        
        s1_letter_frequencies = defaultdict(int)
        s2_window_frequencies = defaultdict(int)

        def compare(dict1, dict2):
            for key in dict1:
                if key not in dict2:
                    return False

                if dict1[key] != dict2[key]:
                    return False
                
            return True

        for ch in s1:
            s1_letter_frequencies[ch] += 1
        
        left = 0
        for right in range(len_s2):
            s2_window_frequencies[s2[right]] += 1
            while right - left + 1 > len_s1:
                s2_window_frequencies[s2[left]] -= 1
                left += 1

            if right - left + 1 == len_s1:
                if compare(s1_letter_frequencies, s2_window_frequencies):
                    return True
        
        return False
        


