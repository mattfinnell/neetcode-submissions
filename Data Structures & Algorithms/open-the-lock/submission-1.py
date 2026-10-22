class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        queue, visited = deque([("0000", 0)]), set(deadends)

        while queue:
            combo, depth = queue.popleft()

            if combo == target:
                return depth

            for neighbor in self.get_neighbors(combo):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1

    def get_neighbors(self, combo):
        for i in range(4):
            for d in [-1, 1]:
                digit = str((int(combo[i]) + d) % 10)

                yield combo[:i] + digit + combo[i + 1:]

