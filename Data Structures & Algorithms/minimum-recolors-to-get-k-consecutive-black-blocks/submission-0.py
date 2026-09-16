class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        ops_in_window = 0
        min_ops = float("inf")
        for right in range(len(blocks)):
            if right - left + 1 <= k:
                if blocks[right] == "W":
                    ops_in_window += 1
            else:               
                # we add right block. if black do nothing. if white increase ops_in_window by 1
                if blocks[right] == "W":
                    ops_in_window += 1

                # we move left block. If it is black do nothing. If white, reduce ops_in_window by 1
                if blocks[left] == "W":
                    ops_in_window -= 1
                
                left += 1

                min_ops = min(min_ops, ops_in_window)
        
        return min(min_ops, ops_in_window)
            

            

