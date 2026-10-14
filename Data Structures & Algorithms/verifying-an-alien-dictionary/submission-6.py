class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = { char: i for i, char in enumerate(order) }
        for k in range(1, len(words)):
            first, second = words[k - 1], words[k]
            j = 0
            while j < min(len(first), len(second)):
                if order_map[first[j]] > order_map[second[j]]:
                    return False
                
                if order_map[first[j]] < order_map[second[j]]:
                    break
                
                j += 1
            
            if len(first) > len(second) and j == len(second):
                return False
        
        return True

