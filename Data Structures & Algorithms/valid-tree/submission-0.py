from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        return not self._has_cycle(graph, 0, -1, visited) and len(visited) == n

    def _has_cycle(self, graph, current, parent, visited):
        if current in visited:
            return True

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == parent:
                continue

            if self._has_cycle(graph, neighbor, current, visited):
                return True
