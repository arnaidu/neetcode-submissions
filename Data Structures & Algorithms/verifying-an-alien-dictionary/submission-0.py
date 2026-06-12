class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_order = {}
        for idx, letter in enumerate(order):
            letter_order[letter] = idx
        
        queue = deque([])
        for letter in words[0]:
            queue.append(letter_order[letter])

        for idx in range(1, len(words)):
            word = words[idx]
            s = []
            for letter in word:
                if queue:
                    prev_word_letter_order = queue.popleft()
                    if prev_word_letter_order > letter_order[letter]:
                        return False
                    elif prev_word_letter_order < letter_order[letter]:
                        queue.clear()
                s.append(letter_order[letter])
            
            if queue:
                return False
            queue = deque(s)
        return True
        

                    
