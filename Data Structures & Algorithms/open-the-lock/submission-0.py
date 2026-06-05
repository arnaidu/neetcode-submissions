class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        front = {'0000'}
        back = {target}
        visited = {'0000', target }
        dead = set(deadends)

        if "0000" in dead:
            return -1
        if target in dead:
            return -1
        def neighbours(node):
            result = []
            for i in range(4):
                digit = int(node[i])
                up, down = (digit + 1) % 10, (digit - 1) % 10
                result.append(node[:i] + str(up) + node[i+1:])
                result.append(node[:i] + str(down) + node[i+1:])
            return result
        steps = 0
        while front and back:
            # front is always smaller of two frontiers
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for node in front:
                for neighbour in neighbours(node):
                    if neighbour in dead:
                        continue
                    if neighbour in back:
                        return steps + 1
                    if neighbour not in visited:
                        visited.add(neighbour)
                        next_front.add(neighbour)
            front = next_front
            steps += 1
        return -1
