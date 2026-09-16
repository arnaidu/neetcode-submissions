class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        ops_in_window = 0
        min_ops = float("inf")
        for right in range(len(blocks)):
            # we add right block. if black do nothing. if white increase ops_in_window by 1
            if blocks[right] == "W":
                ops_in_window += 1            


            if right - left + 1 > k:
                # Remove left block
                if blocks[left] == "W":
                    ops_in_window -= 1
                left += 1

            if right - left + 1 == k:
                min_ops = min(min_ops, ops_in_window)
        
        return min_ops
            

            

