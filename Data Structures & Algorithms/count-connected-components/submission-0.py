from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        from pprint import pprint
        pprint(graph)

        i, result, visited = 0, 0, set()
        for i in range(n):
            if i not in visited:
                self._bfs(graph, i, visited)
                result += 1

        return result

    def _bfs(self, graph, start, visited):
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            for nxt in graph[current]:
                if nxt not in visited:
                    queue.append(nxt)
                    visited.add(nxt)