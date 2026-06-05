class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collide(prev: int, curr: int) -> bool:
            return prev and curr and prev > 0 and curr < 0
        
        def destroy(prev: int, curr: int) -> bool:
            return abs(curr) >= prev

        s = [asteroids[0]]
        for idx in range(1, len(asteroids)):
            curr_asteroid = asteroids[idx]
            prev_asteroid = s.pop() if s else None
            while collide(prev_asteroid, curr_asteroid):
                if abs(curr_asteroid) > prev_asteroid:
                    prev_asteroid = s.pop() if s else None
                elif abs(curr_asteroid) == prev_asteroid:
                    curr_asteroid = None
                    prev_asteroid = None
                else:
                    curr_asteroid = None
            if prev_asteroid:
                s.append(prev_asteroid)
            if curr_asteroid:
                s.append(curr_asteroid)
        return s


            

            

