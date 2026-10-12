class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for source, target, travel_time in times:
            graph[source].append((target, travel_time))

        min_heap, visited, max_arrival_time = [(0, k)], set(), 0
        while min_heap:
            arrival_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            max_arrival_time = arrival_time

            for neighbor, edge_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (arrival_time + edge_time, neighbor))

        return max_arrival_time if len(visited) == n else -1
        