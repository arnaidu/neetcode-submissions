class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_order = {}
        for idx, letter in enumerate(order):
            letter_order[letter] = idx
        
        prevWord = words[0]
        currWord = None
        for idx in range(1, len(words)):
            currWord = words[idx]
            check_lengths = True
            for letter_idx in range(min(len(currWord), len(prevWord))):
                currWordLetterOrder = letter_order[currWord[letter_idx]]
                prevWordLetterOrder = letter_order[prevWord[letter_idx]]
                if prevWordLetterOrder > currWordLetterOrder:
                    return False
                elif prevWordLetterOrder < currWordLetterOrder:
                    prevWord = currWord
                    check_lengths = False
                    break

            # this means we had equal order, but prevWord is longer
            # which breaks lexicographical ordering
            if check_lengths and len(currWord) < len(prevWord):
                return False

        return True
        

                    
