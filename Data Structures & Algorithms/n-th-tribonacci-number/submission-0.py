class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]

        for i in range(2, n):
            t_next = t[2] + t[1] + t[0]
            t[2], t[1], t[0] = t_next, t[2], t[1]
        return t[-1]
